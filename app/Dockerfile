# use official Python 3.9 image as the base image for the container
FROM python:3.9
# setting the environment vraiable in the Dockerfile 
#   to ensure that Flask recognizes the app when using 'flask run' command
ENV FLASK_APP=app.py
# setting the working directory in the container
WORKDIR /app
# copying file from cuurent directory to the working directory in the container
COPY requirements.txt .
# installing all (-r) the python packages specified in the .txt file
RUN pip install -r requirements.txt
# copyting all the other files
COPY . .
# flask -- calls flask command-line interface
# run -- tells the flask to start the developement server
# "--host=0.0.0.0" -- will make it visible, for other devices on the network
# "--port=8000" to avoid conflicts, port==5000 by default
CMD ["flask", "run", "--host=0.0.0.0"]