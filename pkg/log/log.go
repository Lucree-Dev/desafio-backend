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

func Info(message string) {
	log().Info(message)
}

func Error(message string) {
	log().Error(message)
}

func Warn(message string) {
	log().Warn(message)
}

func Debug(message string) {
	log().Debug(message)
}
