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

# versions
사용가능한 우지 웹서비스 버전을 반환합니다. 반환값은 현재 0, 1, 2가 있습니다. 

```
**Request:**
GET /oozie/versions

**Response:**
HTTP/1.1 200 OK
Content-Type: application/json;charset=UTF-8
.
[0,1]
```