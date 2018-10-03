
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sdk.oozie.ws.OozieWebservice import OozieWebservice

jobxml = '''<?xml version="1.0" encoding="UTF-8"?>
<configuration>
<property><name>user.name</name><value>hadoop</value></property>
<property><name>oozie.wf.application.path</name><value>hdfs:///user/hadoop/MR/CL/</value></property>
<property><name>runDate</name><value>20180901</value></property>
<property><name>runTime</name><value>00</value></property>
<property><name>serviceCode</name><value>701</value></property>
<property><name>serviceName</name><value>PreloadApp</value></property>
<property><name>rawPrefix</name><value>s3://stg-kr-raw</value></property>
<property><name>clEncPrefix</name><value>s3://stg-kr-cl4</value></property>
<property><name>clNoEncPrefix</name><value>s3://stg-kr-cl</value></property>
<property><name>etlPrefix</name><value>s3://stg-kr-etl-log</value></property>
<property><name>deployPrefix</name><value>s3://stg-kr-deploy</value></property>
<property><name>logType</name><value>device</value></property>
<property><name>cleansingDatabase</name><value>PAP_701</value></property>
<property><name>runMonth</name><value>201809</value></property>
<property><name>jobDate</name><value>20180901</value></property>
<property><name>jobDateAfter1</name><value>20180902</value></property>
<property><name>jobDateBefore1</name><value>20180831</value></property>
<property><name>jobDateBefore2</name><value>20180830</value></property>
<property><name>jobDateBefore3</name><value>20180829</value></property>
<property><name>jobDateBefore4</name><value>20180828</value></property>
<property><name>jobDateBefore5</name><value>20180827</value></property>
<property><name>jobDateBefore6</name><value>20180826</value></property>
<property><name>jobDateBefore4hyphen</name><value>2018-08-28</value></property>
<property><name>metaDb</name><value>bod_000</value></property>
<property><name>mccMetaTable</name><value>tmsd_mcc_cnty_rel</value></property>
<property><name>appName</name><value>OOZIE_TEST</value></property>
<property><name>nominalDate</name><value>20180901</value></property>
<property><name>nominalTime</name><value>00</value></property>
</configuration>
'''

proxyxml = '''<?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <property>
        <name>fs.default.name</name>
        <value>hdfs://10.11.96.221localhost:8020</value>
    </property>
    <property>
        <name>mapred.job.tracker</name>
        <value>10.11.96.221localhost:8032</value>
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
        <value>hdfs://ip-10-11-96-221.ap-northeast-2.compute.internallocalhost:8020/user/hadoop/share/lib</value>
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
        <value>hdfs://ip-10-11-96-221.ap-northeast-2.compute.internallocalhost:8020/user/hadoop/MR/CL_MR/kr</value>
    </property>
    <property>
        <name>oozie.wf.rerun.skip.nodes</name>
        <value>PM_ODW_CL</value>
    </property>
</configuration>
'''

update_coord_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<configuration>
<property><name>type</name><value>CL</value></property>
<property><name>serviceName</name><value>PreloadApp</value></property>
<property><name>serviceAbbrName</name><value>PAP</value></property>
<property><name>serviceCode</name><value>701</value></property>
<property><name>logType</name><value>device</value></property>
<property><name>hqlFile</name><value>PM_ODW_DC701_001.hql</value></property>
<property><name>appName</name><value>${serviceName}_${logType}</value></property>
<property><name>freq</name><value>60 </value></property>
<property><name>jobTracker</name><value>ip-10-11-96-221.ap-northeast-2.compute.internal</value></property>
<property><name>nameNode</name><value>ip-10-11-96-221.ap-northeast-2.compute.internal</value></property>
<property><name>jobTrackerPort</name><value>8032</value></property>
<property><name>nameNodePort</name><value>8020</value></property>
<property><name>queueLauncher</name><value>q1</value></property>
<property><name>queueShellLauncher</name><value>q3</value></property>
<property><name>queueCl</name><value>q2</value></property>
<property><name>s3Accesskey</name><value>AKIAIUWIIYDP3MF6ZQ2A</value></property>
<property><name>s3Secretkey</name><value>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</value></property>
<property><name>endFinPrefix</name><value>d.fin</value></property>
<property><name>rawPrefix</name><value>s3://stg-kr-raw</value></property>
<property><name>prsPrefix</name><value>s3://stg-kr-cl5</value></property>
<property><name>clEncPrefix</name><value>s3://stg-kr-cl4</value></property>
<property><name>clNoEncPrefix</name><value>s3://stg-kr-cl</value></property>
<property><name>etlPrefix</name><value>s3://stg-kr-etl-log</value></property>
<property><name>deployPrefix</name><value>s3://stg-kr-deploy</value></property>
<property><name>cleansingDatabase</name><value>${serviceAbbrName}_${serviceCode}</value></property>
<property><name>startTime</name><value>2018-09-16T01:00Z</value></property>
<property><name>endTime</name><value>2018-09-19T01:00Z</value></property>
<property><name>appPath</name><value>hdfs:///user/hadoop/MR/${type}_MR/kr</value></property>
<property><name>oozie.coord.application.path</name><value>${appPath}</value></property>
<property><name>oozie.use.system.libpath</name><value>true</value></property>
<property><name>user.name</name><value>hadoop</value></property>
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
    
    #oozie.managing_job("0006357-SAMPLE-oozie-bpse-W", "kill")
    #oozie.managing_job("0006351-SAMPLE-oozie-bpse-W", "rerun", rerun_xml)
    #oozie.rerunnig_coord_by_action_id("0005928-SAMPLE-oozie-bpse-C", "23-24")
    #oozie.rerunnig_coord_by_date("0005928-SAMPLE-oozie-bpse-C", "2018-08-19T21:00Z", "2018-08-19T23:00Z")
        
    #oozie.rerunnig_bundle_by_action_name("0006373-180305053637798-oozie-bpse-B", ["CL_1"])
    #oozie.rerunnig_bundle_by_date("0006373-180305053637798-oozie-bpse-B", "2018-09-12T01:00Z", "2018-09-12T02:00Z")
    
    #oozie.change_coord_info("0005931-SAMPLE180305053637798-oozie-bpse-C", pausetime="2030-09-12T02:00Z")
    
    #oozie.update_coordinatorjob_info("000638400-SAMPLE180305053637798-oozie-bpse-C", update_coord_xml)
    
    #-oozie-bpse-W")
    #job.job_info("00063005928-SAMPLE180305053637798-oozie-bpse-W")
    #o.job_info("0006420--oozie-bpse-C", show="definition"-oozie-bpse-C", filters='status=SKIPPED', length=3, order='desc')
    #ojob.job_info("0000344-SAMPLE180305053637798-oozie-bpse-C@1")
    #ojob.job_info("0000344-SAMPLE180305053637798-oozie-bpse-C@1", show="allruns", type="action")
    #oozie.job_info("0005928-SAMPLE180305053637798-oozie-bpse-C", s=, offset=1en)
    #oozie)
    #job.job_info("0006300-SAMPLE180305053637798-oozie-bpse-W", show="definition")
    #ooziejob.job_info("0006300-SAMPLE180305053637798-oozie-bpse-W", "log")
    #ojob.job_info("0006300-SAMPLE180305053637798-oozie-bpse-W", "errorlog") --
    #ojob.job_info("0005931-SAMPLE180305053637798-oozie-bpse-C", "auditlog")  --
    #oozie.job_log("0006300-SAMPLE180305053637798-oozie-bpse-W")
    #oozie.job_log("0006300-SAMPLE180305053637798-oozie-bpse-W", show="errorlog")
    #oozie.job_log("0005928-SAMPLE180305053637798-oozie-bpse-C", show="auditlog")
    #oozie.job_log("0006300-SAMPLE180305053637798job.job_log("0006300-SAMPLE-oozie-bpse-W", logfilter="limit=3;loglevel=WARN")
    #ooziejob.job_graph("0006300-SAMPLE180305053637798-oozie-bpse-W", file_location="C:/Users/User/Desktop/", showkill="false")
    #ooziejob.job_status("000639400-SAMPLE180305053637798-oozie-bpse-W")
    
    
    #ooziejobs.jobs_information()
    #ooziejobs.jobs_information(1, 1)
    #ooziejobs.jobs_information(10, 1, status="RUNNING")
    #oozie.jobs_information("coordinator", 10, 1)
    #oozie.jobs_information("wf", 10, 1)
    #oozie.jobs_bulk_modify("kill", "wf", 1, 1, status="RUNNING")
    #oozie.jobs_bulk_bundle_information("BUNDLE_TEST")
    #oozie.jobs_bulk_bundle_information("BUNDLE_TEST", coordi_names=["CL_1", "CL_2"], action_status="RUNNING")
    #oozie.jobs_bulk_bundle_information("BUNDLE_TEST", coordi_names=["CL_1", "CL_2"], endScheduledTime="2018-09-13T07:00Z")
    
    oozie.managing_job_coordinator("0005931-SAMPLE-oozie-bpse-C")
    #ooziejobs.jobs_bulk_modify("kill", 1, 1, jobtype="wf", status="RUNNING")
    
    #job.managing_job_coordinator("0005931-SAMPLE-oozie-bpse-C", managing_type="action", scope="4")
       
if __name__ == '__main__':
    main()