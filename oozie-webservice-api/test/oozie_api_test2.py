'''
Created on Feb 26, 2019

@author: seo
'''
from sdk.OozieApi import OozieWebService

def main():
    ows = OozieWebService('http://127.0.0.1:8080')
    ows.admin.build_version()

if __name__ == '__main__':
    main()