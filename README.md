### API

``GET /api/v1/model``

| Object Field | Type | Required? | Description                                                      |
|--------------|------|-----------|------------------------------------------------------------------|
| `limit`      | bool | no        | returns a list with models of `limit`                            |
| `page`       | int  | no        | if limit is set there might be more pages with lenght of `limit` |

Returns a json array with a list of all currently registered models


List models
---------------------
### Request
  `GET /api/v1/model`

#### Request Body
  

| Object Field       | Type    | Required? | Description                                                                                                       |
|--------------------|---------|-----------|-------------------------------------------------------------------------------------------------------------------|
| `limit`            | bool    | yes       | Name of the router group.                                                                                         |
| `page`             | integer | yes       | Type of the router group e.g. `http` or `tcp`.                                                                    |

### Response
  Expected Status `200 OK`

#### Response Body
  A JSON list of all models

| Object Field       | Type   | Description                                                                   |
|--------------------|--------|-------------------------------------------------------------------------------|
| `guid`             | string | GUID of the router group.                                                     |
| `name`             | string | External facing port for the TCP route.                                       |
| `type`             | string | Type of the router group e.g. `tcp`.                                          |
| `reservable_ports` | string | Comma delimited list of reservable port or port ranges. (For `type` of `TCP`) |

#### Example Response:
```json
{
  "guid": "568c0232-e7c0-47ff-4c8a-bc89b49ade5b",
  "name": "my-router-group",
  "type": "http"
  "reservable_ports": ""
}
```