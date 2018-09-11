
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sdk.oozie.ws import common

'''
Created on 2018. 9. 5.

@author: whitebeard-k
'''

COMMAND_V1 = "oozie/v1/jobs"

# v1
def command(command_type):
    request_url = "{oozie_url}/{command}".format(oozie_url = common.OOZIE_URL, command = command_type)
    return request_url

def _jobs_(command_type=COMMAND_V1):
    request_url = command(command_type)
    return common.request_get(request_url)

def jobs_information(length=50, offset=1, **filters):
    '''
    name: the application name from the workflow/coordinator/bundle definition
    user: the user that submitted the job
    group: the group for the job
    status: the status of the job
    startCreatedTime : the start of the window about workflow job's created time
    endCreatedTime : the end of above window

    '''
    request_url = command(COMMAND_V1)
    len_offset_str = "len={0}&offset={1}".format(length, offset)
    fliters_str = "filter="
    
    if filters:
        fliters_str = "{0}{1}".format(fliters_str, common.param_encode(filters))
    
    request_url = "{0}?{1}&{2}".format(request_url, len_offset_str, fliters_str)
    
    return common.request_get(request_url)

def jobs_bulk_modify(action, length=50, offset=1, **filters):
    '''
    filters
    '''
    request_url = command(COMMAND_V1)
    
    action_str = "action={0}".format(action)
    len_offset_str = "len={0}&offset={1}".format(length, offset)
    fliters_str = "filter="
    
    if filters:
        fliters_str = "{0}{1}".format(fliters_str, common.param_encode(filters))
    
    request_url = "{0}?{1}&{2}&{3}".format(request_url, action_str, len_offset_str, fliters_str)
    
    return common.request_put(request_url)
    
def jobs_bulk_bundle_information():
    pass