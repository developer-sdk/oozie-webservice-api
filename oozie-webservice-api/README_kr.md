우지 4.2.0 버전 기준의 [웹서비스 API](https://oozie.apache.org/docs/4.2.0/WebServicesAPI.html)를 파이썬으로 개발하였습니다.  우지 웹서비스는 0, 1, 2 버전이 존재합니다. 버전에 따라 사용 가능한 API가 다르기 때문에 우지 웹서비스가 제공하는 버전을 확인하고 명령을 처리하는 것이 좋습니다. 

# End-Point 종류
End-Point|설명
-|-
versions|사용 가능한 웹서비스 버전 정보 확인 
admin|우지 관련 정보 확인 
job|잡의 정보, 로그 확인. 잡의 설정 변경. 잡의 상태 변경 
jobs|우지에 잡을 제출 
sla|SLA 관련 정보 확인 

### 버전별 사용가능한 End-Point
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
우지 관련 정보를 확인합니다. 정보를 json 형태로 반환합니다. 

요청타입|url|비고
-|-|-
GET|/oozie/v1/admin/status|우지 상태 확인 
GET|/oozie/v1/admin/os-env|os 설정값 확인 
GET|/oozie/v1/admin/java-sys-properties|자바 설정값 확인 
GET|/oozie/v1/admin/configuration|우지 설정값 확인 
GET|/oozie/v1/admin/instrumentation|우지 계측 정보 
GET|/oozie/v2/admin/metrics|우지 계측 정보
GET|/oozie/v1/admin/build-version|우지 빌드 버전 정보 
GET|/oozie/v1/admin/available-timezones|타임존 정보 
GET|/oozie/v1/admin/queue-dump|우지 큐 정보 
GET|/oozie/v2/admin/available-oozie-servers|우지 서버 정보. 고가용성 
GET|/oozie/v2/admin/list_sharelib|쉐어 라이브러리 정보 
GET|/oozie/v2/admin/list_sharelib?lib=pig*|조회 가능 
GET|/oozie/v2/admin/update_sharelib|쉐어 라이브러리 갱신 

* Instrumentation와 Metrics은 둘 중 하나만 동작합니다. 

# jobs
우지에 잡을 제출합니다. 잡 관련 정보를 XML 형태로 전달하면, 잡의 ID를 반환합니다. 

요청타입|url|비고
-|-|-
POST|/oozie/v1/jobs|잡 제출 

# job
잡의 정보, 로그 확인, 잡의 설정 변경, 잡의 상태 변경을 할 수 있습니다. 

요청타입|url|비고|반환값
-|-|-|-
PUT|/oozie/v1/job/[잡-ID]?action=start|잡 실행|json
GET|/oozie/v1/job/job-3?show=info|잡 정보 확인 |json
GET|/oozie/v1/job/job-3?show=definition|잡 선언 정보 확인|xml
