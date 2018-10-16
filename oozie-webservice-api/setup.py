from setuptools import setup, find_packages

setup(
    name             = 'oozie-webservice-api',
    version          = '0.3',
    description      = 'Python wrapper for Oozie Webservice REST API',
    long_description = open('README.rst').read(),
    author           = 'whitebeard-k',
    author_email     = 'fluorite118@gmail.com',
    url              = 'https://github.com/developer-sdk/oozie-webservice-api',
    download_url     = 'https://github.com/developer-sdk/oozie-webservice-api/archive/master.zip',
    packages         = find_packages(),
    keywords         = ['oozie', 'webservice', 'api']
)
