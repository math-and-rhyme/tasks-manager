# use official PostgreSQL image as the base image
FROM postgres 
# setting environment variable for superuser password to access the db
ENV POSTGRES_PASSWORD=take-it-easy-123
# setting environment variable to specify the name of the db to be created
ENV POSTGRES_DB=tasks_db
ENV POSTGRES_USER: just_a_user
# copying the db initialization SQL script to a special directory
COPY init.sql /docker-entrypoint-initdb.d/
