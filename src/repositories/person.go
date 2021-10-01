package repositories

import (
	"database/sql"
	"lucree/src/models"
)

type Person struct {
	db *sql.DB
}

// Create a person repository
func NewRepositoryPerson(db *sql.DB) *Person {
	return &Person{db}
}

func (p Person) Create(person models.Person) (int64, error) {
	statement, err := p.db.Prepare(
		"INSERT INTO persons (first_name, last_name, birthday, password, username) VALUES (?, ?, ?, ?, ?)")

	if err != nil {
		return 0, err
	}

	defer statement.Close()

	result, err := statement.Exec(person.First_name, person.Last_name, person.Birthday, person.Password, person.Username)

	if err != nil {

		return 0, err
	}

	id, err := result.LastInsertId()
	if err != nil {
		return 0, err
	}

	return int64(id), nil
}

func (p Person) PersonByUsername(username string) (models.Person, error) {
	line, err := p.db.Query("SELECT user_id, password from persons where username = ?", username)

	if err != nil {
		return models.Person{}, err
	}

	defer line.Close()

	var person models.Person
	if line.Next() {
		if err = line.Scan(&person.User_id, &person.Password); err != nil {
			return models.Person{}, err
		}
	}

	return person, nil
}

func (p Person) GetFriends(personID uint64) ([]models.Person, error) {
	lines, err := p.db.Query(`SELECT first_name, last_name, birthday, username from persons inner join friends on friends.person_id = persons.user_id
		where friends.friend_id = ? `, personID,
	)

	if err != nil {
		return nil, err
	}

	defer lines.Close()

	var persons []models.Person
	for lines.Next() {
		var person models.Person

		if err = lines.Scan(
			&person.First_name,
			&person.Last_name,
			&person.Birthday,
			&person.Username,
		); err != nil {
			return nil, err
		}

		persons = append(persons, person)
	}
	return persons, nil
}
