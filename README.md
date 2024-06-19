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
### Create a project
<details>
    <summary>Expand</summary>

#### Via curl
```curl -X POST -H "Content-Type: application/json" -d "{\"name_text\": \"POST test\", \"pub_date\": \"2024-06-19\"}" http://localhost:8000/projects```

Which returns a JSON blob such as:

```json
{
    "id":2,
    "name_text":"POST test",
    "pub_date":"2024-06-19"
}
```
</details>


### Get all projects
<details>
    <summary>Expand</summary>

#### Via curl
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
</details>

### Get specific project
<details>
    <summary>Expand</summary>

#### Via curl
```curl -X GET http://localhost:8000/projects/2```

Which returns a JSON blob such as:

```json
{
    "id": 2,
    "name_text": "POST test",
    "pub_date": "2024-06-19"
}
```
</details>

### Delete a specific project
<details>
    <summary>Expand</summary>

#### Via curl
```curl -X DELETE http://localhost:8000/projects/2```

</details>

### Get all notes for a project
<details>
    <summary>Expand</summary>

#### Via curl
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
</details>

### Create a note for a specific project
<details>
    <summary>Expand</summary>

#### Via curl
```curl -X POST -H "Content-Type: application/json" -d "{\"project\": \"2\", \"note_text\": \"Some note for a project\"}" http://localhost:8000/projects/2/notes```


Which returns a JSON blob such as:

```json
{
    "id": 1,
    "project": 2,
    "note_text": "Some note for a project"
}
```
</details>

### Get a specific project note
<details>
    <summary>Expand</summary>

#### Via curl
```curl -X GET http://localhost:8000/projects/2/notes/1```

Which returns a JSON blob such as:

```json
{
    "id": 1,
    "project": 2,
    "note_text": "Some note for a project"
}
```
</details>

### Update a specific project note
<details>
    <summary>Expand</summary>

#### Via curl
```curl -X PUT -H "Content-Type: application/json" -d "{\"id\": \"1\", \"project\": \"2\", \"note_text\": \"Some notes for a project need updating\"}" http://localhost:8000/projects/2/notes/1```

Which returns a JSON blob such as:

```json
{
    "id": 1,
    "project": 2,
    "note_text": "Some notes for a project need updating"
}
```
</details>

### Delete a specific project note
<details>
    <summary>Expand</summary>

#### Via curl
```curl -X DELETE http://localhost:8000/projects/2/notes/1```
</details>

### Get all scripts for a project
<details>
    <summary>Expand</summary>

#### Via curl
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
</details>

### Create a script for a specific project
<details>
    <summary>Expand</summary>

#### Via curl
```curl -X POST -H "Content-Type: application/json" -d "{\"project\": \"2\", \"script_text\": \"A script for the project\"}" http://localhost:8000/projects/2/scripts```


Which returns a JSON blob such as:

```json
{
    "id": 1,
    "project": 2,
    "script_text": "Some note for a project"
}
```
</details>

### Get a specific project script
<details>
    <summary>Expand</summary>

#### Via curl
```curl -X GET http://localhost:8000/projects/2/scripts/1```

Which returns a JSON blob such as:

```json
{
    "id": 1,
    "project": 2,
    "script_text": "Some note for a project"
}
```
</details>

### Update a specific project script
<details>
    <summary>Expand</summary>

#### Via curl
```curl -X PUT -H "Content-Type: application/json" -d "{\"id\": \"1\", \"project\": \"2\", \"script_text\": \"Some scripts for a project need updating\"}" http://localhost:8000/projects/2/scripts/1```

Which returns a JSON blob such as:

```json
{
    "id": 1,
    "project": 2,
    "note_text": "Some notes for a project need updating"
}
```
</details>

### Delete a specific project note
<details>
    <summary>Expand</summary>

#### Via curl
```curl -X DELETE http://localhost:8000/projects/2/notes/1```
</details>