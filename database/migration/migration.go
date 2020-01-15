package migration

import (
	"log"

	"github.com/spf13/viper"
	re "gopkg.in/rethinkdb/rethinkdb-go.v6"

	"github.com/go-pg/pg"
)

func addTesters(db *pg.DB) {

}

func MakeMigration(db *re.Session) {
	if err := re.DBCreate(viper.GetString("database.dbname")).Exec(db); err != nil {
		return
	}

	log.Println("Creating Accounts Table")
	re.TableCreate("accounts").Exec(db)
	re.Table("accounts").IndexCreate("user_id").Exec(db)

	log.Println("Creating CreditCards Table")
	re.TableCreate("creditcards").Exec(db)
	re.Table("creditcards").IndexCreate("card_id").Exec(db)

	log.Println("Creating Friends Table")
	re.TableCreate("friends").Exec(db)

	log.Println("Creating Transfers Table")
	re.TableCreate("transfers").Exec(db)
}
