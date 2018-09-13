
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sdk.oozie.ws.OozieWebservice import OozieWebservice

jobxml = '''<?xml version="1.0" encoding="UTF-8"?>
<configuration>
<property><name>user.name</name><value>hadoop</value></property>
<property><name>oozie.wf.application.path</name><value>hdfs:///user/hadoop/MR/CL/</value></property>
<property><name>nominalDate</name><value>20180901</value></property>
<property><name>nominalTime</name><value>00</value></property>
</configuration>
'''

proxyxml = '''<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <property>
        <name>fs.default.name</name>
        <value>hdfs://localhost:8020</value>
    </property>
    <property>
        <name>mapred.job.tracker</name>
        <value>localhost:8032</value>
    </property>
    <property>
        <name>user.name</name>
        <value>hadoop</value>
    </property>
    <property>
        <name>mapred.job.queue.name</name>
        <value>q2</value>
    </property>
    <property>
        <name>oozie.hive.script</name>
        <value>
            show databases
        </value>
    </property>
    <property>
        <name>oozie.libpath</name>
        <value>hdfs://localhost:8020/user/hadoop/share/lib</value>
    </property>
    <property>
        <name>oozie.proxysubmission</name>
        <value>true</value>
    </property>
</configuration>
'''

rerun_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<configuration>
<property><name>user.name</name><value>hadoop</value></property>
    <property>
        <name>oozie.wf.application.path</name>
        <value>hdfs://localhost:8020/user/hadoop/MR/CL_MR/kr</value>
    </property>
    <property>
        <name>oozie.wf.rerun.skip.nodes</name>
        <value>PM_ODW_CL</value>
    </property>
</configuration>
'''

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
    
    #oozie.managing_job("0006357-SAMPLE-oozie-bpse-W", "kill")
    #oozie.managing_job("0006351-SAMPLE-oozie-bpse-W", "rerun", rerun_xml)
    #oozie.rerunnig_coord_by_action_id("0005928-SAMPLE-oozie-bpse-C", "23-24")
    oozie.rerunnig_coord_by_date("0005928-SAMPLE-oozie-bpse-C", "2018-08-19T21:00Z", "2018-08-19T23:00Z")
        
    #oozie.rerunnig_bundle_by_action_name("0006373-180305053637798-oozie-bpse-B", ["CL_1"])
    #oozie.rerunnig_bundle_by_date("0006373-180305053637798-oozie-bpse-B", "2018-09-12T01:00Z", "2018-09-12T02:00Z")
    
    #oozie.change_coord_info("0005931-180305053637798-oozie-bpse-C", pausetime="2030-09-12T02:00Z")
    
    #oozie.job_info("0006300-SAMPLE-oozie-bpse-W")
    #job.job_info("0005928-SAMPLE-oozie-bpse-C", filters='status=SKIPPED', length=3, order='desc')
    #job.job_info("0000344-SAMPLE-oozie-bpse-C@1")
    #job.job_info("0000344-SAMPLE-oozie-bpse-C@1", "allruns")
    #job.job_info("0006300-SAMPLE-oozie-bpse-W", "definition")
    #job.job_info("0006300-SAMPLE-oozie-bpse-W", "log")
    #job.job_info("0006300-SAMPLE-oozie-bpse-W", "errorlog") --
    #job.job_info("0005931-SAMPLE-oozie-bpse-C", "auditlog")  --
    #job.job_log("0006300-SAMPLE-oozie-bpse-W", logfilter="limit=3;loglevel=WARN")
    #job.job_graph("0006300-SAMPLE-oozie-bpse-W", file_location="C:/Users/User/Desktop/", showkill="false")
    #job.job_status("0006300-SAMPLE-oozie-bpse-W")
    
    #jobs.jobs_information()
    #jobs.jobs_information(1, 1)
    #jobs.jobs_information(10, 1, status="RUNNING")
    #jobs.jobs_bulk_modify("kill", 1, 1, jobtype="wf", status="RUNNING")
    
    #job.managing_job("0005931-SAMPLE-oozie-bpse-C", managing_type="action", scope="4")
       

if __name__ == '__main__':
    main()