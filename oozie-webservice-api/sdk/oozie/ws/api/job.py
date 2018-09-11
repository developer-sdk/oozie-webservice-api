
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sdk.oozie.ws import common
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
    request_url = "{oozie_url}/{command}/{job_id}".format(oozie_url = common.OOZIE_URL, command = command_type, job_id = job_id)
    return request_url

def _job_show_(job_id, show, params, command_type=COMMAND_V1):
    request_url = command(job_id, command_type)
    
    params["show"] = show
    request_url = "{0}?{1}".format(request_url, common.param_encode(params))
    
    return common.request_get(request_url)

def job_log(job_id, **params):
    return _job_show_(job_id, "log", params)

def job_info(job_id, **params):
    return _job_show_(job_id, "info", params)

def job_graph(job_id, file_location="./", showkill="true"):
    response_body = _job_show_(job_id, "graph", { "show_kill": showkill })
    file_location = file_location + job_id + ".png"
    
    with open(file_location,"wb") as output:
            output.write(response_body) 
            output.close()

# v2
def job_status(job_id, **params):
    return _job_show_(job_id, "status", params, COMMAND_V2)

def managing_job(job_id, action="ignore", managing_type="", scope=""):
    request_url = command(job_id, COMMAND_V2)
    
    params = dict()
    params["action"] = action
    
    if managing_type:
        params["type"] = managing_type
        
    if scope:
        params["scope"] = scope
        
    request_url = "{0}?{1}".format(request_url, common.param_encode(params))
    
    return common.request_put(request_url)