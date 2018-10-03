#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sdk.oozie.ws import httplib
'''
Admin End-Point

This endpoint is for obtaining Oozie system status and configuration information.
It supports the following sub-resources: status, os-env, sys-props, configuration, instrumentation, systems, available-timezones .

Created on 2018. 9. 3.

@author: whitebeard-k
'''

COMMAND_V1 = "oozie/v1/admin"
COMMAND_V2 = "oozie/v2/admin"

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

# v1
def command(sub_command, command_type = COMMAND_V1):
    request_url = "{oozie_url}/{command}/{sub_command}".format(oozie_url = httplib.OOZIE_URL, command = command_type, sub_command = sub_command)
    return request_url

def status():
    request_url = command(SUB_COMMAND_STATUS)
    return httplib.request_get(request_url)
    
def change_system_mode(mode):
    request_url = command(SUB_COMMAND_STATUS)
    request_url = "{url}?systemmode={systemmode}".format(url = request_url, systemmode = mode)
    return httplib.request_put(request_url)

def os_env():
    request_url = command(SUB_COMMAND_OS_ENV)
    return httplib.request_get(request_url)

def java_sys_properties():
    request_url = command(SUB_COMMAND_JAVA_SYS_PROPERTIES)
    return httplib.request_get(request_url)

def configuration():
    request_url = command(SUB_COMMAND_CONFIGURATION)
    return httplib.request_get(request_url)

def build_version():
    request_url = command(SUB_COMMAND_BUILD_VERSION)
    return httplib.request_get(request_url)

def available_timezones():
    request_url = command(SUB_COMMAND_AVAILABLE_TIMEZONES)
    return httplib.request_get(request_url)

def queue_dump():
    request_url = command(SUB_COMMAND_QUEUE_DUMP)
    return httplib.request_get(request_url)


# v2
def metrics():
    request_url = command(SUB_COMMAND_METRICS, COMMAND_V2)
    return httplib.request_get(request_url)

def available_oozie_servers():
    request_url = command(SUB_COMMAND_AVAILABLE_OOZIE_SERVERS, COMMAND_V2)
    return httplib.request_get(request_url)

def list_sharelib(keywords=""):
    request_url = command(SUB_COMMAND_LIST_SHARELIB, COMMAND_V2)
    
    if keywords:
        param = { "lib": keywords }
        request_url = "{0}?{1}".format(request_url, httplib.param_encode(param))
        
    return httplib.request_get(request_url)

def update_sharelib():
    request_url = command(SUB_COMMAND_UPDATE_SHARELIB, COMMAND_V2)
    return httplib.request_get(request_url)