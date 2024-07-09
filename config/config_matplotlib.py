"""
Constantes do Matplotlib

Objetivos:
  Constantes utilizadas na visualizacao via Matplotlib

Modificado:
  09 de julho de 2024

Autoria:
  oap
"""

###############################################################################
# > CONFIGURACOES DO MATPLOTLIB
###############################################################################
FIG_DPI         = 100         # Densidade padrao das figuras
WRITER          = "FFMPEG"    # Writer padrao de video
WRITER_FPS      = 30          # FPS padrao dos escritores de video
WRITER_BITRATE  = 1800        # Bitrate padrao dos escritores de video
WRITER_METADATA = dict(artist="oap") # Metadata padrao dos escritores de video
DIR_SAIDA       = "pontos"    # Pasta de saida padrao