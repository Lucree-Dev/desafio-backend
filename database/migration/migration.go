package migration

import (
	"fmt"
	"log"

	"github.com/n0bode/desafio-backend/internal/models"
	"github.com/n0bode/desafio-backend/internal/util"

	re "gopkg.in/rethinkdb/rethinkdb-go.v6"
)

func MakeMigration(db *re.Session) {
	if err := re.DBCreate(util.GetEnv("DATABASE_NAME", "lucree")).Exec(db); err != nil {
		return
	}
	log.Println("Make migrations")

	log.Println("Creating Accounts Table")
	re.TableCreate("accounts", re.TableCreateOpts{
		PrimaryKey: "user_id",
	}).Exec(db)

	//Inserting sample accounts test row
	re.Table("accounts").Insert([]models.Account{
		models.Account{
			UserID:    util.EncodeToSha256("Godfather"),
			Username:  "VitoCorleone",
			Password:  util.EncodeToSha256("Corleone"),
			FirstName: "Vito",
			LastName:  "Corleone",
			Birthday:  "1887-04-29",
		},
		models.Account{
			UserID:    util.EncodeToSha256("Fuck My Ass"),
			Username:  "Tony",
			Password:  util.EncodeToSha256("Montana"),
			FirstName: "Tony",
			LastName:  "Montana",
			Birthday:  "1960-08-28",
		},
		models.Account{
			UserID:    util.EncodeToSha256("RunForrest!"),
			Username:  "Forrest",
			Password:  util.EncodeToSha256("Gump"),
			FirstName: "Forrest",
			LastName:  "Gump",
			Birthday:  "1944-06-06",
		},
	}).Exec(db)

	log.Println("Creating CreditCards Table")
	re.TableCreate("creditcards", re.TableCreateOpts{
		PrimaryKey: "card_id",
	}).Exec(db)

	//Inserting samples credit cards
	re.Table("creditcards").Insert(
		models.CreditCard{
			UserID:       util.EncodeToSha256("RunForrest!"),
			CardID:       util.EncodeToSha256("0000"),
			Title:        "Cartão Teste",
			SecurityCode: "988",
			Pan:          "00000000000000000",
			ExpiryMM:     "02",
			ExpiryYYYY:   "2022",
			Date:         "23/02/2027",
		},
	).Exec(db)

	log.Println("Creating Friends Table")
	re.TableCreate("friends").Exec(db)

	//Creating secundary key
	re.Table("friends").IndexCreate("user_id").Exec(db)

	//Inserting samples friends
	re.Table("friends").Insert([]models.Friend{
		models.Friend{
			UserID:   util.EncodeToSha256("RunForrest!"),
			FriendID: util.EncodeToSha256("GodFather"),
		},
		models.Friend{
			UserID:   util.EncodeToSha256("RunForrest!"),
			FriendID: util.EncodeToSha256("Fuck My Ass"),
		},
	}).Exec(db)

	log.Println("Creating Transfers Table")
	re.TableCreate("transfers").Exec(db)
	re.Table("transfers").Insert([]models.Transfer{
		models.Transfer{
			UserID:     util.EncodeToSha256("GodFather"),
			FriendID:   util.EncodeToSha256("Fuck My Ass"),
			TotalToPay: 150,
			BillingCard: &models.BillingCard{
				CardID: util.EncodeToSha256("0000"),
			},
		},
		models.Transfer{
			UserID:     util.EncodeToSha256("Fuck My Ass"),
			FriendID:   util.EncodeToSha256("RunForrest!"),
			TotalToPay: 980,
			BillingCard: &models.BillingCard{
				CardID: util.EncodeToSha256("0000"),
			},
		},
	}).Exec(db)
	fmt.Println("MADE MIGRATION")
}
