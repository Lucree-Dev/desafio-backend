CREATE TABLE people (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    birthday DATE,
    password VARCHAR(255),
    username VARCHAR(50)
);