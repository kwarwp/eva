#Felipe RC
from _spy.vitollino.main import Cena, Elemento, Texto 
transparente ="https://www.transparenttextures.com/patterns/debut-light.png"
def Historia():
	cenaParque = Cena (img = "http://starkovtattoo.spb.ru/images/400/DSC100466834.jpg")
	mickey = Elemento (img = transparente,
                        tit="Mickey",
                        style=dict(left=20, top=60, width=150, height=500))
	mickey.entra(cenaParque)
	txtMickey = Texto (cenaParque, "Hello")
	mickey.vai = txtMickey.vai
	cenaParque.vai()
Historia()