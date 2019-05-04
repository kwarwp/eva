# cibele RC
from _spy.vitollino.main import Cena, Elemento,Texto
transparente ="https://www.transparenttextures.com/patterns/debut-light.png"
def Historia():
	cena1 = Cena (img = "https://i.imgur.com/0mwf17P.png")
	gato = Elemento (img = transparente,
                      tit="Robinson Crusoe",
                      style=dict(left=150, top=60, width=60, height=200))
	gato.entra(cena1)
	txtGato = Texto (cena1, "The dream of Robinson Crusoe's life was to get out of the city into the sea. But he was dissatisfied with this.Then he saw a friend that the father had a ship and so I decided to sail to London with them. During the trip there was a storm and the RC was very sickly thinking about giving up, but the next day was calm and went on a trip to London. He spent a period in London and made a trip to Africa, but a Turkish pirate ship took ours and made us slaves. For more information, visit our Turkish scanning page.")
	gato.vai = txtGato.vai
	cena1.vai()
Historia()