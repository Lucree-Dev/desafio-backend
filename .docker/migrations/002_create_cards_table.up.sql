CREATE TABLE cards (
    id SERIAL PRIMARY KEY,
    title VARCHAR(50),
    pan VARCHAR(50),
    expiry_mm VARCHAR(2),
    expiry_yyyy VARCHAR(4),
    security_code VARCHAR(255),
    date DATE,
    people_id INTEGER NOT NULL,
    FOREIGN KEY(people_id) REFERENCES people(id)
);