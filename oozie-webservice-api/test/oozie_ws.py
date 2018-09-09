#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sdk.oozie.ws.api import versions
from sdk.oozie.ws.api import admin
from sdk.oozie.ws.api import job
from sdk.oozie.ws.api import jobs

def main():
    ## version
    #versions.oozie_versions()
    
    ## admin
    #admin.status()
    
    #admin.change_system_mode("NOWEBSERVICE")
    #admin.change_system_mode("SAFEMODE")
    #admin.change_system_mode("NORMAL")
    
    #admin.os_env()
    #admin.java_sys_properties()
    #admin.metrics() --
    #admin.build_version()
    #admin.available_timezones()
    #admin.available_oozie_servers()
    #admin.list_sharelib()
    #admin.list_sharelib("hive*")
    #admin.update_sharelib()
    
    #job.job_info("0006300-180305053637798-oozie-bpse-W")
    #job.job_info("0005928-180305053637798-oozie-bpse-C", filters='status=SKIPPED', length=3, order='desc')
    #job.job_info("0000344-180305053637798-oozie-bpse-C@1")
    #job.job_info("0000344-180305053637798-oozie-bpse-C@1", "allruns")
    #job.job_info("0006300-180305053637798-oozie-bpse-W", "definition")
    #job.job_info("0006300-180305053637798-oozie-bpse-W", "log")
    #job.job_info("0006300-180305053637798-oozie-bpse-W", "errorlog") --
    #job.job_info("0005931-180305053637798-oozie-bpse-C", "auditlog")  --
    #job.job_log("0006300-180305053637798-oozie-bpse-W", logfilter="limit=3;loglevel=WARN")
    #job.job_graph("0006300-180305053637798-oozie-bpse-W", file_location="C:/Users/User/Desktop/", showkill="false")
    #job.job_status("0006300-180305053637798-oozie-bpse-W")
    
    jobs.jobs_information()
    #jobs.jobs_information(1, 1)
    #jobs.jobs_information(10, 1, status="RUNNING")
    #jobs.jobs_bulk_modify("kill", 1, 1, jobtype="coordinator", status="RUNNING")
       

if __name__ == '__main__':
    main()