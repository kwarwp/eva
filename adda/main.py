# Luana RC
from _spy.vitollino.main import Cena, Elemento,Texto
transparente ="https://www.transparenttextures.com/patterns/debut-light.png"
def Historia():
	cena4 = Cena (img = "https://i.imgur.com/K2S15Bz.png")
	pequenasereia = Elemento (img = transparente,
                               tit="Robinson Crusoe",
                               style=dict(left=30, top=60, width=180, height=100))
	pequenasereia.entra(cena4)
	txtpequenasereia = Texto (cena4, "By morning the sea was calmer, and to my surprise the ship was there, so I swam to it and managed to get through a hole. A part of the ship was out of the water just where the food was and I took some food to the beach, along with the food I also took knives and other tools that I found on the ship. I decided to build a small house so I used the woods and sails of the ship, I went back a few times to get some things but after a few days there was a big storm and the ship disappeared into the sea. I was happy because despite being alone on the island I was alive and with tools and food.")
	pequenasereia.vai = txtpequenasereia.vai()
	cena4.vai()
Historia()