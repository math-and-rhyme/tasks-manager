-- Create the tasks_table
CREATE TABLE tasks_table (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    info TEXT,
    done BOOLEAN DEFAULT FALSE
);

-- Insert data into tasks_table
INSERT INTO tasks_table (title, info) VALUES ('Task 1', 'Feed the fish');
INSERT INTO tasks_table (title, info) VALUES ('Task 2', 'Feed the cat');

-- serial: automatically generates a unique integer value for each new row inserted
-- primary key: for unique identification