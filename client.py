import requests
import json
import base64


class ChromeFlare(object):
    endpoint = 'http://localhost:8191/v1'

    def __init__(self, session=None, timeout=60000, proxy=None):
        self.timeout = timeout
        self.session = session
        self.proxy = proxy
        self.create_session(session)
        self._text = None

    def _payload(self, cmd="request.get"):
        json_data = {
            'cmd': cmd,
            'maxTimeout': self.timeout
        }
        if self.session:
            json_data["session"] = self.session

        if self.proxy:
            json_data["proxy"] = {'url': f'http://{self.proxy}'}

        return json_data

    @property
    def _headers(self, ):
        return {'Content-Type': 'application/json'}

    def get_response(self, payload):
        return requests.post(self.endpoint, headers=self._headers, json=payload).json()

    def request(self, url=None, rules=None, operation=None, value=None, selector=None, script=None):
        cmd = 'request.post' if operation and operation in ["type", "click", "option"] else 'request.get'
        payload = self._payload(cmd=cmd)
        payload["operation"] = operation
        if url:
            payload["url"] = url
        payload["value"] = value
        payload["selector"] = selector
        payload["script"] = script

        print(payload)

        resp = self.get_response(payload)

        return resp

    def create_session(self, session_id):
        if session_id:
            response = self.get_response(self._payload(cmd="sessions.create"))

    def get(self, url, params: dict = {}):
        if params:
            query_string = "&".join([f"{key}={value}" for key, value in params.items()])
            url = f"{url}?{query_string}"

        info = self.request(url=url)

        self._text = info.get("solution", {}).get("response")
        return self

    @property
    def current_url(self, ):
        return self.request(operation="current_url")["data"]

    @property
    def text(self, ):
        if self._text:
            return self._text
        return self.request(operation="text")["data"]

    @property
    def page_source(self, ):
        return self.text

    def as_png(self, *args, **kwargs):
        png = base64.b64decode(self.request(operation='as_png')["data"])
        return png

    def element_as_png(self, selector):
        img = self.request(operation='element_as_png', selector=selector)["data"]
        png = base64.b64decode(img)
        return png

    def click(self, selector):
        self.request(operation='click', selector=selector)

    def type(self, selector, value):
        self.request(operation='type', selector=selector, value=value)

    def option(self, selector, value):
        self.request(operation='option', selector=selector, value=value)

    @property
    def cookies(self, ):
        return self.request('cookies')

    def execute_script(self, script):
        return self.request(operation='execute_script', script=script)

    def quit(self, ):
        self.request(self._payload(cmd="sessions.destroy"))

    def close(self, ):
        self.request(self._payload(cmd="sessions.destroy"))
