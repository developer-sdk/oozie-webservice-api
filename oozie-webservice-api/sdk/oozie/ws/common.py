#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib, json, urllib2
import xml.etree.ElementTree as ET

PRINT_DEBUG = True
OOZIE_URL = "http://localhost:11000"
_HTTP_REQUEST_TYPE_ = [ "GET", "PUT" ]

def check_param_values(param_index, check_list):
    ''' param_index로 전달된 데이터가, check_list에 있는 데이터 인지 확인하고 오류를 발생하는 데코레이터  '''
    
    def wrapper(func):
        def decorator(*args, **kwargs):
            if args[param_index] not in check_list:
                raise ValueError("args error {0} not in [{1}]".format(args[param_index], ",".join(check_list)))
            
            return func(*args, **kwargs)
        return decorator
    return wrapper

def send_url(request_url):
    '''send url and get request_get'''
    
    if PRINT_DEBUG:
        print(request_url)
    
    response = urllib.urlopen(request_url).read()
    
    if PRINT_DEBUG:
        print(response)
    
    json_obj = json.loads(response)
    
    if PRINT_DEBUG:
        print(json.dumps(json_obj, indent=4, sort_keys=True))
        
    return json_obj

def param_encode(params):
    return urllib.urlencode(params)

def request_get(request_url):
    return request(request_url, "GET")

def request_put(request_url):
    return request(request_url, "PUT")

@check_param_values(1, _HTTP_REQUEST_TYPE_)
def request(request_url, request_type="GET"):
    '''send url and get request_get'''
    
    if PRINT_DEBUG:
        print(request_url)
    
    opener = urllib2.build_opener(urllib2.HTTPHandler)  
    request_get = urllib2.Request(request_url)
    request_get.get_method = lambda: request_type
    response = opener.open(request_get)
    
    response_info = response.info()
    response_body = response.read()
    
    if PRINT_DEBUG:
        print(response_info.getheader("Content-Type"))
    
    content_type = response.info().getheader("Content-Type")
    
    if content_type.startswith("application/json"): 
        json_obj = json.loads(response_body)
        
        if PRINT_DEBUG:
            print(json.dumps(json_obj, indent=4, sort_keys=True))
            
        return json_obj
    
    elif content_type.startswith("application/xml"):
        root = ET.fromstring(response_body)
        
        if PRINT_DEBUG:
            ET.dump(root)
        
        return root
    elif content_type.startswith("text/plain"):
        return response_body
    elif content_type.startswith("image/png"):
        return response_body
    else:
        raise ValueError("unknown Content-Type")