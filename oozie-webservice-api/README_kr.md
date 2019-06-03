# 우지 REST API
우지 웹서비스 API는 HTTP를 이용하여, REST 형식으로 호출하면 JSON 형식의 데이터를 반환합니다. 모든 응답은 UTF-8로 반환됩니다. 제공하는 서비스 목록은 다음과 같습니다. 

-   /versions
-   /v1/admin
-   /v1/job
-   /v1/jobs
-   /v2/job
-   /v2/jobs
-   /v2/admin
-   /v2/sla 

# Versions End-Point
사용 가능한 우지 웹서비스 버전을 반환합니다. 반환값은 현재 0, 1, 2가 있습니다. 

```
**Request:**
GET /oozie/versions

**Response:**
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
.
[0,1]
```

# Admin End-Point
우지의 시스템 상태 및 설정 정보를 얻는데 사용합니다. 

## System Status 
시스템 상태를 얻는 방법은 status를 이용합니다. status는 두가지 모드가 있습니다. 하나는 상태를 얻어오는 것이고, 다른 하나는 상태를 변경하는 것입니다. 

### Get을 이용하여 상태 확인 
상태를 확인할 때는 get방식을 이용하여 처리합니다.  

```
Request:
GET /oozie/v1/admin/status

Response:
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
.
{"systemMode":NORMAL}
```

### Put을 이용하여 상태 변경 
상태를 변경할 때는 put 방식을 이용하고, 변경하고자 하는 상태를 url에 인코딩하여 전달합니다. NORMAL, NOWEBSERVICE, SAFEMODE 중 한가지 상태로 변경 할 수 있습니다. 

```
Request:
PUT /oozie/v1/admin/status?systemmode=SAFEMODE

Response:
HTTP/1.1 200 OK
```

## OS Environment
우지 시스템의 OS환경을 반환합니다. 

```
Request:
GET /oozie/v1/admin/os-env

Response:
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
.
{
  TERM: "xterm",
  JAVA_HOME: "/usr/java/latest",
  XCURSOR_SIZE: "",
  ...
}
```

## Java System Properties
우지 자바 환경 정보를 반환합니다.  

```
Request:
GET /oozie/v1/admin/java-sys-properties

Response:
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
.
{
  java.vm.version: "11.0-b15",
  sun.jnu.encoding: "UTF-8",
  java.vendor.url: "http://java.sun.com/",
  java.vm.info: "mixed mode",
  ...
}
```


## Oozie Configuration
우지 설정 정보를 반환합니다. 


```
Request:
GET /oozie/v1/admin/configuration

Response:
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
.
{
  oozie.service.SchedulerService.threads: "5",
  oozie.service.ActionService.executor.classes: "
            org.apache.oozie.dag.action.decision.DecisionActionExecutor,
            org.apache.oozie.dag.action.hadoop.HadoopActionExecutor,
            org.apache.oozie.dag.action.hadoop.FsActionExecutor
        ",
  oozie.service.CallableQueueService.threads.min: "10",
  oozie.service.DBLiteWorkflowStoreService.oozie.autoinstall: "true",
  ...
}
```