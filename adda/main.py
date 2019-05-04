# Luana RC
from _spy.vitollino.main import Cena, Elemento,Texto
transparente ="https://www.transparenttextures.com/patterns/debut-light.png"
def Historia():
	cena4 = Cena (img = "https://i.imgur.com/K2S15Bz.png")
	pequenasereia = Elemento (img = transparente,
                               tit="Mar",
                               style=dict(left=30, top=60, width=180, height=100))
	pequenasereia.entra(cenaFundodomar)
	txtpequenasereia = Texto (cenaFundodomar, "Hello")
	pequenasereia.vai = txtpequenasereia.vai()
	cenaFundodomar.vai()
Historia()