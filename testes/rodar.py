"""
Bateria de testes

Objetivos:
  Fazer uma bateria de testes

Modificado:
  09 de julho de 2024

Autoria:
  oap
"""

__version__ = "20240709"
__author__  = "oap"

from testes import ds_e2d, ds_e3d, ds_s2d, vi_e2d, vi_e3d

def rodar ():
  print("BATERIA DE TESTES")

  ##########################
  print("VI_E2D")
  vi_e2d.teste()
  ##########################

  ##########################
  print("VI_E3D")
  vi_e3d.teste()
  ##########################

  ##########################
  print("DS_E2D")
  ds_e2d.teste()
  ##########################

  ##########################
  print("DS_E3D")
  ds_e3d.teste()
  ##########################

  ##########################
  print("DS_S2D")
  ds_s2d.teste()
  ##########################