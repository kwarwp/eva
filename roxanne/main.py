# michelle
from _spy.vitollino.main import Cena, Elemento, Texto
linkFaniquita ="https://i.pinimg.com/originals/53/48/7d/53487d3650ef3eb22f3c8f29ad1e09a9.png"
def Historia():
	cenaFeliz = Cena (img = "http://4.bp.blogspot.com/-Ys6mlN-qZaE/VXgmiaGmdyI/AAAAAAAAGoA/fIt-6VwUrdI/s1600/fundos-para-montagens-de-fotos-infantil%2B%25285%2529.jpg")
	faniquita = Elemento (img = linkFaniquita,
                           tit="Faniquita",
                           style=dict(left=70, top=60, width=100, height=60))
	faniquita.entra(cenaFeliz)
	txtfaniquita = Texto (cenaFeliz, "Hello")
	faniquita.vai = txtFaniquita.vai
	cenaFeliz.vai()
Historia()