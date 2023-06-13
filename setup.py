import codecs
import os
import re

from setuptools import setup


dirname = os.path.abspath(os.path.dirname(__file__))

with codecs.open(
    os.path.join(dirname, "undetected_chromedriver", "__init__.py"),
    mode="r",
    encoding="utf-8",
) as fp:
    try:
        version = re.findall(r"^__version__ = ['\"]([^'\"]*)['\"]", fp.read(), re.M)[0]
    except Exception:
        raise RuntimeError("unable to determine version")

description = (
    "Selenium.webdriver.Chrome replacement with compatiblity for Brave, and other Chromium based browsers.",
    "Not triggered by CloudFlare/Imperva/hCaptcha and such.",
    "NOTE: results may vary due to many factors. No guarantees are given, except for ongoing efforts in understanding detection algorithms.",
)

setup(
    name="undetected-chromedriver",
    version=version,
    packages=["src"],
    install_requires=[
        "selenium>=4.9.0",
        "requests",
        "websockets",
    ],
    package_data={"undetected_chromedriver": [os.path.join("example", "example.py")]},
    url="https://github.com/ultrafunkamsterdam/undetected-chromedriver",
    license="GPL-3.0",
    author="UltrafunkAmsterdam",
    author_email="info@blackhat-security.nl",
    description=description,
    long_description=open(os.path.join(dirname, "README.md"), encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
