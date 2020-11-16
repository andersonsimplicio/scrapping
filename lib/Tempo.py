import datetime
from datetime  import date as dt


def obterDataPostagem(tempo=""):
    anoAtual = datetime.datetime.now().year

    if ( 'ano' in tempo) or  ('anos' in tempo):
        passado = int(tempo[0])  
        return anoAtual - passado
    else:
        return anoAtual



