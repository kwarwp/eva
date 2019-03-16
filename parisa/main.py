# sidonia
from _spy.vitollino.main import Cena, Elemento, Texto
linkDoTomandJerry = "https://static.farahexperiences.com/-/media/yasconnect/project/wbw/character/carousel/cartoon-junction/tom_and_jerry.ashxtom_and_jerry.ashx"
def Historia():
	cenaHouse = Cena (img ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ1AU55ME39mqUaas9E_eu_1YquG8lOU-vNnj-nGpEza1DckseESA")
	TomandJerry = Elemento (img = linkDoTomandJerry,
                            tit="TomandJerry"
                            style=dict(left=150, top=60, windth=60,height=200))
	TomandJerry.entra(cenaHouse)
	cenaHouse.vai()
	Historia()