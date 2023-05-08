CREATE TABLE payments (
    id SERIAL PRIMARY KEY,
    friend_id INTEGER NOT NULL,
    people_id INTEGER NOT NULL,
    card_id INTEGER NOT NULL,
    value DECIMAL,
    date DATE,
    FOREIGN KEY(friend_id) REFERENCES people(id),
    FOREIGN KEY(card_id) REFERENCES cards(id),
    FOREIGN KEY(people_id) REFERENCES people(id)
);
