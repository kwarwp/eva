# Luana
from _spy.vitollino.main import Cena, Elemento,Texto
linkDaSereia ="https://www.impaktovisual.com.br/2924-large_default/display-pequena-sereia.jpg"
def Historia():
	cenafundodomar = Cena (img = "https://img.elo7.com.br/product/original/132A83E/painel-fundo-do-mar-g-frete-gratis-festa-de-aniversario.jpg")
	sereia = Elemento (img = linkDaSereia,
                        tit="Mar",
                        style=dict(left=150, top=60, width=60, height=200)
	sereia.entra(cenadofundodomar)
	cenafundodomar.vai()
Historia()