#Felipe RC
from _spy.vitollino.main import Cena, Elemento, Texto 
transparente ="https://www.transparenttextures.com/patterns/debut-light.png"
def Historia():
	cena2 = Cena (img = "https://i.imgur.com/wQmMx4O.png")
	mickey = Elemento (img = transparente,
                        tit="Mickey",
                        style=dict(left=20, top=60, width=150, height=500))
	mickey.entra(cena2)
	txtMickey = Texto (cena2, "Hello")
	mickey.vai = txtMickey.vai
	cena2.vai()
Historia()