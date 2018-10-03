#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sdk.oozie.ws import httplib
from sdk.oozie.ws.util.decorator import check_param_name_values
'''
Created on 2018. 9. 5.

@author: whitebeard-k
'''

COMMAND_V1 = "oozie/v1/jobs"

_JOB_TYPES_ = [ "wf", "coordinator", "bundle" ]

# v1
def command(command_type):
    request_url = "{oozie_url}/{command}".format(oozie_url = httplib.OOZIE_URL, command = command_type)
    return request_url

def _jobs_(command_type=COMMAND_V1):
    request_url = command(command_type)
    return httplib.request_get(request_url)

@check_param_name_values("jobtype", _JOB_TYPES_)
def jobs_information(jobtype="", length=50, offset=1, filters={}):
    '''
    name: the application name from the workflow/coordinator/bundle definition
    user: the user that submitted the job
    group: the group for the job
    status: the status of the job
    startCreatedTime : the start of the window about workflow job's created time
    endCreatedTime : the end of above window

    '''
    request_url = command(COMMAND_V1)
    len_offset_str = "len={0}&offset={1}&jobtype={2}".format(length, offset, jobtype)
    fliters_str = "filter="
    
    if filters:
        fliters_str = "{0}{1}".format(fliters_str, httplib.param_encode(filters))
    
    request_url = "{0}?{1}&{2}".format(request_url, len_offset_str, fliters_str)
    
    return httplib.request_get(request_url)

@check_param_name_values("jobtype", _JOB_TYPES_)
def jobs_bulk_modify(action, jobtype="", length=50, offset=1, filters={}):
    request_url = command(COMMAND_V1)
    
    action_str = "action={0}".format(action)
    len_offset_str = "len={0}&offset={1}&jobtype={2}".format(length, offset, jobtype)
    fliters_str = "filter="
    
    if filters:
        fliters_str = "{0}{1}".format(fliters_str, httplib.param_encode(filters))
    
    request_url = "{0}?{1}&{2}&{3}".format(request_url, action_str, len_offset_str, fliters_str)
    
    return httplib.request_put(request_url)
    
def jobs_bulk_bundle_information(bulk_name, coordi_names=[], action_status="", startCreatedTime="", endCreatedTime="", startScheduledTime="", endScheduledTime="", length=50, offset=1):
    request_url = command(COMMAND_V1)
    
    bulk_str = "bulk=bundle={0}".format(bulk_name)
        
    if coordi_names:
        bulk_str = "{0};coordinators={1}".format(bulk_str, ",".join(coordi_names))
        
    if action_status:
        bulk_str = "{0};actionStatus={1}".format(bulk_str, action_status)
    
    if startCreatedTime:
        bulk_str = "{0};startCreatedTime={1}".format(bulk_str, startCreatedTime)
        
    if endCreatedTime:
        bulk_str = "{0};endCreatedTime={1}".format(bulk_str, endCreatedTime)
        
    if startScheduledTime:
        bulk_str = "{0};startScheduledTime={1}".format(bulk_str, startScheduledTime)
        
    if endScheduledTime:
        bulk_str = "{0};endScheduledTime={1}".format(bulk_str, endScheduledTime)
    
    len_offset_str = "len={0}&offset={1}".format(length, offset)
    
    request_url = "{0}?{1}&{2}".format(request_url, bulk_str, len_offset_str)
    
    return httplib.request_get(request_url)
    
def submit_job(xml, start=False):
    request_url = command(COMMAND_V1)
    
    if start:
        request_url = request_url + "?action=start"
    
    return httplib.request_post(request_url, xml)
    
def submit_proxy_job(xml, job_type):
    request_url = command(COMMAND_V1)
    request_url = "{0}?jobtype={1}".format(request_url, job_type)
    
    return httplib.request_post(request_url, xml)