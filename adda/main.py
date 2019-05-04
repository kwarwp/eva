# Luana RC
from _spy.vitollino.main import Cena, Elemento,Texto
transparente ="https://www.transparenttextures.com/patterns/debut-light.png"
def Historia():
	cenaFundodomar = Cena (img = "https://img.elo7.com.br/product/original/132A83E/painel-fundo-do-mar-g-frete-gratis-festa-de-aniversario.jpg")
	pequenasereia = Elemento (img = transparente,
                               tit="Mar",
                               style=dict(left=30, top=60, width=180, height=100))
	pequenasereia.entra(cenaFundodomar)
	txtpequenasereia = Texto (cenaFundodomar, "Hello")
	pequenasereia.vai = txtpequenasereia.vai()
	cenaFundodomar.vai()
Historia()