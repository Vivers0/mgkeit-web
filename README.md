# MGKEIT WEB API
## About
an API that allows you to receive, send, change, delete information from users autoclosed in the telegram bot [@MGKEIT_bot](https://t.me/MGKEIT_Bot), as well as receive a schedule for each course

## Instalation
- Clone this repository: `git clone https://github.com/Vivers0/mgkeit-web.git`
- Сd into mgkeit-web: `cd mgkeit-web`
- Install environment: `pip install -r requirements.txt`
- Set migrate: `python manage.py migrate`
- Start project: `python manage.py runserver`

## Authentication
All modules are protected from third party requests. To make requests you need to create / get a token.
If you run a copy of this project, then you need to create a superuser first, then create a token.
For the ***admin*** user this is:

Login: `admin`  
Password: `admin`  
Token: `a43e05d7b529c7190331326b6328c026e8855295`

To create a request, you need to add authorization to the header: 
> Authorization: Token a43e05d7b529c7190331326b6328c026e8855295

## Documentation
### All Users
> GET /api/user/
```json
{
    "users": [
        {
            "user_id": 1234567,
            "course_id": 1,
            "notify": true
        },
        {
            "user_id": 7654321,
            "course_id": 2,
            "notify": false
        }
    ]
}
```
> POST /api/user

Parameter | Type | Description
--- | --- | ---
user_id (necessarily) | Number | ID Telegram user
course_id | Number | ID Course (See [function](https://github.com/Vivers0/mgkeit/blob/master/src/course.py))
notify | Boolean | Whether the user will receive notifications
**Example:**
```json
{
    "user": {
        "user_id": 1234567,
        "course_id": 13,
        "notify": false
    }
}
```

### Certain User
> GET /api/user/:id
```json
{
    "user": {
        "user_id": 1234567,
        "course_id": 1,
        "notify": true
    }
}
```

> PUT /api/user/:id

Parameter | Type | Description
--- | --- | ---
course_id | Number | ID Course (See [function](https://github.com/Vivers0/mgkeit/blob/master/src/course.py))
notify | Boolean | Whether the user will receive notifications
**You can change any number of points**

**Example:**
```json
{
    "user": {
        "notify": true
    }
}
```

> DELETE /api/user/:id

**No have body**
### Get All Timetable
> GET /api/user/:id

return:
```json
{
    "timetable": [
        {
            "course_id": 1,
            "day_week": 0,
            "timetable": "1. Иностранный язык (обе группы), 8:30 - 10:05, каб. 301/311 2.Химия, 10:25 - 12:00, каб. 410 3. Литература, 12:20 - 13:55, каб. 309 4.Физ-ра, 14:15 - 15:50, Зал настольного тенниса",
            "is_odd": true
        },
        {
            "course_id": 31,
            "day_week": 0,
            "timetable": "1. Подготовительные электротехнические работы, 8:30 - 10:05, каб. 55\r\n2. Физ-ра, 10:25 - 12:00, каб. 67\r\n3. Основы технической механики и слесарных работ, 12:20 - 13:55, каб. 60\r\n4. Иностранный язык (1 подгруппа), 14:15 - 15:50, каб. 44",
            "is_odd": true
        }
    ]
}
```
## Status Code
- 401: Invalid or unauthorized API user – verify your API user is valid and authorized to access the API. Contact support if you'd like assistance.
- 403: Missing User-Agent header - all API requests require an User-Agent header, please identify yourself appropriately
- 405: Unknown HTTP method - we only support standard HTTP requests, please double-check your request verb
- 429: Too many requests (throttling) – slow down your request frequency
- 502: Under heavy load – slow down your request frequency
- 5xx: Server error - please double-check your JSON payload for formatting errors, data integrity, etc.

## Other Problems
Have you found a bug? Do you have an API feature request? [Submit an issue](https://github.com/Vivers0/mgkeit-web/issues) (requires a github account)