#Felipe
from _spy.vitollino.main import Cena, Elemento, Texto 
linkDoMickey ="https://i.pinimg.com/originals/57/dc/a9/57dca93157d27dd05ef7657c4c0ba07a.png"
def Historia():
	cenaParque = Cena (img = "http://starkovtattoo.spb.ru/images/400/DSC100466834.jpg")
	mickey = Elemento (img = linkDoMickey,
                        tit="Mickey",
                        style=dict(left=110, top=60, width=60, height=200))
	mickey.entra(cenaParque)
	cenaParque.vai()
Historia()