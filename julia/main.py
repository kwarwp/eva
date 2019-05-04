# michelle
from _spy.vitollino.main import Cena, Elemento, Texto
transparente ="https://www.transparenttextures.com/patterns/debut-light.png "
def Historia():
	cena2 = Cena (img = "https://i.imgur.com/wQmMx4O.png")
	faniquita = Elemento (img = transparente,
                           tit="Robinson Crusoe",
                           style=dict(left=70, top=60, width=100, height=60))
	faniquita.entra(cena2)
	txtfaniquita = Texto (cena2, "
For two years I lived a slave life, until I managed to escape using a fishing boat. But I was still in Africa, afraid of animals and the dangers that could be there. He was drifting for a while until being rescued by a Portuguese ship that took him to Brazil")
	faniquita.vai = txtfaniquita.vai
	cena2.vai()
Historia()