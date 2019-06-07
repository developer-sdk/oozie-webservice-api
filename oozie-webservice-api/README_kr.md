우지 4.2.0 버전 기준의 [웹서비스 API](https://oozie.apache.org/docs/4.2.0/WebServicesAPI.html)를 파이썬으로 개발하였습니다. 

# API 종류
우지 웹서비스 API는 HTTP 프로토콜을 이용합니다. GET, PUT 방식을 이용하여 데이터를 전달하면 json 형식으로 응답을 회신합니다.  사용가능한 API 목록은 다음과 같습니다. 

-   /versions
-   /v1/admin
-   /v1/job
-   /v1/jobs
-   /v2/job
-   /v2/jobs
-   /v2/admin
-   /v2/sla 

## End-Point 
우지 API의 구성은 `/버전/End-Point` 형식으로 사용합니다. 각 엔드 포인트에서 사용가능한 정보는 다음과 같습니다. 

- versions
	- 사용가능한 API 버전 정보를 반환 
- admin
	- OS, Java, 우지 관련 정보를 반환 
- job, jobs
	- 잡(번들, 코디네이터, 워크플로우)의 실행
	- 잡의 상태, 로그 등의 정보 반환

## 목록 

### versions
versions의 요청 타입에는 버전정보가 들어가지 않습니다. 

요청타입|url|비고
-|-|-
GET|/oozie/versions|버전 정보 확인

### admin
instrumentation과 metric은 둘 중 하나만 요청 가능합니다. 하나가 지원되면 다른 하나는 지원되지 않습니다 .

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

### job

요청타입|url|비고
-|-|-
POST|/oozie/v1/jobs|잡 제출 
