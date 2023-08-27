from setuptools import find_packages
from setuptools import setup

__version__ = "0.1"

setup(
    name="core",
    version=__version__,
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "flask==2.2",
        "flask-sqlalchemy==3.0.3",
        "flask-restful",
        "flask-migrate",
        "flask-jwt-extended",
        "flask-marshmallow",
        "marshmallow-sqlalchemy",
        "python-dotenv",
        "passlib",
        "apispec[yaml]",
        "apispec-webframeworks",
    ]
)
