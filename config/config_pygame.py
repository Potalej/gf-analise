"""
Constantes do PyGame

Objetivos:
  Constantes utilizadas na visualizacao via PyGame

Modificado:
  09 de julho de 2024

Autoria:
  oap
"""

###############################################################################
# > CONFIGURACOES DO PYGAME
###############################################################################
ZOOM          = 1         # Para aplicacao de zoom
DENSIDADE     = .1        # Vol = massa / densidade
TAXA_DENSIDADE = .01       # Taxa de alteracao da densidade
LARGURA       = 800       # Largura da tela
ALTURA        = 800       # Altura da tela
ESCALA        = 1         # Escala da tela
MOV_X         = 0         # Para movimentacao pela tela (horizontal)
MOV_Y         = 0         # Para movimentacao pela tela (vertical)
FATOR_MOV_X   = 20        # Fator de movimentacao no eixo horizontal
FATOR_MOV_Y   = 20        # Fator de movimentacao no eixo vertical
FONTE         = "Verdana" # Fonte dos textos na tela
TAMANHO_FONTE = 16        # Tamanho da fonte dos textos
FPS           = 60        # Taxa de atualizacao de quadros
TELA_COR_FUNDO = (0,0,0)  # Cor do fundo da tela
TELA_COR_TEXTO = (255,255,255) # Cor do texto
TAXA_ZOOM     = 5         # Taxa de sensibilidade do zoom
COR_PONTO     = (150, 150, 255) # Cor dos pontos (roxo)
DEBUG_POSICAO = (LARGURA-100,0) # Posicao das infos do debug na tela