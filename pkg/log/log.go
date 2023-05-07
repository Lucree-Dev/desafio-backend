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

func Info(value interface{}) {
	log().Info(value)
}

func Error(value interface{}) {
	log().Error(value)
}

func Warn(value interface{}) {
	log().Warn(value)
}

func Debug(value interface{}) {
	log().Debug(value)
}
