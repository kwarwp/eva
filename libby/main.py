# Lucimara
from _spy.vitollino.main import Cena, Elemento, Texto
linkdamoana ="https://vignette.wikia.nocookie.net/characterprofile/images/6/64/Hertmoana.png/revision/latest?cb=20180112235349"
def Historia():
	cenaPraiamoana = Cena (img = "https://img.elo7.ight=2com.br/product/original/16965E0/painel-praia-g-frete-gratis-infanitl.jpg")
	moana = Elemento (img = linkdamoana, 
                       tit="moana",
                       style=dict(left=150, top=60,  Width=60, height=200))
	moana.entra(cenaPraiamoana)                       
	cenaPraiamoana.vai()
Historia()
        