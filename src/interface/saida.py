"""
Saida de informacoes

Objetivos:
  Funcoes para gerenciar a saida de dados e a interface do
  programa.

Modificado:
  09 de julho de 2024

Autoria:
  oap
"""

__version__ = "20240709"
__author__  = "oap"

def erro (mensagem:str):
  print(f"ERRO: {mensagem}")

def info (mensagem:str):
  print(f"\n{mensagem}")

def cabecalho (mensagem:str):
  print(f"\n* {mensagem}")

class Lang:
  DIR = "./language/"

  def _ler (arquivo:str)->None:
    with open(f"{Lang.DIR}/{arquivo}", "r") as arq:
      print(f"\n{arq.read()}")

  def cabecalho ()->None:
    Lang._ler("cabecalho.txt")

  def ajuda ()->None:
    Lang.cabecalho()
    Lang._ler("ajuda.txt")