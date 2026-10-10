# Task Manager API
This API helps users create, list, update and delete tasks.

**Base URL** : http://localhost:8000/task_manager_api

## ENDPOINTS
### 1. List Tasks

* **Method:** `GET`
* **Path:** `/tasks`
* **Description:** Retrieves a list of all tasks.

**Example Request**

```http
GET /task_manager_api/tasks HTTP/1.1
```

**Example Response**
```json
{
  "tasks": [
    {
      "id": 1,
      "Title": "Create an API",
      "Completed": true
    },
    {
      "id": 2,
      "Title": "Learn python",
      "Completed": false
    }
  ]
}
```

**Success status code:** `200 Ok`
      
**Failure case**
`500 Internal Server Error` - An unexpected error occurred.

### 2. Get a Task

* **Method:** `GET`
* **Path:** `/tasks/{task_id}`
* **Description:** Retrieves a task using it's unique ID.

**Example Request**

```http
GET /task_manager_api/tasks/1 HTTP/1.1
```

**Example Response**
```json
{
  "id": 1,
  "Title": "Create an API",
  "Completed": true
}
```

**Success status code:** `200 Ok`
      
**Failure case**
`404 Not Found` - No task found with that ID.

### 3. Create a Task

* **Method:** `POST`
* **Path:** `/tasks`
* **Description:** Creates a new task.

**Example Request**

```http
POST /task_manager_api/tasks HTTP/1.1

{
  "id": 3,
  "Title": "Learn FastAPI",
  "Completed": false 
}
```

**Example Response**

```json
{
  "id": 3,
  "Title": "Learn FastAPI",
  "Completed": false 
}
```

**Success status code:** `201 Created`
      
**Failure case**
`400 Bad Request`
   
### 4. Update a Task

* **Method:** `PATCH`
* **Path:** `/tasks/{task_id}`
* **Description:** Updates a task.

**Example Request**

```http
PATCH /task_manager_api/tasks/3 HTTP/1.1

{
  "Completed": true
}
```

**Example Response**

```json
{
  "id": 3,
  "Title": "Learn FastAPI",
  "Completed": true
}
```

**Success status code:** `200 Ok`
      
**Failure case**
`404 Not Found` - No task found with that ID.
`500 Internal Server Error` - An unexpected error occurred.

### 5. Delete a Task

* **Method:** `DELETE`
* **Path:** `/tasks/{task_id}`
* **Description:** Deletes a task.

**Example Request**

```http
DELETE /task_manager_api/tasks/2 HTTP/1.1
```

**Example Response**

No response is returned.

**Success status code:** `204 No Content`
      
**Failure case**
`404 Not Found` - No task found with that ID.
`500 Internal Server Error` - An unexpected error occurred.







