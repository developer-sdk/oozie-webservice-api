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
        self.version = Versions(oozie_url)
        self.job = Job(oozie_url)
        self.jobs = Jobs(oozie_url)
            
class OozieHttpApi(HttpRequest):
    '''
        Oozie Http Webservice 호출을 위한 슈퍼 클래스  
        command_type: admin, versions, job, jobs
    '''

    _GET_ = "GET"
    _PUT_ = "PUT"
    _OOZIE_URL = "http://"
    
    def __init__(self, oozie_url, end_point):
        super(OozieHttpApi, self).__init__()
        
        self._OOZIE_URL = oozie_url
        
        self._END_POINT = "oozie/" + end_point
        self._V1_END_POINT = "oozie/v1/" + end_point
        self._V2_END_POINT = "oozie/v2/" + end_point
        
    def oozie_request(self, http_request_type, end_point, command=None, params=None, headers={}, data=None):
        
        request_url = self._OOZIE_URL + "/" + end_point
        
        if command:
            request_url = request_url + "/" + command
        
        http_response = self.request(request_url, http_request_type, params, headers, data)
        
        return http_response

class Versions(OozieHttpApi):
    
    def __init__(self, oozie_url):
        super(Versions, self).__init__(oozie_url, 'versions')

    def oozie_versions(self):
        return self.oozie_request(self._GET_, self._END_POINT)
        
class Admin(OozieHttpApi):
    '''
        Oozie Webservice의 Admin API 호출 
    '''

    def __init__(self, oozie_url):
        super(Admin, self).__init__(oozie_url, 'admin')
    
    ### private method
    def __get_oozie_v1_request__(self, command):
        return self.oozie_request(self._GET_, self._V1_END_POINT, command)
    
    def __get_oozie_v2_request__(self, command, params=None):
        return self.oozie_request(self._GET_, self._V2_END_POINT, command, params)

    #### v1
    def status(self, system_mode=None):
        
        if not system_mode:
            return self.__get_oozie_v1_request__("status")
        else:
            if system_mode not in ["NORMAL", "NOWEBSERVICE", "SAFEMODE"]:
                raise ValueError("systemmode in NORMAL, NOWEBSERVICE, SAFEMODE")
        
            return self.oozie_request("PUT", self._V1_END_POINT, "status", params={'systemmode':system_mode})
    
    def os_env(self):
        return self.__get_oozie_v1_request__("os-env")
    
    def java_sys_properties(self):
        return self.__get_oozie_v1_request__("java-sys-properties")
        
    def configuration(self):
        return self.__get_oozie_v1_request__("configuration")
    
    def instrumentation(self):
        return self.__get_oozie_v1_request__("instrumentation")
    
    def build_version(self):
        return self.__get_oozie_v1_request__("build-version")
    
    def available_timezones(self):
        return self.__get_oozie_v1_request__("available-timezones")
        
    def queue_dump(self):
        return self.__get_oozie_v1_request__("queue-dump")
    
    #### v2
    def metrics(self):
        return self.__get_oozie_v2_request__("metrics")
    
    def available_oozie_servers(self):
        return self.__get_oozie_v2_request__("available-oozie-servers")
    
    def list_sharelib(self, keywords=None):
        
        if keywords:
            return self.__get_oozie_v2_request__("list_sharelib", params={'lib': keywords})
        else:
            return self.__get_oozie_v2_request__("list_sharelib")
        
    def update_sharelib(self):
        return self.__get_oozie_v2_request__("update_sharelib")
    

class Job(OozieHttpApi):
    '''
        Oozie Webservice의 Job API 호출 
    '''
    
    def __init__(self, oozie_url):
        super(Job, self).__init__(oozie_url, 'job')
    
    ### private method
    def __get_v1_job_request__(self, job_id, show_type, params={}):
        params["show"] = show_type
        return self.oozie_request(self._GET_, self._V1_END_POINT, job_id, params)
    
    def __get_v2_job_request__(self, job_id, show_type, params={}):
        params["show"] = show_type
        return self.oozie_request(self._GET_, self._V2_END_POINT, job_id, params)
    
    ### v1
    def job_info(self, job_id, filters={}):
        return self.__get_v1_job_request__(job_id, 'info', filters)
    
    def job_log(self, job_id, log_type='log', filters={}):
        
        if log_type not in ["log", "errorlog", "auditlog"]:
            raise ValueError("log_type in log, errorlog, auditlog")
            
        if log_type in ['log']:
            return self.__get_v1_job_request__(job_id, log_type, filters)
        
        if log_type in ['errorlog', 'auditlog']:
            return self.__get_v2_job_request__(job_id, log_type, filters)
    
    def job_graph(self, job_id, file_location="./", showkill="true", file_over_write=False):
        
        file_location = file_location + job_id + ".png"
        
        # check file exist
        if os.path.exists(file_location):
            if file_over_write:
                os.remove(file_location)
            else:
                raise Exception("file exist[" + file_location + " ]")
        
        response = self.__get_v1_job_request__(job_id, "graph", {"show_kill": showkill })
        
        if response.isok:
            response_body = response.body
        
            with open(file_location, "wb") as output:
                output.write(response_body) 
                output.close()
                
            return response
        else:
            return response
            
    def job_status(self, job_id):
        return self.__get_v2_job_request__(job_id, 'status', {})
    
    def managing_job(self, job_id, action_type, xml=""):
        
        if action_type not in ['start', 'suspend', 'resume', 'kill', 'dryrun', 'rerun', 'change', 'ignore']:
            raise Exception("Not valid action type.")
        
        params = {"action" : action_type }
        
        headers={}
        if xml:
            headers = {"Content-Type" : "application/xml;charset=UTF-8"}
        
        return self.oozie_request(self._PUT_, self._V1_END_POINT, job_id, params, headers, xml)
    
        
class Jobs(OozieHttpApi):
    
    def __init__(self, oozie_url):
        super(Jobs, self).__init__(oozie_url, 'jobs')
        
    def submit_job(self, xml):
        headers = {"Content-Type" : "application/xml;charset=UTF-8"}
        
        return self.oozie_request("POST", self._V1_END_POINT, headers=headers, data=xml)
    
            
if __name__ == "__main__":
    
    rerun_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <property><name>user.name</name><value>hadoop</value></property>
</configuration>
'''
    
    submit_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<configuration>
  <property>
    <name>runDate</name>
    <value>20190501</value>
  </property>
</configuration>
'''
    
    
    # https://oozie.apache.org/docs/4.2.0/WebServicesAPI.html
    oozie = OozieWebService("http://localhost:11000")
    
    ## Versions - all json return
    #return_obj = oozie.version.oozie_versions()
    
    ## Admin - all json return
    #return_obj = oozie.admin.status()
    #return_obj = oozie.admin.status('NORMAL')
    #return_obj = oozie.admin.os_env()
    #return_obj = oozie.admin.java_sys_properties()
    #return_obj = oozie.admin.configuration()
    #return_obj = oozie.admin.instrumentation()
    #return_obj = oozie.admin.metrics()    # if metric enable
    #return_obj = oozie.admin.build_version()
    #return_obj = oozie.admin.available_timezones()
    #return_obj = oozie.admin.queue_dump()
    #return_obj = oozie.admin.available_oozie_servers()
    #return_obj = oozie.admin.list_sharelib()
    return_obj = oozie.admin.list_sharelib("pig")
    #return_obj = oozie.admin.update_sharelib()
    
    ## Jobs
    #return_obj = oozie.jobs.submit_job(submit_xml)
    
    ## Job
    #co_id = "C-ID"
    #wf_id = "W-ID"
    #return_obj = oozie.job.job_info(wf_id)
    #return_obj = oozie.job.job_info(co_id)
    #return_obj = oozie.job.job_log(wf_id)  # txt return
    #return_obj = oozie.job.job_log(wf_id, "errorlog")  # txt return
    #return_obj = oozie.job.job_log(wf_id, "auditlog")  # txt return
    #return_obj = oozie.job.job_status(wf_id)
    #return_obj = oozie.job.job_graph(wf_id, file_over_write=True)
    #return_obj = oozie.job.managing_job(wf_id, 'start')              # start ok
    #return_obj = oozie.job.managing_job(wf_id, 'rerun', rerun_xml)    # rerun ok
    
    if return_obj.isok:
        if "Content-Type" in return_obj.headers and "application/json" in return_obj.headers["Content-Type"]:
            json_obj = json.loads(return_obj.body)
            print(json.dumps(json_obj, indent=4, sort_keys=True))
        else:
            print(return_obj.info.url)
            print(return_obj.body)
    else:
        print(return_obj.info.filename)
        print(return_obj.info.headers['oozie-error-code'])
        print(return_obj.info.headers['oozie-error-message'])
        print(return_obj.body)