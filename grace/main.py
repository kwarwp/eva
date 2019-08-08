# eva.grace.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, Sala
CIDADE = "http://lorempixel.com/output/city-q-c-640-480-7.jpg"
CARA = "http://lorempixel.com/100/100/people/1"
OUTRA = "http://lorempixel.com/300/300/city/2"
EOUTRA = "http://lorempixel.com/300/300/city/3"
MSOUTRA = "http://lorempixel.com/300/300/city/4"


class Jogo:
    def __init__(self):
        cidade = Cena(CIDADE)
        outra = Cena(OUTRA)
        cidade.direita = outra
        outra.esquerda = cidade
        #texto.vai()
        #cidade.vai()
        sala = Sala(CIDADE, OUTRA, EOUTRA, MSOUTRA)
        cara = Elemento(CARA, cena=sala.norte, style=dict(width=40, height="40px", left=100, top=100))
        cara.vai = self.vai_cara
        self.texto = Texto(sala.norte, "olá mundo")
        self.texto.foi = self.foi_texto
        self.texto_foi = Texto(sala.norte, "Tudo bem?")
        sala.norte.vai()
        
    def vai_cara(self, ev):
        self.texto.vai()
        
    def foi_texto(self, ev=0):
        self.texto_foi.vai()
        
Jogo()