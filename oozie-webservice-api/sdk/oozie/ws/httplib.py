#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib, json, urllib2
import xml.etree.ElementTree as ET
from urllib2 import HTTPError
from sdk.oozie.ws.util.decorator import check_param_name_values

PRINT_DEBUG = True
OOZIE_URL = ""
_HTTP_REQUEST_TYPE_ = [ "GET", "PUT", "POST" ]

def param_encode(params):
    return urllib.urlencode(params)

def request_get(request_url):
    return request(request_url, "GET")

def request_put(request_url, xml=""):
    return request(request_url, "PUT", xml)

def request_post(request_url, xml):
    return request(request_url, "POST", xml)

@check_param_name_values("request_type", _HTTP_REQUEST_TYPE_)
def request(request_url, request_type="GET", xml=""):
    '''send url and get response'''
    
    if PRINT_DEBUG:
        print("request: {0}".format(request_url))
    
    opener = urllib2.build_opener(urllib2.HTTPHandler)
    request_get = urllib2.Request(request_url, xml, {'Content-Type': 'application/xml'}) if request_type in ("PUT", "POST") else urllib2.Request(request_url) 
    request_get.get_method = lambda: request_type
    
    try:
        response = opener.open(request_get)
    except HTTPError as hpe:
        print("-- HTTPError --")
        print("  error code: {0}".format(hpe.code))
        print("     message: {0}".format(hpe.msg))
        error_html = hpe.read()
        print("  error html: {0}".format(error_html))
        return 
    
    response_info = response.info()
    response_body = response.read()
    
    if PRINT_DEBUG:
        print("response header: {0}".format(response_info.getheader("Content-Type")))
    
    content_type = response.info().getheader("Content-Type")
    
    if content_type is None:
        print("-- process ok --")
        return 
    if content_type.startswith("application/json"): 
        json_obj = json.loads(response_body)
        
        if PRINT_DEBUG:
            print("-- response json body --")
            print(json.dumps(json_obj, indent=4, sort_keys=True))
            
        return json_obj
    
    elif content_type.startswith("application/xml"):
        root = ET.fromstring(response_body)
        
        if PRINT_DEBUG:
            print("-- response xml --")
            ET.dump(root)
        
        return root
    elif content_type.startswith("text/plain"):
        if PRINT_DEBUG:
            print("-- response txt --")
            print(response_body)
            
        return response_body
    elif content_type.startswith("image/png"):
        if PRINT_DEBUG:
            print("-- response image --")
        
        return response_body
    else:
        raise ValueError("unknown Content-Type")
    