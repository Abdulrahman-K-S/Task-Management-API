# <p align='center'>Task-Management-API</p>

### Table of Contents
- [Description](#description)
- [State of Projet](#state-of-project)
- [Routes](#routes)
    - [Tasks](#tasks)
    - [Users](#users)
    - [Projects](#projects)
- [Author](#author)

# Description
Task Management API is an API that provides some functionalities for creating, managing, updating, and deleting tasks.

# Routes
This section is dedicated to the various endpoints in the program and what they require in the body to function.

## Tasks
The tasks route consists of 1 POST, 2 PUTS, 2 GET, and 1 DELETE.

Its attributes are:
```json
{
    "task_id": "3ac500f1-3cb5-4dae-94cb-867dc29ba099",
    "title": "Task #4",
    "description": "This is task #4",
    "status": "todo",
    "assigned_to": null,
    "deleted": "False"
}
```

### POST - http://localhost:5000/api/tasks/
The creation of the task. With this url we envoke the task POST endpoint which requires in it's body the following to work.
```json
{
    "title": "string",
    "description": "string",
    "status": "string",
    "assigned_to": "string"
}
```

### PUT - http://127.0.0.1:5000/api/tasks/{task_id}
The 1st PUT endpoint of the task model is to update a certain feild in the task file in redis where we need to specifiy the id of the task to be modifed and a body to indicate it's modifed attributes

```json
{
    "status": "on going"
}
```

### PUT - http://127.0.0.1:5000/api/tasks/{task_id}/{user_id}
The 2nd PUT endpoint of the task model is to assign a user to a specific task which both are inputed through the URL to the program.

Which it changes the `assigned_to` attribute inside the task from `None` to the `user_id`.

### GET - http://127.0.0.1:5000/api/tasks/
The 1st GET endpoint of the task model gets all the possible tasks inside the redis database.

This is possible as I modeled the database to seperate the entities into their own folders and return the ids of those folders when querying. (Check [redis_client.py](./app/utils/redis_client.py) and look for the get_all_with_prefix method)

### GET - http://127.0.0.1:5000/api/tasks/{task_id}
The 2nd GET endpoint of the task model gets all the attributes of a certain task that is inputed to the program through the URL.

### DELETE - http://127.0.0.1:5000/api/tasks/{task_id}
The DELETE endpoitn takes in a task id and marks the `deleted` attribute of the task to True.

This is done to simulate that the task is deleted since I didn't want it to be hard deleted rather soft deleted.

## Users
The users route consists of 1 POST, 1 PUT, 3 GET, and 1 DELETE.

Its attributes are:
```json
{
    "user_id": "c7d5dead-1baf-442e-a782-3274f715215e",
    "name": "Abdulrahman Khaled",
    "email": "test@email.com",
    "password": "12345",
    "deleted": "False"
}
```

### POST - http://localhost:5000/api/users/
The creation of the user. With this url we envoke the user POST endpoint which requires in it's body the following to work.

```json
{
  "name": "Abdulrahman Khaled",
  "email": "test@email.com",
  "password": "12345"
}
```

### PUT - http://localhost:5000/api/users/{user_id}
To update the user attributes we invoke this endpoint specifing the user_id of the user we want to update its attributes and in the body we specify the attributes to be updates.

```json
    "email": "test@outlook.com"
```

### GET - http://localhost:5000/api/users/
The 1st GET endpoint of the users gets all the users that are in the redis system using the same technique mentioned in the tasks GET endpoint.

### GET - http://localhost:5000/api/users/{user_id}
The 2nd GET endpoint of the users gets all the information of a specific user which it's ID is passed through the URL

### GET - http://localhost:5000/api/users/{user_id}/tasks
The 3rd GET endpoint of the users gets all the tasks a certain user is assigned to along with their details.

### DELETE - http://localhost:5000/api/users/{user_id}
As for the DELETE endpoint of the users it just marks the `deleted` attribute to `True` which simulates that a user has been deleted. 


## Projects
The projects route consists of 1 POST, 2 PUT, 3 GET, and 1 DELETE.

Its attributes are:
```json
{
    "project_id": "052c1e57-c17e-4082-b353-487256d64217",
    "name": "Task Management API",
    "description": "An api that facilitates tasks for people & projects",
    "status": "active",
    "deleted": "False",
    "task_ids": []
}
```

### POST - http://localhost:5000/api/projects/
The creation of the project. With this url we envoke the project POST endpoint which requires in it's body the following to work.

```json
{
  "name": "Task Management API",
  "description": "An api that facilitates tasks for people & projects",
  "status": "string",
  "task_id": [
    "string"
  ]
}
```

Although the status & task_id could be left to string and it won't be added until you envoke the 2nd PUT endpoint to add to the task_id list while the status will be turned to `active` by default

### PUT - http://localhost:5000/api/projects/{project_id}
The 1st PUT endpoint of the projects routes updates the attributes of a specific project that it's `project_id` is passed to the URL if it's present.

### PUT - http://localhost:5000/api/projects/{project_id}/{task_id}
The 2nd PUT endpoint of the projects routes updates the `task_id list` attribute in the porject adding the `task_id` to the list if it's not already in it.

### GET - http://localhost:5000/api/projects/
The 1st GET endpoint in the projects routes retrieves all the projects that are present inside the redis DB using the same method talked about above.

### GET - http://localhost:5000/api/projects/{project_id}
The 2nd GET endpoint in the projects routes retrieves all the info regarding the entered `project_id` if it's present & not deleted.

### GET - http://localhost:5000/api/projects/{project_id}/tasks
The 3rd GET endpoint in the projects routes retireves all the tasks that are inside the project task list.

### DELETE - http://localhost:5000/api/projects/{project_id}
The DELETE endpoint marks the passed `project_id` `deleted` attribute to `True` which simulates it being deleted from the database.

# State of Project
This section outlines the current limitations and future plans for the project. Currently, authentication is minimal and will be improved in future iterations.

# Author
@Abdulrahman Khaled - AK-Salah@outlook.com