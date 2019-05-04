# michelle
from _spy.vitollino.main import Cena, Elemento, Texto
transparente ="https://www.transparenttextures.com/patterns/debut-light.png "
def Historia():
	cenaFeliz = Cena (img = "https://i.imgur.com/wQmMx4O.png")
	faniquita = Elemento (img = transparente,
                           tit="Faniquita",
                           style=dict(left=70, top=60, width=100, height=60))
	faniquita.entra(cena1)
	txtfaniquita = Texto (cena1, "Hello")
	faniquita.vai = txtfaniquita.vai
	cena1.vai()
Historia()