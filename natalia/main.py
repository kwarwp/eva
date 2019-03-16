# carlos paulo 
from _spy.vitollino.main import Cena,Elemento,Texto
LinkDoCachorro = "https://cdn.shopify.com/s/files/1/0934/6862/products/10092191_l_clipped_rev_1_480x480.png?v=1491220521"
def Historia():
	cenaCout = Cena (img = "https://http2.mlstatic.com/sementes-da-melhor-grama-p-jardim-folha-fina-ideal-60-m-D_NQ_NP_524601-MLB20356040711_072015-F.jpg")
	apolo = Elemento (img = LinkDoCachorro,
                        tit="apolo",
                        style=dict(left=60, top=60, widt=60, height=200))
	apolo.entra(cenaCout) 
	txtcachorro = Texto (cenaCout, "hello")
	apolo.vai = txtcachorro.vai
	cenaCout.vai()
Historia()