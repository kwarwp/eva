#Felipe
from _spy.vitollino.main import Cena, Elemento, Texto 
linkDoMickey ="https://vignette.wikia.nocookie.net/dublagempedia/images/6/6d/Mickey-mouse27.png/revision/latest?cb=20180110221858&path-prefix=pt-br"
def Historia():
	cenaParque = Cena (img = "http://starkovtattoo.spb.ru/images/400/DSC100466834.jpg")
    
	mickey = Elemento (img = linkDoMickey,
                        tit="Mickey",
                        style=dict(left=30, top=60, width=150, height=500))
	mickey.entra(cenaParque)
	cenaParque.vai()
Historia()