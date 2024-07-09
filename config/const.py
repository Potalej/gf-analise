"""
Constantes globais

Objetivos:
  Constantes globais do sistema.

Modificado:
  09 de julho de 2024

Autoria:
  oap
"""

from src.visualizacao import visual_matplotlib, visual_pygame

###############################################################################
# > PARAMETROS E ARGUMENTOS PARA ENTRADA DE DADOS
###############################################################################
PARAMS = {
  "AJUDA" : ["-h", "--help"],
  "TESTES": ["-tt", "--testes"],
  "VI"    : ["-vi", "--valores-iniciais"],
  "DS"    : ["-ds", "--dados-simulacao"],
  "E2D"   : ["-e2d", "--exibir-2d"],
  "E3D"   : ["-e3d", "--exibir-3d"],
  "S2D"   : ["-s2d", "--salvar-2d"],
  "MOTOR" : ["-m", "--motor"]
}

###############################################################################
# > MOTORES DE GERACAO DE GRAFICOS
###############################################################################
MOTORES = {
  "vi_2d": {
    "padrao": "matplotlib",
    "disponiveis": {
      "matplotlib": visual_matplotlib.exibir_pontos_2d,
      "pygame"    : visual_pygame.exibir_trajetorias_2d 
    }
  },
  "vi_3d": {
    "padrao": "matplotlib",
    "disponiveis": {
      "matplotlib": visual_matplotlib.exibir_pontos_3d
    }
  },
  "ds_2d": {
    "padrao": "pygame",
    "disponiveis": {
      "matplotlib": visual_matplotlib.exibir_trajetorias_2d,
      "pygame": visual_pygame.exibir_trajetorias_2d
    }
  },
  "ds_3d": {
    "padrao": "matplotlib",
    "disponiveis": {
      "matplotlib": visual_matplotlib.exibir_trajetorias_3d
    }
  },
  "ds_s_2d": {
    "padrao": "matplotlib",
    "disponiveis": {
      "matplotlib": visual_matplotlib.animacao_trajetorias_2d
    }
  },
}