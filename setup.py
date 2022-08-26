from setuptools import setup
import re

version = ""

with open("Qiipy/__init__.py", mode="r", encoding="utf8") as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

with open("README.md", mode="r", encoding="utf8") as f:
    description = f.read()

requirement = "requests"

setup(
    name='pyqiita',
    long_description=description,
    version=version,
    packages=['qiipy'],
    url='https://github.com/peco2282/Qiipy',
    license='MIT',
    author='peco2282',
    author_email='pecop2282@gmail.com',
    description='An API wrapper for Qiita.',
    install_requires=["requests"],
    long_description_content_type="text/markdown"
)
