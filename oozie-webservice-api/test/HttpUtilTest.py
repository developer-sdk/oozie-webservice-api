'''
Created on Apr 9, 2019

@author: seo
'''
from sdk.oozie.ws.HttpUtil import HttpRequest

def request_naver():
    http = HttpRequest()
    response = http.request("http://www.naver.com")
    
    print response.headers
    print response.headers['Content-Type']
    print response.code
    print response.body

if __name__ == "__main__":
    request_naver()