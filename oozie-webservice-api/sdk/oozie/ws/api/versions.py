#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sdk.oozie.ws import common
'''
Created on 2018. 9. 3.

@author: whitebeard-k
'''

def oozie_versions():
    request_url = "{oozie_url}/{command}".format(oozie_url = common.OOZIE_URL, command = "oozie/versions")
    common.send_url(request_url)