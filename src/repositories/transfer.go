package repositories

import (
	"database/sql"
	"lucree/src/models"
)

type Transfer struct {
	db *sql.DB
}

// Create a Transfer repository
func NewRepositoryTransfer(db *sql.DB) *Transfer {
	return &Transfer{db}
}

func (t Transfer) Create(transfer models.Transfer) (int64, error) {
	statement, err := t.db.Prepare(
		"INSERT INTO transfer (friend_id, total_to_pay, card_id) VALUES (?, ?, ?)")

	if err != nil {
		return 0, err
	}

	defer statement.Close()

	result, err := statement.Exec(transfer.Friend_id, transfer.Total_to_pay, transfer.BillingCard.Card_id)

	if err != nil {

		return 0, err
	}

	id, err := result.LastInsertId()
	if err != nil {
		return 0, err
	}

	return int64(id), nil
}

func (t Transfer) GetAll() ([]models.Transfer, error) {
	lines, err := t.db.Query(`SELECT cards.person_id, transfer.friend_id, transfer.total_to_pay, transfer.date, cards.card_id FROM transfer inner join
	cards on cards.card_id = transfer.card_id `,
	)

	if err != nil {
		return nil, err
	}

	defer lines.Close()

	var transfers []models.Transfer
	for lines.Next() {
		var transfer models.Transfer

		if err = lines.Scan(
			&transfer.User_id,
			&transfer.Friend_id,
			&transfer.Value,
			&transfer.Date,
			&transfer.BillingCard.Card_id,
		); err != nil {
			return nil, err
		}

		transfers = append(transfers, transfer)
	}
	return transfers, nil
}

func (t Transfer) getTransferByUser(userId uint64) ([]models.Transfer, error) {
	lines, err := t.db.Query(`SELECT cards.person_id, transfer.friend_id, transfer.total_to_pay, transfer.date, cards.card_id FROM transfer inner join
	cards on cards.card_id = transfer.card_id where cards.person_id = ? `, userId)

	if err != nil {
		return nil, err
	}

	defer lines.Close()

	var transfers []models.Transfer
	for lines.Next() {
		var transfer models.Transfer

		if err = lines.Scan(
			&transfer.User_id,
			&transfer.Friend_id,
			&transfer.Value,
			&transfer.Date,
			&transfer.BillingCard.Card_id,
		); err != nil {
			return nil, err
		}

		transfers = append(transfers, transfer)
	}
	return transfers, nil
}
