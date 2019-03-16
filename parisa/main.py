# sidonia
from _spy.vitollino.main import Cena, Elemento, Texto
linkDoTomandJerry ="https://vignette.wikia.nocookie.net/thomas-and-twilight-sparkles-adventures/images/b/b3/Tom_and_Jerry_PNG_Clipart_Picture.png/revision/latest?cb=20180319200258"
def Historia():
	cenaHouse = Cena (img ="https://system.soprojetos.com.br/files/606/project_page_e/cod-94-projetos_de_casas_modelo_001.jpg?1491503956")
	tomandJerry = Elemento (img =linkDoTomandJerry,
                             tit="TomandJerry",
                             style=dict(left=90, top=60, windth=60, height=200))
	tomandJerry.entra(cenaHouse)
	txtDoTomandJerry = Texto (cenaHouse,"Hello")
	tomandJerry.vai=txtDoTomandJerry.vai
	cenaHouse.vai()
Historia()