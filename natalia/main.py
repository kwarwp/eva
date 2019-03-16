# carlos paulo 
from _spy.vitollino.main import Cena,Elemento,Texto
LinkDoCachorro = "https://cdn.shopify.com/s/files/1/0934/6862/products/10092191_l_clipped_rev_1_480x480.png?v=1491220521"
def Historia():
	cenaCout = Cena (img = "https://q-ec.bstatic.com/images/hotel/max1024x768/837/83757797.jpg")
	apolo = Elemento (img = LinkDoCachorro,
                        tit="apolo",
                        style=dict(left=60, top=60, widt=60, height=200))
	apolo.entra(cenaCout) 
	txtcachorro = Texto (cenaCout, "hello")
	apolo.vai = txtcachorro.vai
	cenaCout.vai()
Historia()