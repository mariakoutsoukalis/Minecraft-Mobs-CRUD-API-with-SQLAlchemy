# Minecraft Mobs API w/ SQLAlchemy Overview

This API provides access to a database of Minecraft mobs to perform CRUD operations. The script includes functions for connecting to, creating, and managing a SQLite database using SQLAlchemy as an ORM for mob data.

## Dependencies
- Flask
- Flask-Migrate
- Flask-SQLAlchemy
- SQLite3

## Running the Application
After setting up with `pipenv install`, execute `app.py` to run the Flask app. The API will be available at `http://127.0.0.1:5000`.

## Endpoints

### Home
- **Endpoint:** `/`
- **Method:** GET
- **Description:** Welcome message from the API.

### API Access
- **Endpoint:** `/api`
- **Method:** GET
- **Description:** Information about supported requests.

### Get All Mobs
- **Endpoint:** `/api/mobs`
- **Method:** GET
- **Description:** Retrieve data for all mobs.

### Get Mob by ID
- **Endpoint:** `/api/mobs/<int:mob_id>`
- **Method:** GET
- **Description:** Retrieve data for a specific mob by ID.

### Add New Mob
- **Endpoint:** `/api/mobs`
- **Method:** POST
- **Description:** Add a new mob to the database.

### Update Mob
- **Endpoint:** `/api/mobs/<int:mob_id>`
- **Method:** PATCH
- **Description:** Update data for a specific mob.

### Delete Mob
- **Endpoint:** `/api/mobs/<int:mob_id>`
- **Method:** DELETE
- **Description:** Delete a specific mob from the database.

## Error Handling

### Error: 404 Not Found
- **Description:** Handling for resource not found.

## Seeding the Database
Use `seed.py` to seed the database with initial mob data.

## Lab Led by https://github.com/djprofessorkash