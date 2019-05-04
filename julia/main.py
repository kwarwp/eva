# michelle
from _spy.vitollino.main import Cena, Elemento, Texto
transparente ="https://www.transparenttextures.com/patterns/debut-light.png "
def Historia():
	cenaFeliz = Cena (img = "http://4.bp.blogspot.com/-Ys6mlN-qZaE/VXgmiaGmdyI/AAAAAAAAGoA/fIt-6VwUrdI/s1600/fundos-para-montagens-de-fotos-infantil%2B%25285%2529.jpg")
	faniquita = Elemento (img = transparente,
                           tit="Faniquita",
                           style=dict(left=70, top=60, width=100, height=60))
	faniquita.entra(cenaFeliz)
	txtfaniquita = Texto (cenaFeliz, "Hello")
	faniquita.vai = txtfaniquita.vai
	cenaFeliz.vai()
Historia()