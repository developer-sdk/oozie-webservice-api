
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
from sdk.oozie.ws.api import jobs
from sdk.oozie.ws.api import job
from sdk.oozie.ws.common import check_param_values

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
    
    @check_param_values(1, _PROXY_JOB_TYPE_)
    def submit_proxy_job(self, jobtype, xml):
        '''
            You can submit a Workflow that contains a single Hive, Pig, MapReduce, Sqoop action without writing a workflow.xml. 
            Any required Jars or other files must already exist in HDFS.
        '''
        return jobs.submit_proxy_job(xml, jobtype)
    
    @check_param_values(2, _MANAGING_JOB_ACTION_)    
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
        
    #def job_info(self, job_info):
    #    return job.job_info(job_id)