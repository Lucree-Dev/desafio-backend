package server

func Start() {
	RegisterEndPoints().Start(":8080") //TODO pegar a porta definida no arquivo application
}
