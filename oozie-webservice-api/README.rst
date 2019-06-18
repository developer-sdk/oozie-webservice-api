This is Python Library for Oozie Web service api.

This project follows the [Oozie 4.2.0 WebServicesAPI](https://oozie.apache.org/docs/4.2.0/WebServicesAPI.html) document.

Usage
=====

Install it::

    pip install oozie-webservice-api

Usage::

	from oozie import OozieWebService
    import json
    '''
    Ooize Web Service Test

    @author: hs_seo
    @since: 2019.06.18
    '''

            
    if __name__ == "__main__":
        
        rerun_xml = '''<?xml version="1.0" encoding="UTF-8"?>
    <configuration>
        <property><name>user.name</name><value>hadoop</value></property>
    </configuration>
    '''
        
        submit_xml = '''<?xml version="1.0" encoding="UTF-8"?>
    <property><name>user.name</name><value>hadoop</value></property>
    </configuration>
    '''

        update_xml = """<configuration>
    <property><name>user.name</name><value>hadoop</value></property>
    </configuration>"""
        
        
        # https://oozie.apache.org/docs/4.2.0/WebServicesAPI.html
        oozie = OozieWebService("http://localhost:11000")
        
        ## Versions - all json return
        return_obj = oozie.version.oozie_versions()
        
        ## Admin - all json return
        return_obj = oozie.admin.status()
        return_obj = oozie.admin.status('NORMAL')
        return_obj = oozie.admin.os_env()
        return_obj = oozie.admin.java_sys_properties()
        return_obj = oozie.admin.configuration()
        return_obj = oozie.admin.instrumentation()
        return_obj = oozie.admin.metrics()    # if metric enable
        return_obj = oozie.admin.build_version()
        return_obj = oozie.admin.available_timezones()
        return_obj = oozie.admin.queue_dump()
        return_obj = oozie.admin.available_oozie_servers()
        return_obj = oozie.admin.list_sharelib()
        return_obj = oozie.admin.list_sharelib("pig")
        return_obj = oozie.admin.update_sharelib()
        
        ## Jobs
        #filters = oozie.jobs.Filters()
        
        # Job Submission
        return_obj = oozie.jobs.submit_job(submit_xml)                           # start ok
        return_obj = oozie.jobs.submit_job(submit_xml, job_type="mapreduce")    # start ok
        return_obj = oozie.jobs.info()
        return_obj = oozie.jobs.info(filters)
        return_obj = oozie.jobs.managing_jobs("kill", "coordinator", filters)      
        
        ## Job
        # Managing a Job
        #co_id = "C-ID"
        #wf_id = "W-ID"
        return_obj = oozie.job.managing_job(wf_id, 'start')                 # start ok
        return_obj = oozie.job.managing_rerun_workflow(wf_id, rerun_xml)    # rerun ok
        return_obj = oozie.job.rerun_coordinator_on_action(co_id, "1")      # rerun ok
        return_obj = oozie.job.rerun_coordinator_on_date(co_id, "2019-05-22T16:00Z", "2019-05-22T16:00Z")    # rerun ok
        return_obj = oozie.job.change_coordinator_concurrency(co_id, 2)
        return_obj = oozie.job.change_coordinator_endtime(co_id, "2019-06-02T16:00Z")
        return_obj = oozie.job.change_coordinator_pausetime(co_id, "2019-06-01T16:00Z")
        return_obj = oozie.job.update_coordinator(co_id, update_xml)
        
        # filter
        #filters = oozie.job.Filters()
        #filters.len = 100
        
        # Log Fiter
        #log_filters = oozie.job.LogFilters()
        
        return_obj = oozie.job.job_info(wf_id)
        return_obj = oozie.job.job_info(co_id)
        return_obj = oozie.job.job_info(co_id, filters)
        return_obj = oozie.job.coordinator_allruns(co_id, "1")
        return_obj = oozie.job.coordinator_allruns(co_id, "1", filters)
        
        return_obj = oozie.job.job_definition(wf_id)
        return_obj = oozie.job.job_log(wf_id)  # txt return
        return_obj = oozie.job.job_log(wf_id)  # txt return
        return_obj = oozie.job.job_log(wf_id, filters=log_filters)  # txt return
        return_obj = oozie.job.job_log(wf_id, "errorlog")  # txt return
        return_obj = oozie.job.job_log(wf_id, "auditlog")  # txt return
        return_obj = oozie.job.job_status(wf_id)
        return_obj = oozie.job.job_graph(wf_id, file_over_write=True)
        
        
        if return_obj.isok:
            print(return_obj.info.url)
            
            if "Content-Type" in return_obj.headers and "application/json" in return_obj.headers["Content-Type"]:
                json_obj = json.loads(return_obj.body)
                print(json.dumps(json_obj, indent=4, sort_keys=True))
            else:
                print(return_obj.body)
        else:
            print(return_obj.info.filename)
            print(return_obj.info.headers['oozie-error-code'])
            print(return_obj.info.headers['oozie-error-message'])
            print(return_obj.body)