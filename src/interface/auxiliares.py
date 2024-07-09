"""
Funcoes auxiliares para a entrada de dados

Objetivos:
  Funcoes auxiliares para a entrada de dados, verificacao de
  argumentos e afins.

Modificado:
  09 de julho de 2024

Autoria:
  oap
"""

__version__ = "20240709"
__author__  = "oap"

from src.interface.saida import Lang, info
from config.const import PARAMS, MOTORES

def verifica_argumentos (argumentos:list, valores:list)->bool:
  for valor in valores:
    if valor in argumentos:
      return True
  return False

def captura_primeiro_indice (argumentos:list, valores:list)->int:
  """Captura primeira ocorrencia de valor na lista de parametros."""
  for valor in valores:
    if valor in argumentos:
      return argumentos.index(valor)
  return -1

def indice_eh_valor (argumentos:list, indice:int)->bool:
  for PARAM in PARAMS:
    if argumentos[indice] in PARAMS[PARAM]:
      return False
  return True

def captura_eixos (argumentos:list, indice:int)->list:
  """Para capturar o parametro de eixos, quando for o caso"""
  eixo_x, eixo_y = 0, 1
  if indice + 1 < len(argumentos) - 1:
    if argumentos[indice+1].isnumeric():
      eixo_x, eixo_y = argumentos[indice+1]
  return int(eixo_x), int(eixo_y)

def escolha_motor (argumentos:list, tipo_motor:str): # retorna uma funcao
  """Para escolha de motor de visualizacao."""
  # Pega o padrao para previnir
  motor_lib = MOTORES[tipo_motor]["padrao"]
  # Agora ve se algum foi informado
  motores_disponiveis = MOTORES[tipo_motor]["disponiveis"]
  if verifica_argumentos(argumentos, PARAMS["MOTOR"]):
    indice = captura_primeiro_indice(argumentos, PARAMS["MOTOR"])
    if argumentos[indice+1] in motores_disponiveis:
      motor_lib = argumentos[indice+1]
    else:
      info(f'Motor {argumentos[indice+1]} invalido. Utilizando o {motor_lib} (padrao).')
  # Retorna a funcao correspondente
  return MOTORES[tipo_motor]["disponiveis"][motor_lib]
