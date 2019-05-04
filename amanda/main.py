# cibele RC
from _spy.vitollino.main import Cena, Elemento,Texto
transparente ="https://www.transparenttextures.com/patterns/debut-light.png"
def Historia():
	cena1 = Cena (img = "https://i.imgur.com/0mwf17P.png")
	gato = Elemento (img = transparente,
                      tit="Garfield",
                      style=dict(left=150, top=60, width=60, height=200))
	gato.entra(cenaHouse)
	txtGato = Texto (cenaHouse, "Hello")
	gato.vai = txtGato.vai
	cenaHouse.vai()
Historia()