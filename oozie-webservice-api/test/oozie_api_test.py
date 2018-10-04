#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sdk.oozie.ws.OozieWebservice import OozieWebservice

jobxml = '''<?xml version="1.0" encoding="UTF-8"?>
<configuration>
<property><name>nominalTime</name><value>00</value></property>
</configuration>
'''

proxyxml = '''<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <property>
        <name>oozie.hive.script</name>
        <value>
            show databases
        </value>
    </property>
</configuration>
'''

rerun_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<configuration>
<property><name>user.name</name><value>hadoop</value></property>
</configuration>
'''

update_coord_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<configuration>
<property><name>type</name><value>CL</value></property>
</configuration>'''

def main():
    
    oozie = OozieWebservice("localhost", 11000)
    
    ## version
    #oozie.versions()
    
    ## admin
    #oozie.status()
    
    #oozie.change_system_mode("NOWEBSERVICE")
    #oozie.change_system_mode("SAFEMODE")
    #oozie.change_system_mode("NORMAL")
    
    #oozie.os_env()
    #oozie.java_sys_properties()
    #oozie.configuration()
    #oozie.metrics() 
    #oozie.build_version()
    #oozie.available_timezones()
    #oozie.queue_dump()
    #oozie.available_oozie_servers()
    #oozie.list_sharelib()
    #oozie.list_sharelib("hive*")
    #oozie.update_sharelib()
    
    #oozie.submit_job(jobxml)
    #oozie.submit_job(jobxml, True)
    #oozie.submit_proxy_job('hive', proxyxml)
    
    #oozie.managing_job("0006357-180305053637798-oozie-bpse-W", "kill")
    #oozie.managing_job("0006351-180305053637798-oozie-bpse-W", "rerun", rerun_xml)
    #oozie.rerunnig_coord_by_action_id("0005928-180305053637798-oozie-bpse-C", "23-24")
    #oozie.rerunnig_coord_by_date("0005928-180305053637798-oozie-bpse-C", "2018-08-19T21:00Z", "2018-08-19T23:00Z")
    
    #oozie.rerunnig_bundle_by_action_name("0006373-180305053637798-oozie-bpse-B", ["CL_1"])
    #oozie.rerunnig_bundle_by_date("0006373-180305053637798-oozie-bpse-B", "2018-09-12T01:00Z", "2018-09-12T02:00Z")
    
    #oozie.change_coord_info("0005931-180305053637798-oozie-bpse-C", pausetime="2030-09-12T02:00Z")
    #oozie.update_coordinator("0006384-180305053637798-oozie-bpse-C", update_coord_xml)
    
    oozie.job_info("0006300-180305053637798-oozie-bpse-W")
    #oozie.job_info("0006420-180305053637798-oozie-bpse-C", show="definition")
    #oozie.job_info("0000344-180305053637798-oozie-bpse-C@1")
    #oozie.job_info("0000344-180305053637798-oozie-bpse-C@1", show="allruns", type="action")
    #oozie.job_info("0005928-180305053637798-oozie-bpse-C", filters='status=SKIPPED', offset=1, len=1, order='desc')
    #oozie.job_info("0006300-180305053637798-oozie-bpse-W", show="definition")
    #oozie.job_info("0006300-180305053637798-oozie-bpse-W", "log")
    #oozie.job_info("0006300-180305053637798-oozie-bpse-W", "errorlog") --
    #oozie.job_info("0005931-180305053637798-oozie-bpse-C", "auditlog")  --
    #oozie.job_log("0006300-180305053637798-oozie-bpse-W")
    #oozie.job_log("0006300-180305053637798-oozie-bpse-W", show="errorlog")
    #oozie.job_log("0005928-180305053637798-oozie-bpse-C", show="auditlog")
    #oozie.job_log("0006300-180305053637798-oozie-bpse-W", logfilter="limit=3;loglevel=WARN")
    #oozie.job_graph("0006300-180305053637798-oozie-bpse-W", file_location="C:/Users/User/Desktop/", showkill="false")
    #oozie.job_status("0006394-180305053637798-oozie-bpse-C")
    
    
    #oozie.jobs_information()
    #oozie.jobs_information(1, 1)
    #oozie.jobs_information(10, 1, status="RUNNING")
    #oozie.jobs_information("coordinator", 10, 1)
    #oozie.jobs_information("wf", 10, 1)
    #oozie.jobs_bulk_modify("kill", "wf", 1, 1, status="RUNNING")
    #oozie.jobs_bulk_bundle_information("BUNDLE_TEST")
    #oozie.jobs_bulk_bundle_information("BUNDLE_TEST", coordi_names=["CL_1", "CL_2"], action_status="RUNNING")
    #oozie.jobs_bulk_bundle_information("BUNDLE_TEST", coordi_names=["CL_1", "CL_2"], endScheduledTime="2018-09-13T07:00Z")
    
    #oozie.managing_job_coordinator("0005931-180305053637798-oozie-bpse-C")
    #oozie.managing_job_coordinator("0005931-180305053637798-oozie-bpse-C", managing_type="action", scope="4")
       

if __name__ == '__main__':
    main()