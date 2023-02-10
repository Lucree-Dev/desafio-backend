CREATE DATABASE IF NOT EXISTS propig;

CREATE TABLE cards (
	id VARCHAR(255) PRIMARY KEY,
  	title VARCHAR(30),
  	pan VARCHAR(16),
  	expiry_mm VARCHAR(2),
  	expiry_yyyy VARCHAR(4),
  	security_code VARCHAR(3),
  	date VARCHAR(10),
  	owner_id VARCHAR(255),
  	FOREIGN KEY (owner_id) REFERENCES people(id)
);

CREATE TABLE people (
	id VARCHAR(255) PRIMARY KEY,
  	first_name VARCHAR(30),
  	last_name VARCHAR(15),
  	birthday VARCHAR(10),
  	password VARCHAR(255),
  	username VARCHAR(15) UNIQUE
);

CREATE TABLE transfers (
	id VARCHAR(255) PRIMARY KEY,
  	friend_id VARCHAR(255),
  	total_to_transfer INT,
  	billing_card VARCHAR(255),
  	FOREIGN KEY (billing_card) REFERENCES cards(id),
  	FOREIGN KEY (friend_id) REFERENCES people(id)
);

CREATE TABLE people_statement (
	id VARCHAR(255) PRIMARY KEY,
  	user_id VARCHAR(255),
  	transfer_id VARCHAR(255),
  	FOREIGN KEY (user_id) REFERENCES people(id),
  	FOREIGN KEY (transfer_id) REFERENCES transfers(id)
);