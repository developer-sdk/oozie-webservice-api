#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2018. 9. 10.

The Oozie Web Services API Wrapper is a HTTP REST JSON API.
All responses are in UTF-8 .

https://oozie.apache.org/docs/4.2.0/WebServicesAPI.html

@author: whitebeard-k
'''
from sdk.oozie.ws import httplib
from sdk.oozie.ws.api import versions
from sdk.oozie.ws.api import admin
from sdk.oozie.ws.api import jobs
from sdk.oozie.ws.api import job
from sdk.oozie.ws.util.decorator import check_param_index_values

class OozieWebservice(object):
    '''
    classdocs
    '''
    
    _OOZIE_SYSTEM_MODE_ = ["NORMAL", "NOWEBSERVICE", "SAFEMODE"]
    _PROXY_JOB_TYPE_ = ["mapreduce", "pig", "hive", "sqoop"]
    _MANAGING_JOB_ACTION_ = [ 'start', 'suspend', 'resume', 'kill', 'dryrun', 'rerun', 'change', 'ignore' ]

    def __init__(self, oozie_ip, oozie_port):
        '''
          ooize_ip: oozie server ip
          oozie_port: oozie server port
        '''
        
        httplib.OOZIE_URL = "http://{0}:{1}".format(oozie_ip, oozie_port)
    
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

    @check_param_index_values(1, _OOZIE_SYSTEM_MODE_)
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
    
    def build_version(self):
        '''  the Oozie build version. '''
        return admin.build_version()
    
    def available_timezones(self):
        ''' returns the available time zones. '''
        return admin.available_timezones()
    
    def queue_dump(self):
        '''  returns the queue dump of the Oozie system. This is an administrator debugging feature. '''
        return admin.queue_dump()
    
    def available_oozie_servers(self):
        '''  returns the list of available Oozie Servers. This is useful when Oozie is configured for High Availability ; if not, it will simply return the one Oozie Server. '''
        return admin.available_oozie_servers()
    
    def list_sharelib(self, keywords=""):
        ''' request to get list of available sharelib. If the name of the sharelib is passed as an argument (regex supported) then all corresponding files are also listed. '''
        return admin.list_sharelib(keywords)
    
    def update_sharelib(self):
        '''
            This webservice call makes the oozie server(s) to pick up the latest version of sharelib present under oozie.service.WorkflowAppService.system.libpath directory 
            based on the sharelib directory timestamp or reloads the sharelib metafile if one is configured. The main purpose is to update the sharelib on the oozie server without restarting.
        '''
        return admin.update_sharelib()
    
    def submit_job(self, xml, start=False):
        '''
            request with an XML configuration as payload creates a job.

            The type of job is determined by the presence of one of the following 3 properties:

                oozie.wf.application.path : path to a workflow application directory, creates a workflow job
                oozie.coord.application.path : path to a coordinator application file, creates a coordinator job
                oozie.bundle.application.path : path to a bundle application file, creates a bundle job
                
            A created job will be in PREP status. If the query string parameter 'action=start' is provided in the POST URL, 
            the job will be started immediately and its status will be RUNNING .
        '''
        return jobs.submit_job(xml, start)
    
    @check_param_index_values(1, _PROXY_JOB_TYPE_)
    def submit_proxy_job(self, jobtype, xml):
        '''
            You can submit a Workflow that contains a single Hive, Pig, MapReduce, Sqoop action without writing a workflow.xml. 
            Any required Jars or other files must already exist in HDFS.
        '''
        return jobs.submit_proxy_job(xml, jobtype)
    
    @check_param_index_values(2, _MANAGING_JOB_ACTION_)    
    def managing_job(self, job_id, action, xml=""):
        ''' 
            request starts, suspends, resumes, kills, update or dryruns a job.
        '''
        return job.managing_job(job_id, action, xml)
    
    def rerunnig_coord_by_action_id(self, coord_id, scope="", refresh=False, nocleanup=False):
        '''
            A coordinator job in RUNNING SUCCEEDED , KILLED or FAILED status can be partially rerun by specifying the coordinator actions to re-execute.
            A rerun request is done with an HTTP PUT request with a coord-rerun action .
            The type of the rerun can be date or action .
            The scope of the rerun depends on the type: * date : a comma-separated list of date ranges. 
                Each date range element is specified with dates separated by :: * action : a comma-separated list of action ranges. 
                Each action range is specified with two action numbers separated by -
            The refresh parameter can be true or false to specify if the user wants to refresh an action's input and output events.
            The nocleanup parameter can be true or false to specify is the user wants to cleanup output events for the rerun actions.
        '''
        return job.rerunning_coordinator(coord_id, "action", scope, "", "", refresh, nocleanup)
    
    def rerunnig_coord_by_date(self, coord_id, start_date_time="", end_date_time="", refresh=False, nocleanup=False):
        '''
            A coordinator job in RUNNING SUCCEEDED , KILLED or FAILED status can be partially rerun by specifying the coordinator actions to re-execute.
            A rerun request is done with an HTTP PUT request with a coord-rerun action .
            The type of the rerun can be date or action .
            The scope of the rerun depends on the type: * date : a comma-separated list of date ranges. 
                Each date range element is specified with dates separated by :: * action : a comma-separated list of action ranges. 
                Each action range is specified with two action numbers separated by -
            The refresh parameter can be true or false to specify if the user wants to refresh an action's input and output events.
            The nocleanup parameter can be true or false to specify is the user wants to cleanup output events for the rerun actions.
        '''
        return job.rerunning_coordinator(coord_id, "date", "", start_date_time, end_date_time, refresh, nocleanup)
    
    def rerunnig_bundle_by_action_name(self, bundle_id, cl_names=[], refresh=False, nocleanup=False):
        '''
            A coordinator job in RUNNING SUCCEEDED , KILLED or FAILED status can be partially rerun by specifying the coordinators to re-execute.
            A rerun request is done with an HTTP PUT request with a bundle-rerun action .
            A comma separated list of coordinator job names (not IDs) can be specified in the coord-scope parameter.
            
            The date-scope parameter is a comma-separated list of date ranges. 
                Each date range element is specified with dates separated by :: . If empty or not included, Oozie will figure this out for you
            The refresh parameter can be true or false to specify if the user wants to refresh the coordinator's input and output events.
            The nocleanup parameter can be true or false to specify is the user wants to cleanup output events for the rerun coordinators.
        '''
        return job.rerunning_bundle(bundle_id, ",".join(cl_names), "", "", refresh, nocleanup)
    
    def rerunnig_bundle_by_date(self, bundle_id, start_date_time="", end_date_time="", refresh=False, nocleanup=False):
        return job.rerunning_bundle(bundle_id,"", start_date_time, end_date_time, refresh, nocleanup)
        
    def change_coord_info(self, coord_id, concurrency="", endtime="", pausetime=""):
        '''
            A coordinator job not in KILLED status can have it's endtime, concurrency, or pausetime changed.
            A change request is done with an HTTP PUT request with a change action .
            The value parameter can contain any of the following: * endtime: the end time of the coordinator job. 
                * concurrency: the concurrency of the coordinator job. * pausetime: the pause time of the coordinator job.
            Multiple arguments can be passed to the value parameter by separating them with a ';' character.
            If an already-succeeded job changes its end time, its status will become running.
        '''
        return job.change_coord_info(coord_id, concurrency, endtime, pausetime)
        
    def update_coordinator(self, coord_id, xml):
        ''' Existing coordinator definition and properties will be replaced by new definition and properties. Refer Updating coordinator definition and properties '''
        return job.update_coordinator(coord_id, xml)
    
    def job_info(self, job_id, **params):
        '''
            request retrieves the job information. wf, coord, bundle information
            params
                show: info, allruns
                offset
                len
                filter
                order
        '''
        return job.job_info(job_id, params)
    
    def job_log(self, job_id, **params):
        
        return job.job_log(job_id, params)
    
    def job_graph(self, job_id, file_location="./", showkill="true"):
        return job.job_graph(job_id, file_location, showkill)
    
    def job_status(self, job_id, **params):
        return job.job_status(job_id, params)
    
    def jobs_information(self, jobtype="", length=1000, offset=1, **filters):
        ''' 
            request retrieves workflow and coordinator jobs information. 
            
            name: the application name from the workflow/coordinator/bundle definition
            user: the user that submitted the job
            group: the group for the job
            status: the status of the job
            startCreatedTime : the start of the window about workflow job's created time
            endCreatedTime : the end of above window

            The query will do an AND among all the filter names.

            The query will do an OR among all the filter values for the same name. 
                Multiple values must be specified as different name value pairs.
            
            Additionally the offset and len parameters can be used for pagination. 
                The start parameter is base 1.
            
            Moreover, the jobtype parameter could be used to determine what type of job is looking for. 
                The valid values of job type are: wf , coordinator or bundle .
        '''
        return jobs.jobs_information(jobtype, length, offset, filters)
    
    def jobs_bulk_modify(self, action, jobtype="", length=50, offset=1, **filters):
        ''' 
            request can kill, suspend, or resume all jobs that satisfy the url encoded parameters.
            
            PUT /oozie/v1/jobs?action=kill&filter=name%3Dcron-coord&offset=1&len=50&jobtype=coordinator

            This request will kill all the coordinators with name=cron-coord up to 50 of them.
            
            Note that the filter is URL encoded, its decoded value is name=cron-coord . The syntax for the filter is
            
            [NAME=VALUE][;NAME=VALUE]*
            
            Valid filter names are:
            
                name: the application name from the workflow/coordinator/bundle definition
                user: the user that submitted the job
                group: the group for the job
                status: the status of the job
            
            The query will do an AND among all the filter names.
            
            The query will do an OR among all the filter values for the same name. 
                Multiple values must be specified as different name value pairs.
            
            Additionally the offset and len parameters can be used for pagination. 
                The start parameter is base 1.
            
            Moreover, the jobtype parameter could be used to determine what type of job is looking for. 
                The valid values of job type are: wf , coordinator or bundle 
        '''
        return jobs.jobs_bulk_modify(action, jobtype, length, offset, filters)
    
    def jobs_bulk_bundle_information(self, bulk_name, coordi_names=[], action_status="", startCreatedTime="", endCreatedTime="", startScheduledTime="", endScheduledTime="", length=50, offset=1):
        '''
            A HTTP GET request retrieves a bulk response for all actions, corresponding to a particular bundle, 
            that satisfy user specified criteria. This is useful for monitoring purposes, where user can find out about the status of downstream jobs with a single bulk request. 
            The criteria are used for filtering the actions returned. Valid options (_case insensitive_) for these request criteria are:
            
                bundle : the application name from the bundle definition
                coordinators : the application name(s) from the coordinator definition.
                actionStatus : the status of coordinator action (Valid values are WAITING, READY, SUBMITTED, RUNNING, SUSPENDED, TIMEDOUT, SUCCEEDED, KILLED, FAILED)
                startCreatedTime : the start of the window you want to look at, of the actions' created time
                endCreatedTime : the end of above window
                startScheduledTime : the start of the window you want to look at, of the actions' scheduled i.e. nominal time.
                endScheduledTime : the end of above window
            
            Specifying 'bundle' is REQUIRED. All the rest are OPTIONAL but that might result in thousands of results depending on the size of your job. (pagination comes into play then)
            
            If no 'actionStatus' values provided, by default KILLED,FAILED will be used. 
                For e.g if the query string is only "bundle=MyBundle", the response will have all actions (across all coordinators) whose status is KILLED or FAILED
            
            The query will do an AND among all the filter names, and OR among each filter name's values.
            
            The syntax for the request criteria is
            
            [NAME=VALUE][;NAME=VALUE]*
            
            For 'coordinators' and 'actionStatus', if user wants to check for multiple values, 
                they can be passed in a comma-separated manner. *Note*: The query will do an OR among them. Hence no need to repeat the criteria name
            
            All the time values should be specified in ISO8601 (UTC) format i.e. yyyy-MM-dd'T'HH:mm'Z'
            
            Additionally the offset and len parameters can be used as usual for pagination. The start parameter is base 1.
            
            If you specify a coordinator in the list, that does not exist, no error is thrown; 
                simply the response will be empty or pertaining to the other valid coordinators. 
            However, if bundle name provided does not exist, an error is thrown.
        '''
        return jobs.jobs_bulk_bundle_information(bulk_name, coordi_names, action_status, startCreatedTime, endCreatedTime, startScheduledTime, endScheduledTime, length, offset)
    
    def managing_job_coordinator(self, job_id, managing_type="", scope=""):
        '''
            A ignore request is done with an HTTP PUT request with a ignore
            
            The type parameter supports action only. 
                The scope parameter can contain coordinator action id(s) to be ignored. 
                Multiple action ids can be passed to the scope parameter
            
            Request:
            
            Ignore a coordinator job
                PUT /oozie/v2/job/job-3?action=ignore
            
            Ignore coordinator actions            
                PUT /oozie/v2/job/job-3?action=ignore&type=action&scope=3-4
        '''
        return job.managing_job_coordinator(job_id, managing_type, scope)