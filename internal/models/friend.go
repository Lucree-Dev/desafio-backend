package models

import "github.com/jinzhu/gorm"

type Friend struct {
	gorm.Model
	UserID   string  `gorm:"type:varchar(128)"`
	FriendID string  `gorm:"type:varchar(128);index"`
	Friend   Account `gorm:"foreignkey:UserID;association_foreignkey:FriendID"`
}
