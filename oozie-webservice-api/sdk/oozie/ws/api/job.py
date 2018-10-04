#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sdk.oozie.ws import httplib
'''
Created on 2018. 9. 4.

@author: whitebeard-k
'''

COMMAND_V1 = "oozie/v1/job"
COMMAND_V2 = "oozie/v2/job"

# v1
SUB_COMMAND_STATUS = "status"

# v1
def command(job_id, command_type):
    request_url = "{oozie_url}/{command}/{job_id}".format(oozie_url = httplib.OOZIE_URL, command = command_type, job_id = job_id)
    return request_url

def _job_show_(job_id, show, params, command_type=COMMAND_V1):
    request_url = command(job_id, command_type)
    
    params["show"] = show
    request_url = "{0}?{1}".format(request_url, httplib.param_encode(params))
    
    return httplib.request_get(request_url)

def job_log(job_id, params):
    return _job_show_(job_id, params["show"] if "show" in params else "log", params, command_type=COMMAND_V2)

def job_info(job_id, params={}):
    return _job_show_(job_id, params["show"] if "show" in params else "info", params)




def job_graph(job_id, file_location="./", showkill="true"):
    response_body = _job_show_(job_id, "graph", { "show_kill": showkill })
    file_location = file_location + job_id + ".png"
    
    with open(file_location,"wb") as output:
            output.write(response_body) 
            output.close()

# v2
def job_status(job_id, params):
    return _job_show_(job_id, "status", params, COMMAND_V2)

def managing_job(job_id, action, xml=""):
    request_url = command(job_id, COMMAND_V1)
    request_url = "{0}?action={1}".format(request_url, action)
    
    return httplib.request_put(request_url, xml)

def rerunning_coordinator(coord_id, rerun_type, scope="", start_date_time="", end_date_time="", refresh=False, nocleanup=False):
    '''
        action=coord-rerun&type=action&scope=1-2&refresh=false&nocleanup=false
        action=coord-rerun&type=date2009-02-01T00:10Z::2009-03-01T00:10Z&scope=&refresh=false&nocleanup=false
    '''
    request_url = command(coord_id, COMMAND_V1)
    
    params = dict()
    params["action"] = "coord-rerun"
    
    if rerun_type == "action":
        params["type"] = "action"
        params["scope"] = scope
    elif rerun_type == "date":
        params["type"] = "date"
        params["scope"] = "{0}::{1}".format(start_date_time, end_date_time)
        
    params["refresh"] = "true" if refresh else "false"
    params["nocleanup"] = "true" if refresh else "false"
    
    request_url = "{0}?{1}".format(request_url, httplib.param_encode(params))
    
    return httplib.request_put(request_url)

def rerunning_bundle(bundle_id, coord_names="", start_date_time="", end_date_time="", refresh=False, nocleanup=False):
    ''' /oozie/v1/job/job-3?action=bundle-rerun&coord-scope=coord-1&refresh=false&nocleanup=false '''
    request_url = command(bundle_id, COMMAND_V1)
    
    params = dict()
    params["action"] = "bundle-rerun"
    
    if coord_names:
        params["coord-scope"] = coord_names
    elif start_date_time and end_date_time:
        params["date-scope"] = "{0}::{1}".format(start_date_time, end_date_time)
        
    params["refresh"] = "true" if refresh else "false"
    params["nocleanup"] = "true" if refresh else "false"
    
    request_url = "{0}?{1}".format(request_url, httplib.param_encode(params))
    
    return httplib.request_put(request_url)

def managing_job_coordinator(job_id, managing_type="", scope=""):
    request_url = command(job_id, COMMAND_V2)
    
    params = dict()
    params["action"] = 'ignore'
    
    if managing_type:
        params["type"] = managing_type
        
    if scope:
        params["scope"] = scope
        
    request_url = "{0}?{1}".format(request_url, httplib.param_encode(params))
    
    return httplib.request_put(request_url)

def change_coord_info(coord_id, concurrency="", endtime="", pausetime=""):
    '''
        /oozie/v1/job/job-3?action=change&value=concurrency=100
        /oozie/v1/job/job-3?action=change&value=endtime=2011-12-01T05:00Z;concurrency=100;pausetime=2011-12-01T05:00Z        
    '''
    request_url = command(coord_id, COMMAND_V1)
    
    values = ""
    
    if concurrency <> "":
        values = values + "concurrency={0}".format(concurrency)
    
    if endtime:
        if values:
            values = values + ";"
            
        values =  values + "endtime={0}".format(endtime)
    
    if pausetime:
        if values:
            values = values + ";"
    
        values =  values + "pausetime={0}".format(pausetime)
    
    request_url = "{0}?action=change&value={1}".format(request_url, values)
    
    return httplib.request_put(request_url)

def update_coordinator(coord_id, xml):
    ''' oozie/v2/job/0000000-140414102048137-oozie-puru-C?action=update '''
    request_url = command(coord_id, COMMAND_V2)
    request_url = "{0}?action=update".format(request_url)
    
    return httplib.request_put(request_url, xml=xml)

def change_sla(job_id):
    pass