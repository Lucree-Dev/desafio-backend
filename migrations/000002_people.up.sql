CREATE TABLE IF NOT EXISTS people (
	id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
	first_name VARCHAR(100) NOT NULL,
	last_name VARCHAR(100) NOT NULL,
	birthday DATE NOT NULL,
	password VARCHAR(255) NOT NULL,
	username VARCHAR(100) NOT NULL,
	created_at TIMESTAMP DEFAULT NOW()
)
