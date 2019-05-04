# cibele RC
from _spy.vitollino.main import Cena, Elemento,Texto
trasparente ="https://www.transparenttextures.com/patterns/debut-light.png"
def Historia():
	cenaHouse = Cena (img = "https://www.simsnetwork.com/sites/simsnetwork.com/files/styles/box-downloads/public/20140218-downloads-arbuckle-03.jpg?itok=TcZfhuU-")
	gato = Elemento (img = linkDoGato,
                      tit="Garfield",
                      style=dict(left=150, top=60, width=60, height=200))
	gato.entra(cenaHouse)
	txtGato = Texto (cenaHouse, "Hello")
	gato.vai = txtGato.vai
	cenaHouse.vai()
Historia()