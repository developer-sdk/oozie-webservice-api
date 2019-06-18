우지 4.2.0 버전 기준의 [웹서비스 API](https://oozie.apache.org/docs/4.2.0/WebServicesAPI.html)를 파이썬으로 개발하였습니다.  우지 웹서비스는 0, 1, 2 버전이 존재합니다. 버전에 따라 사용 가능한 API가 다르기 때문에 우지 웹서비스가 제공하는 버전을 확인하고 명령을 처리하는 것이 좋습니다. 

# End-Point 종류

+ versions
	+ 사용 가능한 웹서비스 버전 정보 확인 
+ admin
	+ 우지 관련 정보 확인 
	+ 환경변수, 설정변수 등의 정보 확인 
+ job
	+ 잡의 정보, 로그 확인. 잡의 설정 변경. 잡의 상태 변경 
+ jobs
	+ 우지에 잡을 제출. 정보 확인. 잡의 설정 변경.
	+ job과 유사하지만 상태, 잡타입 등의 범위를 설정하여 대규모 변경에 이용
+ sla
	+ SLA 관련 정보 확인 

## 버전별 사용가능한 End-Point
버전|End-Point
-|-
v1|admin, job, jobs
v2|admin, job, jobs, sla

# Versions
versions는 사용 가능한 웹서비스 버전 정보 확인합니다. 반환 정보로 사용가능한 API 버전 정보를 확인할 수 있습니다. 

요청타입|url|비고
-|-|-
GET|/oozie/versions|버전 정보 확인


# admin
우지 관련 정보를 확인합니다. 정보를 json 형태로 반환합니다. Instrumentation와 Metrics은 설정에 따라 둘 중 하나만 동작합니다. 

명령어|함수명 
-|-
System Status|status
OS Environment|os_env
Java System Properties|java_sys_properties
Oozie Configuration|configuration
Oozie Instrumentation|instrumentation
Oozie Metrics|metrics
Version|build_version
Available Time Zones|available_timezones
Queue Dump|queue_dump
Available Oozie Servers|available_oozie_servers
List available sharelib|list_sharelib
Update system sharelib|update_sharelib

# jobs, job
잡의 정보, 로그 확인, 잡의 설정 변경, 잡의 상태 변경을 할 수 있습니다. 필터링은 각 End-Point의 필터링 객체를 이용하여 전달합니다. 

* jobs는 mapreduce, pig, hive, sqoop 잡을 지정해서 처리할 수 있습니다. 
* rerun은 추가적인 파라미터가 필요함. 워크플로우 리런은 xml 파일이 필요함. 코디네이터 리런은 아이디 기준과 작업 일자 기준이 있음. 번들 리런은 코디네이터 기준과 작업 일자 기준이 있음 

End-Points|명령어|함수명
-|-|-
Jobs|Job Submission|submit_job
Jobs|Standard Job Submission|submit_job
Jobs|Proxy MapReduce Job Submission|submit_job
Jobs|Proxy Pig Job Submission|submit_job
Jobs|Proxy Hive Job Submission|submit_job
Jobs|Proxy Sqoop Job Submission|submit_job
Job|Managing a Job|managing_job
Job|    Re-Running a Workflow Job|rerun_workflow
Job|    Re-Running a coordinator job|rerun_coordinator_on_action(). rerun_coordinator_on_date()
Job|    Re-Running a bundle job|rerun_bundle_coord_scope(). rerun_bundle_on_date
Job|    Changing endtime/concurrency/pausetime of a Coordinator Job|change_coordinator_endtime(). change_coordinator_concurrency(). change_coordinator_pausetime(). 
Job|    Updating coordinator definition and properties|update_coordinator
Job|Job Information|job_info. coordinator_allruns
Job|Job Application Definition|job_definition
Job|Job Log|job_log
Job|Job Error Log|job_log(errorlog)
Job|Job Audit Log|job_log(auditlog)
Job|Filtering the server logs with logfilter options|job_log(filters)
Job|Job graph|job_graph
Job|Job Status|job_status
Job|Changing job SLA definition and alerting|TBD
Jobs|Jobs Information|info
Jobs|Bulk modify jobs|managing_jobs
Jobs|Jobs information using Bulk API|TBD