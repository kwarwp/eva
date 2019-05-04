# Lucimara
from _spy.vitollino.main import Cena, Elemento, Texto
transparente ="https://www.transparenttextures.com/patterns/debut-light.png"
def Historia():
	cena3 = Cena (img = "https://i.imgur.com/I2u7XCz.png")
	moana = Elemento (img = linkdamoana, 
                       tit="moana",
                       style=dict(left=10, top=60,  Width=60, height=50))
	moana.entra(cena3)                       
	txtmoana = Texto (cena3, "Hello")
	moana.vai = txtmoana.vai
	cena3.vai ()
Historia()# eva.sarah.main.py