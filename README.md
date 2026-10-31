# Task Manager API
The Task Manager API is designed to provide a way for users to manage their tasks efficiently. It defines endpoints that allow clients to create, retrieve, update, and delete tasks.

## Features
* Retrieve a list of tasks.
* Retrieve a single task by its ID.
* Create new tasks.
* Update existing tasks.
* Delete tasks.

## Database Migrations
This project uses **Alembic** to manage database schema changes.

After installing the project dependencies, run the following command to apply all migrations:

\```bash
alembic upgrade head
\```

This creates the database tables and applies any pending schema changes.

To check the current migration version, run:

\```bash
alembic current
\```

### Database Relationships
The project implements a one-to-many relationship between Users and Tasks.

- A user can have multiple tasks.
- A task can belong to one user.
- The `user_id` column in the `tasks` table is a foreign key referencing `users.id`.
- The `user_id` column is nullable, allowing existing tasks to remain unassigned.

### User Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/task-manager-api/users` | Create a user |
| POST | `/task-manager-api/users/{user_id}/tasks` | Create a task for a user |
| GET | `/task-manager-api/users/{user_id}` | Retrieve a user and their tasks |