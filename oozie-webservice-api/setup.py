from setuptools import setup, find_packages

setup(
    name             = 'oozie-webservice-api',
    version          = '1.1.0',
    description      = 'Python wrapper for Oozie Webservice REST API',
    long_description = open('README.rst').read(),
    license          = 'MIT',
    author           = 'hs_seo',
    author_email     = 'fluorite118@gmail.com',
    url              = 'https://github.com/developer-sdk/oozie-webservice-api',
    download_url     = 'https://github.com/developer-sdk/oozie-webservice-api/archive/master.zip',
    packages         = find_packages(exclude = ['test']),
    keywords         = ['oozie', 'webservice', 'api'],
    python_requires  = '>=2.6',
    classifiers=[
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 3',
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
    ],
)
