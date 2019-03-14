#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Feb 25, 2019

@author: whitebeard-k
'''
from sdk.HttpRequestApi import HttpRequest
from _ctypes import ArgumentError

class OozieWebService(object):
    '''
        Oozie 웹서비스 호출 클래스 
    '''
    
    def __init__(self, oozie_url):
        self._OOZIE_URL = oozie_url
        
        self.admin = Admin(oozie_url)
        self.version = Version(oozie_url)
        self.job = Job(oozie_url)
        self.jobs = Jobs(oozie_url)

class OozieHttpApi(HttpRequest):
    '''
        Oozie Http Webservice 호출을 위한 슈퍼 클래스 
        
        command_type: admin, versions, job, jobs
    '''

    _OOZIE_URL = "http://"
    _COMMAND_V1 = "oozie/v1/"
    _COMMAND_V2 = "oozie/v2/"

    def __init__(self, oozie_url, command_type):
        super(OozieHttpApi, self).__init__()
        
        self._OOZIE_URL = oozie_url
        self._COMMAND_V1 = self._COMMAND_V1 + command_type
        self._COMMAND_V2 = self._COMMAND_V2 + command_type
    
    def _mk_command_url(self, version, command, params=None):
        param_string = ''
        
        if params:
            param_string = '?' + self.param_encode(params)
            
        return "{oozie_url}/{version}/{command}{params}".format(oozie_url=self._OOZIE_URL, version=version, command=command, params=param_string) 
        
    # make v1 command string
    def _mk_url(self, version, command, params=None):
        return self._mk_command_url(version, command, params)
    
    # request v1 oozie service
    def get_request_v1(self, command, param=None):
        url = self._mk_url(self._COMMAND_V1, command)
        return self.request_get(url, param)
    
    # request v2 oozie service
    def get_request_v2(self, command, param=None):
        url = self._mk_url(self._COMMAND_V2, command)
        return self.request_get(url, param)
    
    # request v1 oozie service
    def put_request_v1(self, command, param=None):
        url = self._mk_url(self._COMMAND_V1, command)
        return self.request_put(url, param)
    
    # request v2 oozie service
    def put_request_v2(self, command, param=None):
        url = self._mk_url(self._COMMAND_V2, command)
        return self.request_put(url, param)
            
class Admin(OozieHttpApi):
    '''
        Oozie Webservice의 Admin API 호출 
    '''

    # v1
    _SUB_COMMAND_STATUS = "status"
    _SUB_COMMAND_BUILD_VERSION = "build-version"
    _SUB_COMMAND_AVAILABLE_TIMEZONES = "available-timezones"
    _SUB_COMMAND_OS_ENV = "os-env"
    _SUB_COMMAND_JAVA_SYS_PROPERTIES = "java-sys-properties"
    _SUB_COMMAND_CONFIGURATION = "configuration"
    _SUB_COMMAND_INSTRUMENTATION = "instrumentation"
    _SUB_COMMAND_QUEUE_DUMP = "queue-dump"
    
    # v2
    _SUB_COMMAND_METRICS = "metrics"
    _SUB_COMMAND_AVAILABLE_OOZIE_SERVERS = "available-oozie-servers"
    _SUB_COMMAND_LIST_SHARELIB = "list_sharelib"
    _SUB_COMMAND_UPDATE_SHARELIB = "update_sharelib"
    
    def __init__(self, oozie_url):
        super(Admin, self).__init__(oozie_url, 'admin')

    def status(self):
        return self.get_request_v1(self._SUB_COMMAND_STATUS)
        
    def change_system_mode(self, systemmode):
        if systemmode not in ["NORMAL", "NOWEBSERVICE", "SAFEMODE"]:
            raise ArgumentError("systemmode in NORMAL, NOWEBSERVICE, SAFEMODE")
        
        url = self._mk_command_url(self._COMMAND_V1, self._SUB_COMMAND_STATUS, {'systemmode':systemmode})
        
        return self.request_put(url)
    
    def os_env(self):
        return self.get_request_v1(self._SUB_COMMAND_OS_ENV)
    
    def java_sys_properties(self):
        return self.get_request_v1(self._SUB_COMMAND_JAVA_SYS_PROPERTIES)
        
    def configuration(self):
        return self.get_request_v1(self._SUB_COMMAND_CONFIGURATION)
    
    def build_version(self):
        return self.get_request_v1(self._SUB_COMMAND_BUILD_VERSION)
    
    def available_timezones(self):
        return self.get_request_v1(self._SUB_COMMAND_AVAILABLE_TIMEZONES)
        
    def queue_dump(self):
        return self.get_request_v1(self._SUB_COMMAND_QUEUE_DUMP)
    
    # v2
    def metrics(self):
        return self.get_request_v2(self._SUB_COMMAND_METRICS)
    
    def available_oozie_servers(self):
        return self.get_request_v2(self._SUB_COMMAND_AVAILABLE_OOZIE_SERVERS)
    
    def list_sharelib(self, keywords=None):
        params = None
        
        if keywords:
            params = {'lib': keywords}
            
        return self.get_request_v2(self._SUB_COMMAND_LIST_SHARELIB, params)
        
    def update_sharelib(self):
        return self.get_request_v2(self._SUB_COMMAND_UPDATE_SHARELIB)
    
class Version(OozieHttpApi):
    
    _SUB_COMMAND_VERSION = "oozie/versions"
    
    def __init__(self, oozie_url):
        super(Version, self).__init__(oozie_url, 'version')

    def oozie_versions(self):
        return self.get_request_v1(self._SUB_COMMAND_VERSION)
    
class Job(OozieHttpApi):
    # v1
    _SUB_COMMAND_STATUS = "status"
    
    def __init__(self, oozie_url):
        super(Job, self).__init__(oozie_url, 'job')
        
        self._COMMAND_V1 = "oozie/v1/job"
        self._COMMAND_V2 = "oozie/v2/job"
        

    def _request_url_(self, job_id, command_type):
        request_url = "{oozie_url}/{command}/{job_id}".format(oozie_url=self._OOZIE_URL, command=command_type, job_id=job_id)
        return request_url
    
    def _job_show(self, version, job_id, show, params):
        
        url = "{oozie_url}/{version}/{job_id}".format(oozie_url=self._OOZIE_URL, version=version, job_id=job_id)
        params["show"] = show
        
        return self.request_get(url, params)
    
    def job_log(self, job_id, log_type='log', filters={}):
        
        command_version = self._COMMAND_V1
        
        if log_type in ['errorlog', 'auditlog']:
            command_version = self._COMMAND_V2
        
        return self._job_show(command_version, job_id, log_type, filters)

class Jobs(OozieHttpApi):
    
    def __init__(self, oozie_url):
        super(Jobs, self).__init__(oozie_url, 'jobs')
