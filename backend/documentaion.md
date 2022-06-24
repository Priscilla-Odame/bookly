## Table of Contents

- [RegisterAPI](#RegisterAPI)
- [RetrieveSurveyDetailsAPI](#RetrieveSurveyDetailsAPI)
- [CreateSurveyDetailsAPI](#CreateSurveyDetailsAPI)
- [Reports](#ReportViewSet)
- [CreateProjectAPI](#CreateProjectApi)
- [ListProjectAPI](#ListProjectAPI)
- [RetrieveProjectAPI](#RetrieveProjectAPI)
- [UpdateProjectAPI](#UpdateProjectAPI)
- [UpdateSurveyDetailsAPI](#UpdateSurveyDetailsAPI)
- [ListSurveyDetailsAPI](#ListSurveyDetailsAPI)
- [DestroySurveyDetailsAPI](#DestroySurveyDetailsAPI)
- [CreateSurveyProgressAPI](#CreateSurveyProgressAPI)
- [RetrieveSurveyProgressAPI](#RetrieveSurveyProgressAPI)
- [UpdateSurveyProgressAPI](#UpdateSurveyProgressAPI)
- [DestroySurveyProgressAPI](#DestroySurveyProgressAPI)


<a name="RetrieveSurveyDetailsAPI"></a>

## RetrieveSurveyDetailsAPI

This endpoint takes no user input.

_Django Api / RetrieveSurveyDetailsAPI_
This Endpoint was created by **Moses Wuniche Alhassan**

### Request Information

| Type | URL          |
| ---- | ------------ |
| GET  | surveys/<id> |

### Header

| Type             | Property name      |
| ---------------- | ------------------ |
| Allow            | GET, OPTIONS       |
| Content-Type     | application/json   |
| Vary             | Accept             |
| WWW-Authenticate | Bearer realm="api" |

### JSON Body

| Property Name | type | required | Description |
| ------------- | ---- | -------- | ----------- |

### Error Responses

| Code | Message                                         |
| ---- | ----------------------------------------------- |
| 401  | "Authentication credentials were not provided." |
| 404  | "Not found"                                     |

### Successful Response Example

```
{
    "id": 2,
    "deleted_at": null,
    "name": "An awesome survey",
    "question_count": 60,
    "description": "A survey for awesome people",
    "survey_deadline": "2021-03-26T14:43:00Z",
    "published_at": "2021-03-09T14:43:00Z",
    "project": 1
}
```

<a name="CreateSurveyDetailsAPI"></a>

## CreateSurveyDetailsAPI

The CreateSurveyDetailsAPI API will accept the following data fields:
name, description, question_count, created_at, survey_deadline, project

_Django Api / CreateSurveyDetailsAPI_
This Endpoint was created by **Moses Wuniche Alhassan**

### Request Information

| Type | URL            |
| ---- | -------------- |
| POST | surveys/create |

### Header

| Type             | Property name      |
| ---------------- | ------------------ |
| Allow            | POST, OPTIONS      |
| Content-Type     | application/json   |
| Vary             | Accept             |
| WWW-Authenticate | Bearer realm="api" |

### JSON Body

| Property Name   | type      | required | Description                                 |
| --------------- | --------- | -------- | ------------------------------------------- |
| name            | String    | true     | The name of the survey                      |
| description     | String    | true     | A short description of the project          |
| question_count  | int       | true     | The number of question the survey contains  |
| published_at    | DateTime  | false    | The date the survey was published           |
| survey_deadline | DateTimie | true     | The date the survey is due                  |
| project         | int       | true     | The id of the project the survey belongs to |

### Error Responses

| Code | Message                                         |
| ---- | ----------------------------------------------- |
| 400  | "SurveyDetails already exits"                   |
| 401  | "Authentication credentials were not provided." |
| 400  | "This field may not be blank."                  |
| 400  | "A valid integer is required."                  |

### Successful Response Example

```
{
    "id": 2,
    "deleted_at": null,
    "name": "An awesome survey",
    "question_count": 60,
    "description": "A survey for awesome people",
    "survey_deadline": "2021-03-26T14:43:00Z",
    "published_at": "2021-03-09T14:43:00Z",
    "project": 1
}

```

<a name="ReportViewSet">Report List</a>

This API 

1. Creates a report

| Type             | Property name      |
| ---------------- | ------------------ |
| Allow            | POST, OPTIONS      |
| Content-Type     | application/json   |
| Vary             | Accept             |
| WWW-Authenticate | Bearer realm="api" |

### JSON Body

| Property Name   | type      | required | Description                                 |
| --------------- | --------- | -------- | ------------------------------------------- |
| name            | String    | true     | The name of the survey                      |
| description     | String    | true     | A short description of the project          |
| question_count  | int       | true     | The number of question the survey contains  |
| published_at    | DateTime  | false    | The date the survey was published           |
| survey_deadline | DateTimie | true     | The date the survey is due                  |
| project         | int       | true     | The id of the project the survey belongs to |

### Error Responses

| Code | Message                                         |
| ---- | ----------------------------------------------- |
| 400  | "SurveyDetails already exits"                   |
| 401  | "Authentication credentials were not provided." |
| 400  | "This field may not be blank."                  |
| 400  | "A valid integer is required."                  |

### Successful Response Example

```
[
 {
        "id": 2,
        "project": "http://127.0.0.1:8000/projects/api/project/1",
        "name": "Telefonica - Report 2",
        "description": "Description of Telefonica - Report 2",
        "published_at": "2021-03-04",
        "last_modified": "2021-03-04"
    },
    {
        "id": 5,
        "project": "http://127.0.0.1:8000/projects/api/project/1",
        "name": "Telefonica - Report 3",
        "description": "Description of Telefonica - Report 3",
        "published_at": "2021-03-04",
        "last_modified": "2021-03-04"
    }
]

```

2. returns the list of reports that the currently logged in user is authorized to view.
Additional get parameters to can be used to customize the results returned by the API.

3. Updates a report

4.  Deletes a report

## List Reports API

\_Django Api / ListReports
This Endpoint was created by **Robert Kamau Njuguna**

### Request Information

| Type    | URL                |
| ----    | ------------       |
| GET     | api/reports/       |
| POST    | api/reports/       |
| UPDATE  | api/reports/pk     |
| DELETE  | api/reports/delete |

### Header

| Type         | Property name    |
| ------------ | ---------------- |
| Allow        | GET, OPTIONS     |
| Content-Type | application/json |

### Request Parameters

| Property Name | type         | required | Description                             |
| ------------- | ------------ | -------- | --------------------------------------- |
| is_unread     | query string | no       | set value 1 to return unread parameters |

### Error Responses

| Code | Message                                         |
| ---- | ----------------------------------------------- |
| 401  | "Authentication credentials were not provided." |
| 404  | "Not found"                                     |

### Successful Response Example

```
[
    {
        "id": 2,
        "project": "http://127.0.0.1:8000/projects/api/project/1",
        "name": "Telefonica - Report 2",
        "description": "Description of Telefonica - Report 2",
        "published_at": "2021-03-04",
        "last_modified": "2021-03-04"
    },
    {
        "id": 5,
        "project": "http://127.0.0.1:8000/projects/api/project/1",
        "name": "Telefonica - Report 3",
        "description": "Description of Telefonica - Report 3",
        "published_at": "2021-03-04",
        "last_modified": "2021-03-04"
    },
    {
        "id": 6,
        "project": "http://127.0.0.1:8000/projects/api/project/1",
        "name": "Telefonica - Report 4",
        "description": "Description of Telefonica - Report 4",
        "published_at": "2021-03-04",
        "last_modified": "2021-03-04"
    },
]
```

<a name="CreateProjectAPI"></a>

## CreateProjectApi

This endpoint takes no user input.

_Django Api / CreateProjectAPI_
This Endpoint was created by **Philip Owusu-Afriyie**

### Request Information

| Type | URL                |
| ---- | ------------------ |
| POST | api/project/create |

### Header

| Type             | Property name      |
| ---------------- | ------------------ |
| Allow            | POST, OPTIONS      |
| Content-Type     | application/json   |
| Vary             | Accept             |
| WWW-Authenticate | Bearer realm="api" |

### JSON Body

| Property Name | type   | required | Description                                           |
| ------------- | ------ | -------- | ----------------------------------------------------- |
| name          | String | true     | The name of the project                               |
| description   | String | false    | A short description of the project                    |
| company       | int    | true     | The name of the company the project belongs to        |
| status        | String | true     | The status of the project, whether active or inactive |
| published_by  | int    | true     | The id of the creator of the project                  |

### Error Responses

| Code | Message                                         |
| ---- | ----------------------------------------------- |
| 400  | "project with this name already exists."        |
| 401  | "Authentication credentials were not provided." |
| 404  | "Not found"                                     |

### Successful Response Example

```
[
    {
        "id": 4,
        "name": "Pull",
        "company": 1,
        "description": "Hello Hi",
        "published_at": "2021-03-04T15:27:27.795668Z",
        "status": "active",
        "created_by": 1
    }
]
```

<a name="UpdateSurveyDetailsAPI"></a>

## UpdateSurveyDetailsAPI

This endpoint recieves the following field data:
name, description, question_count, published_at, survey_deadline, project

_Django Api / UpdateSurveyDetailsAPI_
This Endpoint was created by **Moses Wuniche Alhassan**

### Request Information

| Type       | URL                 |
| ---------- | ------------------- |
| PUT, PATCH | surveys/update/<id> |

### Header

| Type         | Property name       |
| ------------ | ------------------- |
| Allow        | PUT, PATCH, OPTIONS |
| Content-Type | application/json    |
| Vary         | Accept              |

### JSON Body

| Property Name   | type     | required | Description                                         |
| --------------- | -------- | -------- | --------------------------------------------------- |
| name            | String   | true     | The updated name of the survey                      |
| description     | String   | false    | Updated description of the project                  |
| question_count  | int      | true     | Updated number of question the survey contains      |
| published_at    | DateTime | true     | Updated published date                              |
| survey_deadline | DateTime | true     | Updated due date                                    |
| project         | int      | true     | The updated id of the project the survey belongs to |

### Error Responses

| Code | Message                                         |
| ---- | ----------------------------------------------- |
| 401  | "Authentication credentials were not provided." |
| 400  | "This field may not be blank."                  |
| 400  | "A valid integer is required."                  |

### Successful Response Example

```
{
    "id": 2,
    "deleted_at": null,
    "name": "An updated awesome survey",
    "question_count": 70,
    "description": "An updated survey for awesome people",
    "survey_deadline": "2022-03-26T14:43:00Z",
    "published_at": "2021-03-09T14:43:00Z",
    "project": 1
}
```

<a name="ListSurveyDetailsAPI"></a>

## ListSurveyDetailsAPI

This endpoint takes no user input.

_Django Api / ListSurveyDetailsAPI_
This Endpoint was created by **Moses Wuniche Alhassan**

### Request Information

| Type | URL      |
| ---- | -------- |
| GET  | surveys/ |

### Header

| Type             | Property name      |
| ---------------- | ------------------ |
| Allow            | GET, OPTIONS       |
| Content-Type     | application/json   |
| Vary             | Accept             |
| WWW-Authenticate | Bearer realm="api" |

### JSON Body

| Property Name | type | required | Description |
| ------------- | ---- | -------- | ----------- |

### Error Responses

| Code | Message                                         |
| ---- | ----------------------------------------------- |
| 401  | "Authentication credentials were not provided." |
| 404  | "Not found"                                     |

### Successful Response Example

```
[
    {
    "id": 2,
    "deleted_at": null,
    "name": "An awesome survey",
    "question_count": 60,
    "description": "A survey for awesome people",
    "survey_deadline": "2021-03-26T14:43:00Z",
    "published_at": "2021-03-09T14:43:00Z",
    "project": 1
},
    {
    "id": 4,
    "deleted_at": null,
    "name": "Another awesome survey",
    "question_count": 44,
    "description": "Another survey for awesome people",
    "survey_deadline": "2021-03-26T14:43:00Z",
    "published_at": "2021-03-11T14:55:00Z",
    "project": 2
}
]
```

<a name="DestroySurveyDetailsAPI"></a>

## DestroySurveyDetailsAPI

This endpoint takes no user input.

_Django Api / DestroySurveyDetailsAPI_
This Endpoint was created by **Moses Wuniche Alhassan**

### Request Information

| Type   | URL                 |
| ------ | ------------------- |
| DELETE | surveys/remove/<id> |

### Header

| Type             | Property name      |
| ---------------- | ------------------ |
| Allow            | DELETE, OPTIONS    |
| Content-Type     | application/json   |
| Vary             | Accept             |
| WWW-Authenticate | Bearer realm="api" |

### JSON Body

| Property Name | type | required | Description |
| ------------- | ---- | -------- | ----------- |

### Error Responses

| Code | Message                                         |
| ---- | ----------------------------------------------- |
| 401  | "Authentication credentials were not provided." |
| 404  | "Not found"                                     |

```

```

<a name="ListProjectAPI"></a>

## ListProjectAPI

This endpoint takes no user input.

_Django Api / ListProjectAPI_
This Endpoint was created by **Philip Owusu-Afriyie**

### Request Information

| Type | URL          |
| ---- | ------------ |
| GET  | api/projects |

### Header

| Type             | Property name      |
| ---------------- | ------------------ |
| Allow            | GET,HEAD, OPTIONS  |
| Content-Type     | application/json   |
| Vary             | Accept             |
| WWW-Authenticate | Bearer realm="api" |

### Error Responses

| Code | Message                                         |
| ---- | ----------------------------------------------- |
| 401  | "Authentication credentials were not provided." |
| 404  | "Not found"                                     |

### Successful Response Example

```
[
{
"id": 1,
"name": "Telefonica",
"company": 1,
"description": "Description of the Telefonica Project",
"published_at": "2021-03-03T12:48:18.579000Z",
"status": "active",
"created_by": 1
},
{
"id": 2,
"name": "Lafarge",
"company": 1,
"description": "Description of the Lafarge Project",
"published_at": "2021-03-03T12:48:18.579000Z",
"status": "active",
"created_by": 1
}
]

```

<a name="RetrieveProjectAPI"></a>

## RetrieveProjectAPI

This endpoint takes no user input.

_Django Api / RetrieveProjectAPI_
This Endpoint was created by **Philip Owusu-Afriyie**

### Request Information

| Type | URL              |
| ---- | ---------------- |
| GET  | api/project/<id> |

### Header

| Type             | Property name      |
| ---------------- | ------------------ |
| Allow            | GET,HEAD, OPTIONS  |
| Content-Type     | application/json   |
| Vary             | Accept             |
| WWW-Authenticate | Bearer realm="api" |

### Error Responses

| Code | Message                                         |
| ---- | ----------------------------------------------- |
| 401  | "Authentication credentials were not provided." |
| 404  | "Not found"                                     |

### Successful Response Example

```
{
"project": {
"id": 1,
"deleted_at": null,
"name": "Telefonica",
"description": "Description of the Telefonica Project",
"company_id": 1,
"published_at": "2021-03-03T12:48:18.579000Z",
"status": "active",
"created_by_id": 1
},
"members": [
{
"user__firstname": "George",
"user__othernames": "Awesome",
"user__email": "george@somewhere.com",
"id": 1,
"role__name": "Member",
"published_at": "2021-03-04",
"access_status": "invited",
"approval_status": "1"
},
{
"user__firstname": "Priscy",
"user__othernames": "Awesome",
"user__email": "caribbeanbarbie0@gmail.com",
"id": 4,
"role__name": "Member",
"published_at": "2021-03-15",
"access_status": "invited",
"approval_status": "0"
}
]
}

```

<a name="CreateSurveyProgressAPI"></a>

## CreateSurveyProgressAPI

The CreateSurveyProgressAPI API will accept the following data fields:
user, survey, is_current, questions_completed, last_modified, is_completed.

_Django Api / CreateSurveyProgressAPI_
This Endpoint was created by **Moses Wuniche Alhassan**

### Request Information

| Type | URL                     |
| ---- | ----------------------- |
| POST | surveys/progress/create |

### Header

| Type             | Property name      |
| ---------------- | ------------------ |
| Allow            | POST, OPTIONS      |
| Content-Type     | application/json   |
| Vary             | Accept             |
| WWW-Authenticate | Bearer realm="api" |

### JSON Body

| Property Name       | type     | required | Description                                                                |
| ------------------- | -------- | -------- | -------------------------------------------------------------------------- |
| user                | int      | true     | The id of the user who's survey completion progress is being tracked       |
| survey              | int      | true     | The id of the survey which' progress is being tracked                      |
| is_current          | boolean  | false    | This indicates whether the given survey is the users current survey or not |
| questions_completed | int      | true     | The total number of questions in the given survey                          |
| last_modified       | DateTime | fasle    | The date and time the user's progress was last updated                     |
| is_completed        | boolean  | false    | Indicates the completion status of the survey                              |

### Error Responses

| Code | Message                                         |
| ---- | ----------------------------------------------- |
| 400  | "SurveyProgress already exits"                  |
| 401  | "Authentication credentials were not provided." |
| 400  | "This field may not be blank."                  |
| 400  | "A valid integer is required."                  |

### Successful Response Example

```
{
    "id": 1,
    "deleted_at": null,
    "questions_completed": 77,
    "is_completed": false,
    "last_modified": "2021-03-24T21:08:28.322356Z",
    "is_current": true,
    "user": 1,
    "survey": 2
}

```

<a name="RetrieveSurveyProgressAPI"></a>

## RetrieveSurveyProgressAPI

This endpoint takes no user input.

_Django Api / RetrieveSurveyProgressAPI_
This Endpoint was created by **Moses Wuniche Alhassan**

### Request Information

| Type | URL                  |
| ---- | -------------------- |
| GET  | surveys/progess/<id> |

### Header

| Type             | Property name      |
| ---------------- | ------------------ |
| Allow            | GET, OPTIONS       |
| Content-Type     | application/json   |
| Vary             | Accept             |
| WWW-Authenticate | Bearer realm="api" |

### JSON Body

| Property Name | type | required | Description |
| ------------- | ---- | -------- | ----------- |

### Error Responses

| Code | Message                                         |
| ---- | ----------------------------------------------- |
| 401  | "Authentication credentials were not provided." |
| 404  | "Not found"                                     |

### Successful Response Example

```
{
    "id": 1,
    "deleted_at": null,
    "questions_completed": 77,
    "is_completed": false,
    "last_modified": "2021-03-24T21:08:28.322356Z",
    "is_current": true,
    "user": 1,
    "survey": 2
}
```

<a name="UpdateSurveyProgressAPI"></a>

## UpdateSurveyProgressAPI

This endpoint recieves the following field data:
user, survey, is_current, questions_completed, last_modified, is_completed.

_Django Api / UpdateSurveyProgressAPI_
This Endpoint was created by **Moses Wuniche Alhassan**

### Request Information

| Type       | URL                          |
| ---------- | ---------------------------- |
| PUT, PATCH | surveys/progress/update/<id> |

### Header

| Type         | Property name       |
| ------------ | ------------------- |
| Allow        | PUT, PATCH, OPTIONS |
| Content-Type | application/json    |
| Vary         | Accept              |

### JSON Body

| Property Name       | type     | required | Description                                                              |
| ------------------- | -------- | -------- | ------------------------------------------------------------------------ |
| user                | int      | true     | Updated id of the user who's survey completion progress is being tracked |
| survey              | int      | true     | Updated id of the survey which' progress is being tracked                |
| is_current          | boolean  | false    | Udated is_current status                                                 |
| questions_completed | int      | true     | Updated total number of questions in the given survey                    |
| last_modified       | DateTime | fasle    | Updated date and time the user's progress was last updated               |
| is_completed        | boolean  | false    | Updated completion status                                                |

### Error Responses

| Code | Message                                         |
| ---- | ----------------------------------------------- |
| 401  | "Authentication credentials were not provided." |
| 400  | "This field may not be blank."                  |
| 400  | "A valid integer is required."                  |

### Successful Response Example

```
{
    "id": 1,
    "deleted_at": null,
    "questions_completed": 40,
    "is_completed": true,
    "last_modified": "2021-03-24T21:08:28.322356Z",
    "is_current": false,
    "user": 1,
    "survey": 2
}
```

<a name="ListSurveyProgressAPI"></a>

## ListSurveyProgressAPI

This endpoint takes no user input.

_Django Api / ListSurveyProgressAPI_
This Endpoint was created by **Moses Wuniche Alhassan**

### Request Information

| Type | URL               |
| ---- | ----------------- |
| GET  | surveys/progress/ |

### Header

| Type         | Property name    |
| ------------ | ---------------- |
| Allow        | GET, OPTIONS     |
| Content-Type | application/json |
| Vary         | Accept           |

### JSON Body

| Property Name | type | required | Description |
| ------------- | ---- | -------- | ----------- |

### Error Responses

| Code | Message                                         |
| ---- | ----------------------------------------------- |
| 401  | "Authentication credentials were not provided." |
| 404  | "Not found"                                     |

### Successful Response Example

```
[
    {
        "id": 1,
        "deleted_at": null,
        "questions_completed": 40,
        "is_completed": true,
        "last_modified": "2021-03-24T21:08:28.322356Z",
        "is_current": false,
        "user": 1,
        "survey": 2
    }
]
```

<a name="DestroySurveyProgressAPI"></a>

## DestroySurveyProgressAPI

This endpoint takes no user input.

_Django Api / DestroySurveyProgressAPI_
This Endpoint was created by **Moses Wuniche Alhassan**

### Request Information

| Type   | URL                          |
| ------ | ---------------------------- |
| DELETE | surveys/progress/remove/<id> |

### Header

| Type         | Property name    |
| ------------ | ---------------- |
| Allow        | DELETE, OPTIONS  |
| Content-Type | application/json |
| Vary         | Accept           |

### JSON Body

| Property Name | type | required | Description |
| ------------- | ---- | -------- | ----------- |

### Error Responses

| Code | Message                                         |
| ---- | ----------------------------------------------- |
| 401  | "Authentication credentials were not provided." |
| 404  | "Not found"                                     |

```

```

### Method Information

| Name          | Argument-type | Response-type   |
| ------------- | ------------- | --------------- |
| create_ticket | dictionary    | dictionary/JSON |

### Header

| Name      | Property |
| --------- | -------- |
| X-API-Key | api-key  |

The ticket creation script works by sending a request to the hosted osTicket instance which in turn requires one to be authenticated, therefore owing an `API-Key` in order to make said request.
An `API-Key` can be created within the web interface of the hosted osTicket instance by any dev with valid osTicket login credentials at `Admin Profile -> Manage -> API -> Add New API Key`.

This `API-Key` is then included as a dictionary value with the key `api_key` when calling the method.
More information on osTicket API authentication can be found in the link below.

##`https://docs.osticket.com/en/latest/Developer%20Documentation/API%20Docs.html#authentication`

### Required Dictionary Keys -> Required Ticket details

| Key     | type                    | Description                                    |
| ------- | ----------------------- | ---------------------------------------------- |
| name    | string                  | name of ticket-creation submitter              |
| subject | string                  | subject of the ticket                          |
| message | String(plain-text)/html | initial message for the ticket thread          |
| email   | string                  | email of the ticket-creator                    |
| ip      | strings                 | ip address of the machine issueing the request |
| api_key | string                  | x-api-key of the machine sending the request   |

### Optional Dictionary Keys -> Required Ticket details

There are several ticket fields that can be optionally included, these can all be included as keys in the method's dictionary argument when calling said method.
All optional as well as required fields along with their detailed descriptions can be found in link below.

##`https://docs.osticket.com/en/latest/Developer%20Documentation/API/Tickets.html`

### Error Responses

Exceptions are caught and printed to the console should any thing go wrong in the ticket creation process.
This will be improved in later iterations to be sent as a response instead.

### Successful Response Example

```
Status: 201 Created
123456

```

#Note:
A more comprehensive documentation on the osTicket API of which the script is leveraging off of can be found in the url in the link below.

##`https://docs.osticket.com/en/latest/Developer%20Documentation/API/Tickets.html`
