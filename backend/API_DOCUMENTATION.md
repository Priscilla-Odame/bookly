The ValidateEmailAPI checks if an email is valid and if it is already in the DB during sign up,
this is to ensure that a valid email is used and no user can create two accounts using the same email

_Django API / Email Valid and Unique
This Endpoint was created by **Priscilla Odame**

### Request Information
|Type|URL|
|--|--|
|GET|/api/email/|

### Header
|Type|Property name|
|--|--|
|Allow|POST, OPTIONS|
|Content-Type|application/json|
|Vary|Accept|


### JSON Body
|Property Name|type|required|Description|
|--|--|--|--|
|email|CharField|true| email for the user|

### Error Responses
| Code | Message |
|--|--|
| 400 | "The email address is already in use."
| 400 | "Enter a valid email address."
| 400 | "Please provide an email"

### Successful Response Example
```
|Code | Message |
|--|--|
| 200 | OK      |
{
    "Email is valid and available"
}
```
