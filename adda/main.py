# Luana RC
from _spy.vitollino.main import Cena, Elemento,Texto
transparente ="https://www.transparenttextures.com/patterns/debut-light.png"
def Historia():
	cena4 = Cena (img = "https://i.imgur.com/K2S15Bz.png")
	pequenasereia = Elemento (img = transparente,
                               tit="Mar",
                               style=dict(left=30, top=60, width=180, height=100))
	pequenasereia.entra(cena1)
	txtpequenasereia = Texto (cena1, "Hello")
	pequenasereia.vai = txtpequenasereia.vai()
	cena1.vai()
Historia()