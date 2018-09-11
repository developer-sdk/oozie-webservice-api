
#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2018. 9. 10.

The Oozie Web Services API Wrapper is a HTTP REST JSON API.
All responses are in UTF-8 .

https://oozie.apache.org/docs/4.2.0/WebServicesAPI.html

@author: whitebeard-k
'''
from sdk.oozie.ws import common
from sdk.oozie.ws.api import versions
from sdk.oozie.ws.api import admin
from sdk.oozie.ws.common import check_param_values

class OozieWebservice(object):
    '''
    classdocs
    '''
    
    _OOZIE_SYSTEM_MODE_ = ["NORMAL", "NOWEBSERVICE", "SAFEMODE"]

    def __init__(self, oozie_ip, oozie_port):
        '''
          ooize_ip: oozie server ip
          oozie_port: oozie server port
        '''
        
        common.OOZIE_URL = "http://{0}:{1}".format(oozie_ip, oozie_port)
    
    def versions(self):
        ''' 
            This endpoint is for clients to perform protocol negotiation.
            It support only HTTP GET request and not sub-resources.
            It returns the supported Oozie protocol versions by the server.
        '''
        return versions.oozie_versions()
    
    def status(self):
        ''' A HTTP GET request returns the system status. '''
        return admin.status()

    @check_param_values(1, _OOZIE_SYSTEM_MODE_)
    def change_system_mode(self, system_mode):
        ''' change the system status between NORMAL , NOWEBSERVICE , and SAFEMODE . '''
        return admin.change_system_mode(system_mode)
    
    def os_env(self):
        ''' the Oozie system OS environment. '''
        return admin.os_env()
    
    def java_sys_properties(self):
        '''  the Oozie Java system properties. '''
        return admin.java_sys_properties()
    
    def configuration(self):
        '''  the Oozie system configuration. '''
        return admin.configuration()
    
    def metrics(self):
        ''' 
           A HTTP GET request returns the Oozie metrics information. 
           Keep in mind that timers and counters that the Oozie server hasn't incremented yet will not show up.
        '''
        return admin.metrics()