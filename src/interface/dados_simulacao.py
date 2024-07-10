"""
Funcoes para lidar com dados de simulacao

Objetivos:
  Funcoes para lidar com a entrada e saida de arquivos de dados de
  simulacoes.

Modificado:
  10 de julho de 2024

Autoria:
  oap
"""

__version__ = "20240710"
__author__  = "oap"

from src.interface import auxiliares, saida
from src.arquivos.ler import ler_dados_simulacao
from src.visualizacao import visual_matplotlib, visual_pygame
from config.const import PARAMS, MOTORES

def dados_simulacao (argumentos:list)->None:
  # Verifica se quer pular dados na leitura
  indice = auxiliares.captura_primeiro_indice(argumentos, PARAMS["DS"])
  eh_valor = auxiliares.indice_eh_valor(argumentos, indice+1)
  qnt_em_qnt = int(argumentos[indice+1]) if eh_valor else 1

  # Le o arquivo
  diretorio = argumentos[-1]
  infos = ler_dados_simulacao(diretorio, qnt_em_qnt)

  # Verifica se quer exibir em 2d
  if auxiliares.verifica_argumentos(argumentos, PARAMS["E2D"]):
    
    # Captura os argumentos da exibicao
    indice = auxiliares.captura_primeiro_indice(argumentos, PARAMS["E2D"])
    eixo_x, eixo_y = auxiliares.captura_eixos(argumentos, indice)

    # Captura o motor escolhido para visualizacao
    motor = auxiliares.escolha_motor(argumentos, "ds_2d")
    
    # Roda
    motor(infos, int(eixo_x), int(eixo_y))

  # Verifica se quer exibir em 3d
  elif auxiliares.verifica_argumentos(argumentos, PARAMS["E3D"]):

    # Captura o motor escolhido para visualizacao
    motor = auxiliares.escolha_motor(argumentos, "ds_3d")
    
    # Roda
    motor(infos["corpos"])

  # Verifica se quer salvar animacoes em 2d
  elif auxiliares.verifica_argumentos(argumentos, PARAMS["S2D"]):
    
    # Captura os argumentos da exibicao
    indice = auxiliares.captura_primeiro_indice(argumentos, PARAMS["S2D"])
    eixo_x, eixo_y = auxiliares.captura_eixos(argumentos, indice)

    # Captura o motor escolhido para visualizacao
    motor = auxiliares.escolha_motor(argumentos, "ds_s_2d")
    
    # Roda
    motor(infos["corpos"], int(eixo_x), int(eixo_y), maximo=-1)

  return