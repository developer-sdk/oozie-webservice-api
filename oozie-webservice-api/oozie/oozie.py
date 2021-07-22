#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os

if sys.version_info[0] == 3:
    from .httputil3 import HttpRequest
else:
    from .httputil2 import HttpRequest
            
class OozieHttpApi(HttpRequest):
    '''
        Oozie Http Webservice 호출을 위한 슈퍼 클래스  
        command_type: admin, versions, job, jobs
    '''

    _GET_ = "GET"
    _PUT_ = "PUT"
    _POST_ = "POST"
    _OOZIE_URL = "http://"
    
    def __init__(self, oozie_url, end_point):
        super(OozieHttpApi, self).__init__()
        
        self._OOZIE_URL = oozie_url
        
        self._END_POINT = "oozie/" + end_point
        self._V1_END_POINT = "oozie/v1/" + end_point
        self._V2_END_POINT = "oozie/v2/" + end_point
        
        self._XML_HEADERS = {"Content-Type" : "application/xml;charset=UTF-8"} 
        
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
    
    class Filters():
        
        def __init__(self):
            self.offset = 1
            self.len = 30
            self.order = "asc"
            self.status = "SUCCEEDED"
            self.status_except = False
            
        def params(self):
            params = dict()
            params["offset"] = self.offset
            params["len"] = self.len
            params["order"] = self.order
            
            status_filter = "status" + ("=" if not self.status_except else "!=")
            params["filter"] = status_filter + self.status
            
            return params
        
    class LogFilters():
        def __init__(self):
            self.limit = 3
            self.log_level = "WARN"
            
        def params(self):
            filters = "limit={0};".format(self.limit)
            filters += "loglevel={0};".format(self.log_level)
            return { "logfilter" : filters}
            
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
    def job_info(self, job_id, filters=None):
        filters = filters.params() if filters else {}
        return self.__get_v1_job_request__(job_id, 'info', filters)
        
    
    def job_definition(self, job_id, filters=None):
        filters = filters.params() if filters else {}
        return self.__get_v1_job_request__(job_id, 'definition', filters)
    
    def job_log(self, job_id, log_type='log', filters=None):
        filters = filters.params() if filters else {}
        
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
        
        if action_type not in ['start', 'suspend', 'resume', 'kill', 'dryrun', 'change', 'ignore']:
            raise Exception("Not valid action type.")
        
        params = {"action" : action_type }
        headers = {}
        if xml:
            headers = self._XML_HEADERS
        
        return self.oozie_request(self._PUT_, self._V1_END_POINT, job_id, params, headers, xml)
    
    ## rerun
    def rerun_workflow(self, job_id, xml):
        params = {"action" : 'rerun' }
        headers = self._XML_HEADERS
        return self.oozie_request(self._PUT_, self._V1_END_POINT, job_id, params, headers, xml)
    
    ## rerun coord action - action=coord-rerun&type=action&scope=1-2&refresh=false&nocleanup=false 
    def rerun_coordinator_on_action(self, coord_id, scope="", refresh=False, nocleanup=False):
        params = {"action" : 'coord-rerun', "type":"action", "scope":scope }
        return self._rerun_(coord_id, params, refresh, nocleanup)
    
    ## rerun coord date - action=coord-rerun&type=date2009-02-01T00:10Z::2009-03-01T00:10Z&scope=&refresh=false&nocleanup=false 
    def rerun_coordinator_on_date(self, coord_id, start_date_time="", end_date_time="", refresh=False, nocleanup=False):
        params = {"action" : 'coord-rerun', "type":"date", "scope":"{0}::{1}".format(start_date_time, end_date_time) }
        return self._rerun_(coord_id, params, refresh, nocleanup)
    
    # rerun bundloe coord_scope
    def rerun_bundle_coord_scope(self, bundle_id, coord_scope, refresh=False, nocleanup=False):
        params = {"action" : 'bundle-rerun', "coord-scope":coord_scope }
        return self._rerun_(bundle_id, params, refresh, nocleanup)
    
    # rerun bundle date
    def rerun_bundle_on_date(self, bundle_id, start_date_time="", end_date_time="", refresh=False, nocleanup=False):
        params = {"action" : 'bundle-rerun', "date-scope":"{0}::{1}".format(start_date_time, end_date_time) }
        return self._rerun_(bundle_id, params, refresh, nocleanup)
    
    # common coord, bundle rerun 
    def _rerun_(self, cb_id, params, refresh, nocleanup):
        params["refresh"] = "true" if refresh else "false"
        params["nocleanup"] = "true" if nocleanup else "false"
        
        headers = self._XML_HEADERS
        
        return self.oozie_request(self._PUT_, self._V1_END_POINT, cb_id, params, headers)
    
    ### change coord
    def change_coordinator_endtime(self, coord_id, end_time):
        params = {"action" : 'change', "value":"endtime="+end_time }
        return self.oozie_request(self._PUT_, self._V1_END_POINT, coord_id, params)
    
    def change_coordinator_concurrency(self, coord_id, concurrency):
        params = {"action" : 'change', "value":"concurrency={0}".format(concurrency) }
        return self.oozie_request(self._PUT_, self._V1_END_POINT, coord_id, params)
    
    def change_coordinator_pausetime(self, coord_id, pausetime):
        params = {"action" : 'change', "value":"pausetime="+pausetime }
        return self.oozie_request(self._PUT_, self._V1_END_POINT, coord_id, params)
    
    ### update coord
    def update_coordinator(self, coord_id, xml):
        params = {"action" : 'update' }
        headers = self._XML_HEADERS
        return self.oozie_request(self._PUT_, self._V2_END_POINT, coord_id, params, headers, xml)
        
    ### v2
    def coordinator_allruns(self, coord_id, action_number, filters={}):
        filters = filters.params() if filters else {}
        action_id = coord_id + "@" + action_number
        return self.__get_v2_job_request__(action_id, 'allruns', filters)        
        
class Jobs(OozieHttpApi):
    
    class Filters():
        def __init__(self):
            self.offset = 1
            self.len = 2
            self.order = "asc"
            
            self.name = None
            self.user = None
            self.group = None
            self.status = None
            self.startCreatedTime = None
            self.endCreatedTime = None
            
        def params(self):
            params = dict()
            params["offset"] = self.offset
            params["len"] = self.len
            params["order"] = self.order
            
            filters = ""
            filters += "name={0};".format(self.name) if self.name else ""
            filters += "user={0};".format(self.user) if self.user else ""
            filters += "group={0};".format(self.group) if self.group else ""
            filters += "status={0};".format(self.status) if self.status else ""
            filters += "startCreatedTime={0};".format(self.startCreatedTime) if self.startCreatedTime else ""
            filters += "endCreatedTime={0};".format(self.endCreatedTime) if self.endCreatedTime else ""
        
            params["filter"] = filters
            
            return params
        
        
    def __init__(self, oozie_url):
        super(Jobs, self).__init__(oozie_url, 'jobs')
        
    def submit_job(self, xml, job_type=None):
        
        if job_type in ["mapreduce", "pig", "hive", "sqoop"]:
            params = {"jobtype" : job_type }
            return self.oozie_request(self._POST_, self._V1_END_POINT, headers=self._XML_HEADERS, params=params, data=xml)
        elif job_type is None:
            return self.oozie_request(self._POST_, self._V1_END_POINT, headers=self._XML_HEADERS, data=xml)
        else:
            raise ValueError("job_type in none, mapreduce, pig, hive, sqoop")
        
    def info(self, job_type=None, filters=None):
        if job_type not in ["wf", "coordinator", "bundle"]:
            raise ValueError("job_type in wf, coordinator, bundle")
        
        filters = filters.params() if filters else {}
        filters["jobtype"] = job_type
        
        return self.oozie_request(self._GET_, self._V1_END_POINT, params=filters)
    
    def managing_jobs(self, action, job_type, filters=None):
        if job_type not in ["wf", "coordinator", "bundle"]:
            raise ValueError("job_type in wf, coordinator, bundle")
            
        filters = filters.params() if filters else {}
        filters["action"] = action
        filters["jobtype"] = job_type
        return self.oozie_request(self._PUT_, self._V1_END_POINT, params=filters)
