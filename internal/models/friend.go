package models

type Friend struct {
	UserID   string `rethinkdb:"user_id"`
	FriendID string `rethinkdb:"friend_id"`
}
