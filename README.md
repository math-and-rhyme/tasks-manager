# Simple Task Tracker

The app is made for creating and storing tasks. 
Each task contains two fields: Title and Description.

## Current Version 0.0.1

- adding a new task from the Main page
- displaying all the tasks on a separate Tasks page

## How to run

Make sure Docker is installed.

Run the Bash script ```start.sh```
or run the line:
``` docker-compose up --build ```

## How to stop

Shutting down:
``` docker-compose down ```

# Learning Objectives

1. Practice connecting and working with a Postgres Database
2. Practice building several Docker containers and working with docker-compose
3. Understand the structure of a simple web app
4. Learn the handling of GET and POST requests in Flask

### Technologies and Tools Used

Database management:     PostgreSQL
Backend:                 Python (Flask)
Frontend:                HTML, CSS
Build:                   Docker, Bash

# Versions

### Version 0.0.1

- Basic feature of adding a new task
- Displaying all the tasks on a separate page

# Ideas to work on

- database storage (volumes, Docker)
- add tags for tasks
- add deletion and update features for the tasks
- show tasks in several columns
- intercative columns
- separate page for each card
- due dates