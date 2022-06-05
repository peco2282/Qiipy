from setuptools import setup
import re

version = ""

with open("Qiipy/__init__.py", mode="r", encoding="utf8") as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

requirement = "requests"

setup(
    name='pyqiita',
    version=version,
    packages=['qiipy'],
    url='https://github.com/peco2282/Qiipy',
    license='MIT',
    author='peco2282',
    author_email='pecop2282@gmail.com',
    description='An API wrapper for Qiita.'
)
