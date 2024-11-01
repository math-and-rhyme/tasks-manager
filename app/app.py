# *************************************************************
#           importing 
#               the Flask class, the jsonify function, the request object
#               the render_template function
#               the psycopg2 lib for PostgreSQL database connection
#               the os lib for accessing environment variables
# *************************************************************

from flask import Flask, jsonify, request, render_template
import psycopg2
import os


# *************************************************************
#           creating an instance of a Flask class
# *************************************************************

app = Flask(__name__)


# *************************************************************
#           function for connecting to the database
# *************************************************************

def connect_db():
    # creating a connection object using psycopg2 library
    connection_obj = psycopg2.connect(dbname=os.environ['POSTGRES_DB'], user=os.environ['POSTGRES_USER'],password=os.environ['POSTGRES_PASSWORD'],host='db')
    return connection_obj


# *************************************************************
#           getting all the tasks and displaying them.
#               using the HTTP GET method
# *************************************************************

@app.route("/tasks", methods=["GET"])
def get_tasks():

    # establish the conenction with db, using an object from funcrion connect_db
    connection = connect_db()

    # cretaing a cursor object to execute SQL queries and fetch results of them
    cur = connection.cursor() 

    # execute a SQL command to get all the tasks
    cur.execute("SELECT * FROM tasks_table;")

    # fetch all the rows we got from an executed query 
    tasks_data = cur.fetchall()

    # each row is a list of tuples, where each tuple == one row
    #   converting it into a list of dictionaries for JSON serialiazation
    tasks_list = [dict(zip(['id', 'title', 'info', 'done'], task)) for task in tasks_data]

    # closing the cursor
    cur.close()

    # closing the database connection
    connection.close()

    # render a page displaying the tasks
    return render_template("tasks.html", tasks_data=tasks_list)


# *************************************************************
#           defining a route for adding a new tasks
# *************************************************************

@app.route('/', methods=['GET'])
def index():
    # returning rendered page with passed tasks to the html template
    return render_template("index.html")


# *************************************************************
#           adding a new task.
#               using the HTTP POST method and form
# *************************************************************

@app.route("/", methods=["POST"])
def add_task():
    title = request.form['title']
    info = request.form.get('info', '')
    connection = connect_db()
    cur = connection.cursor()
    cur.execute("INSERT INTO tasks_table (title, info) VALUES (%s, %s);", (title, info))
    connection.commit()
    cur.close()
    connection.close()
    # message = {"message": "Task created successfully"}
    message = "Task created successfully"
    return render_template("index.html", status_message=message)


# *************************************************************
#           defining a route to display the About page
# *************************************************************

@app.route("/about")
def about():
  return render_template("about.html")