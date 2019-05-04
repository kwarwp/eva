# Lucimara
from _spy.vitollino.main import Cena, Elemento, Texto
transparente ="https://www.transparenttextures.com/patterns/debut-light.png"
def Historia():
	cena3 = Cena (img = "https://i.imgur.com/I2u7XCz.png")
	moana = Elemento (img = transparente, 
                       tit="Robinson Crusoe",
                       style=dict(left=10, top=60,  Width=60, height=50))
	moana.entra(cena3)                       
	txtmoana = Texto (cena3, "For two years I lived a slave life, until I managed to escape using a fishing boat. But I was still in Africa, afraid of animals and the dangers that could be there. He was drifting for a while until being rescued by a Portuguese ship that took him to Brazil.")
	moana.vai = txtmoana.vai
	cena3.vai ()
Historia()# eva.sarah.main.py