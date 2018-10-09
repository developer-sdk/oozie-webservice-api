from setuptools import setup, find_packages

setup(
    name             = 'oozie-webservice',
    version          = '1.0',
    description      = 'Python wrapper for Oozie Webservice REST API',
    author           = 'whitebeard-k',
    author_email     = 'fluorite118@gmail.com',
    url              = 'https://github.com/developer-sdk/oozie-webservice-api',
    download_url     = 'https://github.com/developer-sdk/oozie-webservice-api/archive/1.0.tar.gz',
    install_requires = [ ],
    packages         = find_packages(exclude = ['test*']),
    keywords         = ['oozie', 'webservice', 'api'],
    python_requires  = '>=2.7'
)