from setuptools import find_packages, setup


setup(
    name='wirescreen-api',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        "requests==2.22.0",
        "validators==0.14.2",
    ]
)
