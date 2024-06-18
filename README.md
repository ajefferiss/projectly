# projectly
Simple API to create and manage "projects". A project includes notes and scripts, as well as a simple calendar to track when things should get done.

## Quick Install
Install the requirements listed in `requirements.txt`:
`python -m pip install -r requirements.txt`
## Run locally
To run the Django API you can simply run: `python manage.py runserver`
## Testing Endpoints
For the current endpoints, see [openapi-schema.yaml](./openapi-schema.yaml).
### Get all projects
<details>
    <summary>Expand</summary>

#### Via curl
```curl -H GET http://localhost:8000/projects/```

Which returns a JSON blob such as:

```json
[
    {
        "id":2,
        "name_text":"Another project", 
        "pub_date":"2024-06-18T15:52:08Z"
    },
    {
        "id":1,
        "name_text":"New Project",
        "pub_date":"2024-06-18T15:36:08Z"
    },
    {
        "id":3,
        "name_text":"Old Project",
        "pub_date":"2024-04-01T15:52:33Z"
    }
]
```
</details>

### Get specific project
<details>
    <summary>Expand</summary>

#### Via curl
```curl -H GET http://localhost:8000/projects/1/```

Which returns a JSON blob such as:

```json
{
    "id":1,
    "name_text":"New Project",
    "pub_date":"2024-06-18T15:36:08Z"
}
```
</details>

### Get all notes for a project
<details>
    <summary>Expand</summary>

#### Via curl
```curl -H GET http://localhost:8000/projects/1/notes/```

Which returns a JSON blob such as:

```json
[
    {
        "id":1,
        "project":1,
        "note_text": "One"
    },
    {
        "id":2,
        "project":1,
        "note_text":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus facilisis tortor in ultrices efficitur. In felis justo, mollis at vehicula sit amet, auctor et lacus. Mauris rutrum, enim congue hendrerit tristique, sem turpis pretium mauris, iaculis vehicula dolor ligula ac turpis. Sed nulla ipsum, facilisis eu quam vel, scelerisque iaculis leo. Aenean rutrum fringilla lectus a volutpat. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos."
    }
]
```
</details>

### Get a specific project note
<details>
    <summary>Expand</summary>

#### Via curl
```curl -H GET http://localhost:8000/projects/1/notes/1/```

Which returns a JSON blob such as:

```json
{
    "id":1,
    "project":1,
    "note_text": "One"
}
```
</details>