#Felipe RC
from _spy.vitollino.main import Cena, Elemento, Texto 
transparente ="https://www.transparenttextures.com/patterns/debut-light.png"
def Historia():
	cena2 = Cena (img = "https://i.imgur.com/wQmMx4O.png")
	mickey = Elemento (img = transparente,
                        tit="Robinson Crusoe",
                        style=dict(left=20, top=60, width=150, height=500))
	mickey.entra(cena2)
	txtMickey = Texto (cena2, "For two years I lived a slave life, until I managed to escape using a fishing boat. But I was still in Africa, afraid of animals and animals that exist there. He was adrift for a time until he was rescued by a Portuguese ship that was taking him to Brazil.")
	mickey.vai = txtMickey.vai
	cena2.vai()
Historia()