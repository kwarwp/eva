# daiane
from _spy.vitollino.main import Cena,Elemento,Texto
linkxango = "https://i.pinimg.com/originals/a9/91/3e/a9913ee60a08b68d18d2022010acf7fb.png"
def Historia():
	cenafloresta = Cena ("https://www.mundoecologia.com.br/wp-content/gallery/ecologia-de-plantas/Ecologia-de-Plantas-4.png")
	xango = Elemento(img=linkxango,
                      tit="xango",
                      style=dict(left=150, top =60, width=60, height=200))
	xango.entra(cenafloresta)
	txtxango = Texto(cenafloresta,"hello")
	xango.vai=txtxango.vai 
	cenafloresta.vai()
Historia()
