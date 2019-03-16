# sidonia
from _spy.vitollino.main import Cena, Elemento, Texto
linkDoTomandJerry ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS76gDxCl_SENmx4-FjMGDWSi4TZzYE-__Yn1WYOzytmCGxsXnbon-junction/tom_and_jerry.ashxtom_and_jerry.ashx"
def Historia():
	cenaHouse = Cena (img ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS76gDxCl_SENmx4-FjMGDWSi4TZzYE-__Yn1WYOzytmCGxsXnbU-vNnj-nGpEza1DckseESA")
	tomandJerry = Elemento (img =linkDoTomandJerry,
                             tit="TomandJerry",
                             style=dict(left=150, top=60, windth=60, height=200))
	tomandJerry.entra(cenaHouse)
	cenaHouse.vai()
	Historia()