# cibele
from _spy.vitollino.main import Cena, Elemento,Texto
linkDoGato ="https://vignette.wikia.nocookie.net/character-stats-and-profiles/images/0/09/Garfield.png/revision/latest?cb=20170701143047"
def Historia():
	cenaHouse = Cena (img = "https://www.simsnetwork.com/sites/simsnetwork.com/files/styles/box-downloads/public/20140218-downloads-arbuckle-03.jpg?itok=TcZfhuU-")
	gato = Elemento (img = linkDoGato,
                      tit="Garfield",
                      style=dict(left=150, top=60, width=60, height=200))
	gato.entra(cenaHouse)
	txtGato = Texto (cenaHouse, "Hello")
	
	cenaHouse.vai()
Historia()