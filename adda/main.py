# Luana
from _spy.vitollino.main import Cena, Elemento,Texto
linkDaSereia ="https://www.impaktovisual.com.br/2924-large_default/display-pequena-sereia.jpg"
def Historia():
	cenaFundodomar = Cena (img = "https://img.elo7.com.br/product/original/132A83E/painel-fundo-do-mar-g-frete-gratis-festa-de-aniversario.jpg")
	pequenasereia = Elemento (img = linkDaSereia,
                               tit="Mar",
                               style=dict(left=30, top=60, width=180, height=100))
	pequenasereia.entra(cenaFundodomar)
	txtpequenasereia = Texto (cenaFundodomar, "Hello")
	pequenasereia.vai = txtpequenasereia.vai()
	cenaFundodomar.vai()
Historia()