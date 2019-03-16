# Maryne
from _spy.vitollino.main import Cena, Elemento , Texto
linkDaTemari = "https://i.pinimg.com/originals/63/64/cf/6364cf82ddf68873bae992d2b9331128.jpg"
def Historia(): 
	cenaAldeiadaAreia = Cena (img = "https://pm1.narvii.com/6398/faaf9efd310bba5b5fc7ee68cb18ca138d43e30b_hq.jpg")
	Temari = Elemento (img =  linkDaTemari,
                        tit="Temari",
                        style=dict(left=150, top=60, width=60, height=200))
 	Temari.entra(cenaAldeiadaAreia)
 	txtTemari = Texto ( cenaAldeiadaAreia, "Hello")
 	Temari.vai = txtTemari.vai
 	cenaAldeiadaAreia.vai()
Historia()