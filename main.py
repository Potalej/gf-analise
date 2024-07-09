import sys
from src.interface import auxiliares, saida, dados_simulacao, valores_iniciais
from config.const import PARAMS
import testes.rodar

###############################################################################

def main ()->None:

  # Argumentos no prompt
  argumentos = sys.argv[1:]

  # Ajuda
  if auxiliares.verifica_argumentos(argumentos, PARAMS["AJUDA"]):
    saida.Lang.ajuda()
    return
  
  # Valores iniciais
  if auxiliares.verifica_argumentos(argumentos, PARAMS["VI"]):
    valores_iniciais.valores_iniciais(argumentos)
    return

  # Dados de simulacao
  elif auxiliares.verifica_argumentos(argumentos, PARAMS["DS"]):
    dados_simulacao.dados_simulacao(argumentos)
    return
  
  # Testes
  elif auxiliares.verifica_argumentos(argumentos, PARAMS["TESTES"]):
    testes.rodar.rodar()


if __name__ == "__main__":
  main()