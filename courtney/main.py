# Samara
from _spy.vitollino.main import Cena, Elemento, Texto
linkDoBobEsponja ="https://vignette.wikia.nocookie.net/infobob/images/6/60/Bob_esponja4.gif/revision/latest?cb=20111023134928&path-prefix=pt"
def Historia():
	cenaPineapple = Cena (img = "data:image/jpeg;base64,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")
	bobesponja = Elemento (img = linkDoBobEsponja,
                            tit="BobEsponja",
                            style=dict(left=10, top=10, widt=10, height=10))
	bobesponja.entra(cenaPineapple)
	cenaPineapple.vai()
Historia()