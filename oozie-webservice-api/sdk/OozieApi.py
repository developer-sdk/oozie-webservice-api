#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Feb 25, 2019

@author: seo
'''
from sdk.HttpRequestApi import HttpRequest

class OozieHttpApi(HttpRequest):

    COMMAND_V1 = "oozie/v1/"
    COMMAND_V2 = "oozie/v2/"


    def __init__(self, command_type):
        super(OozieHttpApi, self).__init__()
        
        self.COMMAND_V1 = self.COMMAND_V1 + command_type
        self.COMMAND_V2 = self.COMMAND_V2 + command_type

            
class Admin(OozieHttpApi):
    
    def __init__(self):
        super(Admin, self).__init__('admin')
