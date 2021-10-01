package repositories

import (
	"database/sql"
	"lucree/src/models"
)

type Card struct {
	db *sql.DB
}

// Create a Card repository
func NewRepositoryCard(db *sql.DB) *Card {
	return &Card{db}
}

func (c Card) Create(card models.Card) (int64, error) {
	statement, err := c.db.Prepare(
		"INSERT INTO cards (person_id, title, pan, expiry_mm, expiry_yyy, security_code, date) VALUES (?, ?, ?, ?, ?, ?, ?)")

	if err != nil {
		return 0, err
	}

	defer statement.Close()

	result, err := statement.Exec(card.Person_ID, card.Title, card.Pan, card.Expiry_mm, card.Expiry_yyy, card.Security_code, card.Date)

	if err != nil {

		return 0, err
	}

	id, err := result.LastInsertId()
	if err != nil {
		return 0, err
	}

	return int64(id), nil
}

func (c Card) GetAll(personID uint64) ([]models.Card, error) {

	lines, err := c.db.Query(
		"SELECT card_id, title, pan, expiry_mm, expiry_yyy, security_code, date from cards where person_id = ?", personID,
	)

	if err != nil {
		return nil, err
	}

	defer lines.Close()

	var cards []models.Card
	for lines.Next() {
		var card models.Card

		if err = lines.Scan(
			&card.Card_ID,
			&card.Title,
			&card.Pan,
			&card.Expiry_mm,
			&card.Expiry_yyy,
			&card.Security_code,
			&card.Date,
		); err != nil {
			return nil, err
		}

		cards = append(cards, card)
	}
	return cards, nil
}
