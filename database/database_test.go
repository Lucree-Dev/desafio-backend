package database

import (
	"testing"

	"github.com/n0bode/desafio-backend/internal/models"
)

var (
	neocard models.CreditCard
)

func TestDatabaseConnection(t *testing.T) {
	//db = connectDB()
}

func TestAccountModel(t *testing.T) {
	obj := &models.Account{
		FirstName: "Forrest",
		LastName:  "Gump",
		Birthday:  "1944-06-06",
		Username:  "BubbaGump",
		Password:  "RunForrest",
		UserID:    "001",
	}

	/*	t.Run("Create", func(t0 *testing.T) {
		db.Create(&obj)
		db.Create(&models.Friend{
			UserID:   "001",
			FriendID: "010",
		})

		var friends []models.Friend
		db.Where("user_id = ?", obj.UserID).Find(&friends)
		fmt.Println(len(friends))
	})*/
}

// func TestCreditModel(t *testing.T) {
// 	card := &models.CreditCard{
// 		CardID:     "70c881d4a26984ddce795f6f71817c9cf4480e79",
// 		Title:      "Cartão 1",
// 		Pan:        "5527952393064634",
// 		ExpiryMM:   "03",
// 		ExpiryYYY:  "2022",
// 		SecuryCode: "656",
// 		Date:       "26/11/2015",
// 		UserID:     "70c881d4a26984ddce795f6f71817c9cf4480e79",
// 	}

// 	t.Run("Create", func(t0 *testing.T) {
// 		err := db.CreateTable((*models.CreditCard)(nil), &orm.CreateTableOptions{
// 			IfNotExists:   true,
// 			FKConstraints: true,
// 		})

// 		if err != nil {
// 			t0.Error("Error to Create Table")
// 		}
// 	})

// 	t.Run("Insert", func(t0 *testing.T) {
// 		err := db.Insert(card)

// 		if err != nil {
// 			t0.Error("Error to Insert on table")
// 		}
// 	})

// 	t.Run("Select All", func(t0 *testing.T) {
// 		var cards []models.CreditCard
// 		if err := db.Model(&cards).Select(); err != nil {
// 			t0.Error(err)
// 		}
// 		if len(cards) == 0 {
// 			t0.Error("Error Select All")
// 		}
// 	})

// 	t.Run("Update", func(t0 *testing.T) {
// 		resp, err := db.Model((*models.CreditCard)(nil)).Set("title = 'bubba'").Where("card_id = ?", card.CardID).Update()

// 		if err != nil {
// 			t0.Error(err)
// 		}

// 		if resp.RowsAffected() == 0 {
// 			t0.Fail()
// 		}
// 	})

// 	t.Run("Select Where", func(t0 *testing.T) {
// 		if err := db.Model(&neocard).Where("title = 'bubba'").Select(); err != nil {
// 			t0.Error(err)
// 		}

// 		fmt.Println(neocard)
// 		if card.CardID != neocard.CardID {
// 			t0.Fail()
// 		}
// 	})

// 	// t.Run("Delete", func(t0 *testing.T) {
// 	// 	res, err := db.Model(card).Where("card_id = ?", card.CardID).Delete()
// 	// 	if err != nil {
// 	// 		t0.Error(err)
// 	// 	}

// 	// 	if res.RowsAffected() == 0 {
// 	// 		t0.Error("Error to delete")
// 	// 	}
// 	// })

// }

// func TestTransferModel(t *testing.T) {

// 	transfer := &models.Transfer{
// 		FriendID:      "70c881d4a26984ddce795f6f71817c9cf4480e79",
// 		TotalToPay:    "100",
// 		BillingCardID: neocard.CardID,
// 		BillingCard:   &neocard,
// 		UserID:        neocard.UserID,
// 	}

// 	t.Run("Create", func(t0 *testing.T) {
// 		err := db.CreateTable((*models.Transfer)(nil), &orm.CreateTableOptions{
// 			FKConstraints: true,
// 		})

// 		if err != nil {
// 			t0.Error("Error to Create Table")
// 		}
// 	})

// 	t.Run("Insert", func(t0 *testing.T) {
// 		err := db.Insert(transfer)

// 		if err != nil {
// 			t0.Error("Error to Insert on table")
// 		}
// 	})

// 	t.Run("Select All", func(t0 *testing.T) {
// 		var transfers []models.Transfer
// 		if err := db.Model(&transfers).Select(); err != nil {
// 			t0.Error(err)
// 		}
// 		if len(transfers) == 0 {
// 			t0.Error("Error Select All")
// 		}
// 	})

// 	t.Run("Select Where", func(t0 *testing.T) {
// 		var ntransfer models.Transfer
// 		if err := db.Model(&ntransfer).Where("friend_id = ?", transfer.FriendID).Select(); err != nil {
// 			t0.Error(err)
// 		}

// 		fmt.Println(ntransfer)
// 	})

// }

// func TestDropAllTable(t *testing.T) {

// 	db.DropTable((*models.Friend)(nil), &orm.DropTableOptions{})
// 	if err := db.DropTable((*models.Account)(nil), &orm.DropTableOptions{
// 		Cascade: true,
// 	}); err != nil {
// 		t.Error(err)
// 	}
// 	db.Close()
// }
