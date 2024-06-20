# projectly
Simple API to create and manage "projects". A project includes notes and scripts, as well as a simple calendar to track when things should get done.

## Quick Install
Install the requirements listed in `requirements.txt`: `python -m pip install -r requirements.txt`

Migrate the database: `python manage.py migrate`

Create the super user: `python manage.py createsuperuser`
## Run locally
To run the Django API you can simply run: `python manage.py runserver`
## Testing Endpoints
For the current endpoints, see [openapi-schema.yaml](./openapi-schema.yaml).


### Projects
***
#### Create a project
```
curl -X POST -H "Content-Type: application/json" -d "{\"name_text\": \"POST test\", \"pub_date\": \"2024-06-19\"}" http://localhost:8000/projects
```

Which returns a JSON blob such as:

```json
{
    "id":2,
    "name_text":"POST test",
    "pub_date":"2024-06-19"
}
```


#### Get all projects
```curl -X GET http://localhost:8000/projects```

Which returns a JSON blob such as:

```json
[
    {
        "id": 2,
        "name_text": "POST test",
        "pub_date": "2024-06-19"
    }
]
```


#### Get specific project
```curl -X GET http://localhost:8000/projects/2```

Which returns a JSON blob such as:

```json
{
    "id": 2,
    "name_text": "POST test",
    "pub_date": "2024-06-19"
}
```

#### Delete a specific project
```curl -X DELETE http://localhost:8000/projects/2```


### Notes
***
#### Get all notes for a project
```curl -X GET http://localhost:8000/projects/2/notes```

Which returns a JSON blob such as:

```json
[
    {
        "id": 1,
        "project": 2,
        "note_text": "Some note for a project"
    }
]
```

#### Create a note for a specific project
```
curl -X POST -H "Content-Type: application/json" -d "{\"project\": \"2\", \"note_text\": \"Some note for a project\"}" http://localhost:8000/projects/2/notes
```


Which returns a JSON blob such as:

```json
{
    "id": 1,
    "project": 2,
    "note_text": "Some note for a project"
}
```

#### Get a specific project note
```curl -X GET http://localhost:8000/projects/2/notes/1```

Which returns a JSON blob such as:

```json
{
    "id": 1,
    "project": 2,
    "note_text": "Some note for a project"
}
```

#### Update a specific project note
```
curl -X PUT -H "Content-Type: application/json" -d "{\"id\": \"1\", \"project\": \"2\", \"note_text\": \"Some notes for a project need updating\"}" http://localhost:8000/projects/2/notes/1
```

Which returns a JSON blob such as:

```json
{
    "id": 1,
    "project": 2,
    "note_text": "Some notes for a project need updating"
}
```

#### Delete a specific project note

```curl -X DELETE http://localhost:8000/projects/2/notes/1```


### Scripts
***
#### Get all scripts for a project

```curl -X GET http://localhost:8000/projects/2/scripts```

Which returns a JSON blob such as:

```json
[
    {
        "id": 1,
        "project": 2,
        "script_text": "Some note for a project"
    }
]
```

#### Create a script for a specific project

```
curl -X POST -H "Content-Type: application/json" -d "{\"project\": \"2\", \"script_text\": \"A script for the project\"}" http://localhost:8000/projects/2/scripts
```


Which returns a JSON blob such as:

```json
{
    "id": 1,
    "project": 2,
    "script_text": "Some note for a project"
}
```

#### Get a specific project script
```curl -X GET http://localhost:8000/projects/2/scripts/1```

Which returns a JSON blob such as:

```json
{
    "id": 1,
    "project": 2,
    "script_text": "Some note for a project"
}
```

#### Update a specific project script

```
curl -X PUT -H "Content-Type: application/json" -d "{\"id\": \"1\", \"project\": \"2\", \"script_text\": \"Some scripts for a project need updating\"}" http://localhost:8000/projects/2/scripts/1
```

Which returns a JSON blob such as:

```json
{
    "id": 1,
    "project": 2,
    "note_text": "Some notes for a project need updating"
}
```

#### Delete a specific project note
```curl -X DELETE http://localhost:8000/projects/2/notes/1```

### Calendar
***
#### Get all calendar entries for a project

```curl -X GET http://localhost:8000/projects/2/calendar```

Which returns a JSON blob such as:

```json
[
    {
        "id": 2,
        "project": 2,
        "start_date": "2024-06-19",
        "end_date": "2024-06-19",
        "completed": false
    }
]
```

#### Create a calendar entry for a specific project

```
curl -X POST -H "Content-Type: application/json" -d "{\"project\": \"2\", \"start_date\": \"2024-06-19\", \"end_date\": \"2024-06-19\"}" http://localhost:8000/projects/2/calendar
```


Which returns a JSON blob such as:

```json
{
    "id": 2,
    "project": 2,
    "start_date": "2024-06-19",
    "end_date": "2024-06-19",
    "completed": false
}
```

#### Get a specific calendar entry
```curl -X GET http://localhost:8000/projects/2/calendar/2```

Which returns a JSON blob such as:

```json
{
    "id": 2,
    "project": 2,
    "start_date": "2024-06-19",
    "end_date": "2024-06-19",
    "completed": false
}
```

#### Update a specific project script

```
curl -X PUT -H "Content-Type: application/json" -d "{\"id\": 2, \"project\": 2, \"start_date\": \"2024-06-19\", \"end_date\": \"2024-06-19\", \"completed\": true}" http://localhost:8000/projects/2/calendar/2
```

Which returns a JSON blob such as:

```json
{
    "id": 2,
    "project": 2,
    "start_date": "2024-06-19",
    "end_date": "2024-06-19",
    "completed": true
}
```

#### Delete a specific project note
```curl -X DELETE http://localhost:8000/projects/2/calendar/2```