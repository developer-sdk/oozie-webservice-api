#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sdk.oozie.ws import httplib
'''
Created on 2018. 9. 3.

@author: whitebeard-k
'''

def oozie_versions():
    request_url = "{oozie_url}/{command}".format(oozie_url = httplib.OOZIE_URL, command = "oozie/versions")
    httplib.request_get(request_url)