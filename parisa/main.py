# sidonia
from _spy.vitollino.main import Cena, Elemento, Texto
linkDoTomandJerry ="https://vignette.wikia.nocookie.net/thomas-and-twilight-sparkles-adventures/images/b/b3/Tom_and_Jerry_PNG_Clipart_Picture.png/revision/latest?cb=20180319200258"
def Historia():
	cenaHouse = Cena (img ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS76gDxCl_SENmx4-FjMGDWSi4TZzYE-__Yn1WYOzytmCGxsXnbU-vNnj-nGpEza1DckseESA")
	tomandJerry = Elemento (img =linkDoTomandJerry,
                             tit="TomandJerry",
                             style=dict(left=150, top=60, windth=60, height=200))
	tomandJerry.entra(cenaHouse)
	txtlinkDoTomandJerry =Texto
	cenaHouse.vai()
	Historia()