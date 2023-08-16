import codecs
import os
import re
from pathlib import Path
from setuptools import setup


dirname = os.path.abspath(os.path.dirname(__file__))

deps = Path('requirements.txt').read_text().splitlines()
# deps.append("urllib3==1.25.11")

path_to_change = os.path.join(dirname, "src")

os.chdir(path_to_change)

dirname = path_to_change


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
)

setup(
    name="undetected-chromedriver",
    version=version,
    packages=["undetected_chromedriver"],
    install_requires=deps,
    py_modules=['utils'],
    url="https://github.com/sellamanic/FlareSolverr",
    license="GPL-3.0",
    author="xkjjdsasuw",
    description=description,
)
