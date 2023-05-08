package log

import (
	"os"

	"github.com/sirupsen/logrus"
)

func log() *logrus.Logger {
	logger := logrus.New()
	logger.SetFormatter(&logrus.JSONFormatter{})
	logger.SetOutput(os.Stdout)
	logger.SetLevel(logrus.InfoLevel) //TODO Parametrizar isto no arquivo application
	return logger
}

func Info(field string, value interface{}, message string) {
	log().WithFields(logrus.Fields{
		field: value,
	}).Info(message)
}

func InfoSimple(value interface{}) {
	log().Info(value)
}

func ErrorSimple(value interface{}) {
	log().Error(value)
}

func WarnSimple(value interface{}) {
	log().Warn(value)
}

func DebugSimple(value interface{}) {
	log().Debug(value)
}
