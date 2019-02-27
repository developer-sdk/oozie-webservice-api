#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Feb 25, 2019

@author: whitebeard-k
'''
from sdk.HttpRequestApi import HttpRequest


class OozieHttpApi(HttpRequest):

    OOZIE_URL = "http://"
    COMMAND_V1 = "oozie/v1/"
    COMMAND_V2 = "oozie/v2/"

    def __init__(self, oozie_url, command_type):
        super(OozieHttpApi, self).__init__()
        
        self.OOZIE_URL = oozie_url
        self.COMMAND_V1 = self.COMMAND_V1 + command_type
        self.COMMAND_V2 = self.COMMAND_V2 + command_type
    
    def command(self, command_version, sub_command):
        request_command = "{oozie_url}/{command}/{sub_command}".format(oozie_url=self.OOZIE_URL, command=command_version, sub_command=sub_command)
        return request_command

    def command_v1(self, sub_command):
        return self.command(self.COMMAND_V1, sub_command)
    
    def command_v2(self, sub_command):
        return self.command(self.COMMAND_V2, sub_command)

            
class Admin(OozieHttpApi):

    # v1
    SUB_COMMAND_STATUS = "status"
    SUB_COMMAND_BUILD_VERSION = "build-version"
    SUB_COMMAND_AVAILABLE_TIMEZONES = "available-timezones"
    SUB_COMMAND_OS_ENV = "os-env"
    SUB_COMMAND_JAVA_SYS_PROPERTIES = "java-sys-properties"
    SUB_COMMAND_CONFIGURATION = "configuration"
    SUB_COMMAND_INSTRUMENTATION = "instrumentation"
    SUB_COMMAND_QUEUE_DUMP = "queue-dump"
    
    # v2
    SUB_COMMAND_METRICS = "metrics"
    SUB_COMMAND_AVAILABLE_OOZIE_SERVERS = "available-oozie-servers"
    SUB_COMMAND_LIST_SHARELIB = "list_sharelib"
    SUB_COMMAND_UPDATE_SHARELIB = "update_sharelib"
    
    def __init__(self):
        super(Admin, self).__init__('admin')

    def status(self):
        return self.request_get(self.command_v1(self.SUB_COMMAND_STATUS))
        
    def change_system_mode(self, systemmode):
        return self.request_get(self.command_v1(self.SUB_COMMAND_STATUS, {'systemmode':systemmode}))
    
    def os_env(self):
        return self.request_get(self.command_v1(self.SUB_COMMAND_OS_ENV))
    
    def java_sys_properties(self):
        return self.request_get(self.command_v1(self.SUB_COMMAND_JAVA_SYS_PROPERTIES))
        
    def configuration(self):
        return self.request_get(self.command_v1(self.SUB_COMMAND_CONFIGURATION))
    
    def build_version(self):
        return self.request_get(self.command_v1(self.SUB_COMMAND_BUILD_VERSION))
    
    def available_timezones(self):
        return self.request_get(self.command_v1(self.SUB_COMMAND_AVAILABLE_TIMEZONES))
        
    def queue_dump(self):
        return self.request_get(self.command_v1(self.SUB_COMMAND_QUEUE_DUMP))
    
    # v2
    def metrics(self):
        return self.request_get(self.command_v2(self.SUB_COMMAND_METRICS))
    
    def available_oozie_servers(self):
        return self.request_get(self.command_v2(self.SUB_COMMAND_AVAILABLE_OOZIE_SERVERS))
    
    def list_sharelib(self, keywords=None):
        request_url = self.command_v2(self.SUB_COMMAND_LIST_SHARELIB)
        
        if keywords:
            param = { "lib": keywords }
            request_url = "{0}?{1}".format(request_url, self.param_encode(param))
            
        return self.request_get(request_url)
    
    def update_sharelib(self):
        return self.request_get(self.command_v2(self.SUB_COMMAND_UPDATE_SHARELIB))
    
