
{'date': 'Thu Aug 08 2019 13:46:58.241 GMt-0300 (GMT-03:00) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 7
    texto = Texto("olá mundo", cena=cidade)
TypeError: __init__() got multiple values for argument 'cena'
'''},
{'date': 'Thu Aug 08 2019 13:47:59.200 GMt-0300 (GMT-03:00) -X- SuPyGirls -X-',
'error': '''
 module <string> line 7
  texto = Texto(cena=cidade, "olá mundo")
                                        ^
SyntaxError: non-keyword arg after keyword arg
'''},
{'date': 'Thu Aug 08 2019 14:04:22.452 GMt-0300 (GMT-03:00) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 32
    Jogo()
  module <module> line 22
    self.texto.foi = self.foi_text
AttributeError: 'Jogo' object has no attribute 'foi_text'
'''},