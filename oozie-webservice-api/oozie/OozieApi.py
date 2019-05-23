#!/usr/bin/env python
# -*- coding: utf-8 -*-
from httputil import HttpRequest
import json, os

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
    
    def oozie_request(self, req_type, command, version=None, params=None, headers={}, data=None):
        
        url_param = {"oozie_url": self._OOZIE_URL, "command": command }
        
        if version:
            url_param["version"] = version
            request_url = "%(oozie_url)s/%(version)s/%(command)s" % url_param
        else:
            request_url = "%(oozie_url)s/%(command)s" % url_param
        
        http_response = self.request(request_url, req_type, params, headers, data)
        
        return self.json_response(http_response)
        
    def json_response(self, response):
        
        if "Content-Type" in response.headers and "application/json" in response.headers["Content-Type"]:
            return json.loads(response.body)
        
        return response
    
class Version(OozieHttpApi):
    
    _SUB_COMMAND_VERSION = "oozie/versions"
    
    def __init__(self, oozie_url):
        super(Version, self).__init__(oozie_url, 'version')

    def oozie_versions(self):
        return self.oozie_request("GET", self._SUB_COMMAND_VERSION)
        
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

    def status(self, system_mode=None):
        
        if not system_mode:
            return self.oozie_request("GET", self._SUB_COMMAND_STATUS, self._COMMAND_V1)
        else:
            if system_mode not in ["NORMAL", "NOWEBSERVICE", "SAFEMODE"]:
                raise ValueError("systemmode in NORMAL, NOWEBSERVICE, SAFEMODE")
        
            return self.oozie_request("PUT", self._SUB_COMMAND_STATUS, self._COMMAND_V1, params={'systemmode':system_mode})
    
    def os_env(self):
        return self.oozie_request("GET", self._SUB_COMMAND_OS_ENV, self._COMMAND_V1)
    
    def java_sys_properties(self):
        return self.oozie_request("GET", self._SUB_COMMAND_JAVA_SYS_PROPERTIES, self._COMMAND_V1)
        
    def configuration(self):
        return self.oozie_request("GET", self._SUB_COMMAND_CONFIGURATION, self._COMMAND_V1)
    
    def build_version(self):
        return self.oozie_request("GET", self._SUB_COMMAND_BUILD_VERSION, self._COMMAND_V1)
    
    def available_timezones(self):
        return self.oozie_request("GET", self._SUB_COMMAND_AVAILABLE_TIMEZONES, self._COMMAND_V1)
        
    def queue_dump(self):
        return self.oozie_request("GET", self._SUB_COMMAND_QUEUE_DUMP, self._COMMAND_V1)
    
    # v2
    def metrics(self):
        return self.oozie_request("GET", self._SUB_COMMAND_METRICS, self._COMMAND_V2)
    
    def available_oozie_servers(self):
        return self.oozie_request("GET", self._SUB_COMMAND_AVAILABLE_OOZIE_SERVERS, self._COMMAND_V2)
    
    def list_sharelib(self, keywords=None):
        params = None
        
        if keywords:
            params = {'lib': keywords}
            
        return self.oozie_request("GET", self._SUB_COMMAND_LIST_SHARELIB, self._COMMAND_V2, params=params)
        
    def update_sharelib(self):
        return self.oozie_request("GET", self._SUB_COMMAND_UPDATE_SHARELIB, self._COMMAND_V2)
    

class Job(OozieHttpApi):
    '''
        Oozie Webservice의 Job API 호출 
    '''
    
    # v1
    _SUB_COMMAND_STATUS = "status"
    
    def __init__(self, oozie_url):
        super(Job, self).__init__(oozie_url, 'job')
    
    def __request_show__(self, version, job_id, show_type, params):
        params["show"] = show_type
        return self.oozie_request("GET", job_id, version, params)
    
    
    def job_log(self, job_id, log_type='log', filters={}):
        
        if log_type not in ["log", "errorlog", "auditlog"]:
            raise ValueError("log_type in log, errorlog, auditlog")
            
        command_version = self._COMMAND_V1
        
        if log_type in ['errorlog', 'auditlog']:
            command_version = self._COMMAND_V2
        
        return self.__request_show__(command_version, job_id, log_type, filters)
    
    def job_info(self, job_id, filters={}):
        return self.__request_show__(self._COMMAND_V1, job_id, 'info', filters)
    
    def job_graph(self, job_id, file_location="./", showkill="true"):
        
        file_location = file_location + job_id + ".png"
        
        # check file exist
        if os.path.exists(file_location):
            raise Exception("file exist[" + file_location + " ]")
        
        response_body = self.__request_show__(self._COMMAND_V1, job_id, "graph", {"show_kill": showkill }).body
        
        with open(file_location, "wb") as output:
            output.write(response_body) 
            output.close()
            
    def job_status(self, job_id):
        return self.__request_show__(self._COMMAND_V2, job_id, 'status', {})
    
    def managing_job(self, job_id, action_type, xml=""):
        
        if action_type not in ['start', 'suspend', 'resume', 'kill', 'dryrun', 'rerun', 'change', 'ignore']:
            raise Exception("Not valid action type.")
        
        params = {}
        params["action"] = action_type
        
        headers={}
        if xml:
            headers["Content-Type"] = "application/xml;charset=UTF-8"
        
        return self.oozie_request("PUT", job_id, self._COMMAND_V1, params, headers=headers, data=xml)
        
class Jobs(OozieHttpApi):
    
    def __init__(self, oozie_url):
        super(Jobs, self).__init__(oozie_url, 'jobs')
    
            
if __name__ == "__main__":
    
    rerun_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<configuration>
<property><name>user.name</name><value>hadoop</value></property>
<property><name>oozie.wf.rerun.failnodes</name><value>false</value></property>
</configuration>
'''
    # https://oozie.apache.org/docs/4.2.0/WebServicesAPI.html#Job_Information
    oozie = OozieWebService("http://localhost:11000")
    
    # Version - all json return
    # return_obj = oozie.version.oozie_versions()
    
    # Admin - all json return
    # return_obj = oozie.admin.status()
    # return_obj = oozie.admin.status('NORMAL')
    #return_obj = oozie.admin.os_env()
    #return_obj = oozie.admin.java_sys_properties()
    #return_obj = oozie.admin.configuration()
    #return_obj = oozie.admin.build_version()
    #return_obj = oozie.admin.available_timezones()
    #return_obj = oozie.admin.queue_dump()
    #return_obj = oozie.admin.metrics()    # if metric enable
    #return_obj = oozie.admin.available_oozie_servers()
    #return_obj = oozie.admin.list_sharelib()
    #return_obj = oozie.admin.list_sharelib("pig")
    #return_obj = oozie.admin.update_sharelib()
    
    # Job
    co_id = "C-ID"
    wf_id = "W-ID"
    #return_obj = oozie.job.job_info(wf_id)
    #return_obj = oozie.job.job_info(co_id)
    #return_obj = oozie.job.job_log(wf_id)  # txt return
    #return_obj = oozie.job.job_log(wf_id, "errorlog")  # txt return
    #return_obj = oozie.job.job_log(wf_id, "auditlog")  # txt return
    #return_obj = oozie.job.job_status(wf_id)
    #return_obj = oozie.job.job_graph(wf_id)
    return_obj = oozie.job.managing_job(wf_id, 'start')
    #return_obj = oozie.job.managing_job(wf_id, 'rerun', rerun_xml)
    
    if isinstance(return_obj, dict):
        print(json.dumps(return_obj, indent=4, sort_keys=True))
    else:
        if return_obj.isok:
            print(return_obj.info.url)
            print(return_obj.body)
        else:
            print(return_obj.info.filename)
            print(return_obj.body)