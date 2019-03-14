#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sdk import OozieApi

ows = OozieApi.OozieWebService("http://127.0.0.1:11000")

#########################
# admin
#########################
# v1
#ows.admin.build_version()
#ows.admin.status()
#ows.admin.change_system_mode('NORMAL')
#ows.admin.os_env()
#ows.admin.java_sys_properties()
#ows.admin.configuration()
#ows.admin.build_version()
#ows.admin.available_timezones()
#ows.admin.queue_dump()

#v2
#ows.admin.metrics()
#ows.admin.available_oozie_servers()
#ows.admin.list_sharelib()
#ows.admin.list_sharelib('pig')
#ows.admin.update_sharelib()


#########################
# version
#########################
#ows.version.oozie_versions()

#########################
# job
#########################
#ows.job.job_log("OOZIE-Workflow-ID")
#ows.job.job_log("OOZIE-Workflow-ID", log_type='errorlog')
ows.job.job_log("OOZIE-Workflow-ID", log_type='auditlog')