from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

# get version from __version__ variable in umt_nfe/__init__.py
from umt_nfe import __version__ as version

setup(
    name="umt_nfe",
    version=version,
    description="National Federation of Education Management System",
    author="Codeium",
    author_email="contact@codeium.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)
