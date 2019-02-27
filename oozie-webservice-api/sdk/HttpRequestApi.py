#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib, json, urllib2, logging
import xml.etree.ElementTree as ET
from urllib2 import HTTPError
'''
Created on Feb 11, 2019

@author: whitebeard-k
'''

class HttpRequest(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.logger = logging.getLogger("{0}".format(self.__class__))
        
    def debug(self, message):
        self.logger.debug(message)
    
    def param_encode(self, params):
        return urllib.urlencode(params)
    
    def request_get(self, request_url, params=None):
        if params:
            return self.request('{0}?{1}'.format(request_url, self.param_encode(params), "GET"))
        
        return self.request(request_url, "GET")
    
    def request_put(self, request_url, xml=""):
        return self.request(request_url, "PUT", xml)
    
    def request_post(self, request_url, xml):
        return self.request(request_url, "POST", xml)
    
    def request(self, request_url, request_type="GET", xml=""):
        '''send url and get response'''
        
        self.debug("request: {0}".format(request_url))
        
        opener = urllib2.build_opener(urllib2.HTTPHandler)
        request_get = urllib2.Request(request_url, xml, {'Content-Type': 'application/xml'}) if request_type in ("PUT", "POST") else urllib2.Request(request_url) 
        request_get.get_method = lambda: request_type
        
        try:
            response = opener.open(request_get)
        except HTTPError as hpe:
            self.logger.exception(hpe)
            return 
        
        response_info = response.info()
        response_body = response.read()
        
        self.debug("response header: {0}".format(response_info.getheader("Content-Type")))
        
        content_type = response.info().getheader("Content-Type")
        
        if content_type is None:
            return 
        
        if content_type.startswith("application/json"): 
            json_obj = json.loads(response_body)
            
            self.debug(json.dumps(json_obj, indent=4, sort_keys=True))
                
            return json_obj
        
        elif content_type.startswith("application/xml"):
            root = ET.fromstring(response_body)
            
            self.debug("-- response xml --")
            ET.dump(root)
            
            return root
        
        elif content_type.startswith("text/plain"):
            self.debug("-- response txt --")
            print(response_body)
                
            return response_body
        
        elif content_type.startswith("image/png"):
            self.debug("-- response image --")
            
            return response_body
        
        else:
            raise ValueError("unknown Content-Type")