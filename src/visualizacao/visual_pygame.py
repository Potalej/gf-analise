"""
Visualizacao de informacoes em graficos com pygame

Objetivos:
  Funcoes para visualizar graficos atraves do pygame.

Modificado:
  10 de julho de 2024

Autoria:
  oap
"""

__all__     = ["exibir_trajetorias_2d"]
__version__ = "20241111"
__author__  = "oap"

import pygame
from src.arquivos.ler import ler_dados_simulacao
from config.config_pygame import *
from src.visualizacao.seta import draw_arrow
from numpy.linalg import norm

##############################################################################
# > FUNCOES PRINCIPAIS
##############################################################################

def exibir_trajetorias_2d (infos:dict, eixo_x:int=0, eixo_y:int=1)->None:
  """Plot de trajetorias 2d dada uma lista de corpos (dicts)."""
  corpos = infos["corpos"]
  massas, posicoes, momentos = [], [], []
  for corpo in corpos:
    massas.append(corpo["massa"])
    posicoes.append(corpo["posicoes"])
    momentos.append(corpo["momentos"])
  maior_massa = max(massas)
  massas_relativas = [massa/maior_massa for massa in massas]
  exibir_evolucao_2d(massas_relativas, posicoes, momentos, infos)


##############################################################################
# > FUNCOES AUXILIARES
##############################################################################

def criar_tela ():
  global LARGURA, ALTURA, ESCALA
  tela = pygame.display.set_mode((LARGURA, ALTURA))
  superficie = pygame.Surface((LARGURA*ESCALA, ALTURA*ESCALA))
  pygame.display.set_caption("gf-analise")
  pygame.init()
  
  # Para debug
  texto_debug = pygame.font.SysFont(FONTE, TAMANHO_FONTE)
  
  return tela, superficie, texto_debug

def aplicar_zoom (qntd:int)->None:
  """Aplica zoom na tela."""
  global ZOOM, TAXA_ZOOM
  ZOOM += TAXA_ZOOM * qntd

def aplicar_movimentacao (evento_chave:int)->None:
  """Aplica movimentacao da tela."""
  global MOV_X, MOV_Y
  if evento_chave == pygame.K_LEFT:
    MOV_X -= 1
  elif evento_chave == pygame.K_RIGHT:
    MOV_X += 1
  elif evento_chave == pygame.K_UP:
    MOV_Y -= 1
  elif evento_chave == pygame.K_DOWN:
    MOV_Y += 1

def aplicar_densidade (evento_chave:int)->None:
  """Aplica alteracao na densidade."""
  global DENSIDADE, TAXA_DENSIDADE
  if evento_chave == pygame.K_w:
    DENSIDADE += TAXA_DENSIDADE
  elif evento_chave == pygame.K_s:
    if round(DENSIDADE - TAXA_DENSIDADE,3) > 0:
      DENSIDADE -= TAXA_DENSIDADE

def aplicar_fps ()->None:
  """Aplica alteracao na quantidade de FPS."""
  global FPS
  if   FPS == 24:  FPS = 30
  elif FPS == 30:  FPS = 60
  elif FPS == 60:  FPS = 120
  elif FPS == 120:  FPS = 240
  elif FPS == 240:  FPS = 480
  elif FPS == 480: FPS = 24

def exibir_vetores ()->None:
  global EXIBIR_VETORES
  EXIBIR_VETORES = not EXIBIR_VETORES

def controle_eventos (eventos:list)->None:
  """Dada uma lista de eventos de interacao (input), faz a acao devida."""
  for evento in eventos:
    # Sair
    if evento.type in [pygame.QUIT, pygame.K_ESCAPE]:
      return 1
      
    # Zoom (rodinha do mouse)
    elif evento.type == pygame.MOUSEWHEEL:
      aplicar_zoom(evento.y)
    
    elif evento.type == pygame.KEYDOWN:

      # Movimentacao na tela (setinhas)
      if evento.key in [pygame.K_LEFT, pygame.K_RIGHT, 
                        pygame.K_UP, pygame.K_DOWN]:
        aplicar_movimentacao(evento.key)

      # Para reiniciar a exibicao
      elif evento.key == pygame.K_BACKSPACE:
        return 2

      # Para exibir o debug
      elif evento.key == pygame.K_d:
        return 3

      # Para pausar ou despausar
      elif evento.key == pygame.K_SPACE:
        return 4
      
      # Para alterar a densidade
      elif evento.key in [pygame.K_w, pygame.K_s]:
        aplicar_densidade(evento.key)

      # Para alterar a taxa de atualizacao
      elif evento.key == pygame.K_f:
        aplicar_fps()

      # Para exibir ou nao os vetores
      elif evento.key == pygame.K_v:
        exibir_vetores()
    
def adaptacao_coordenadas (x:float, y:float)->list:
  """Adapta coordenadas cartesianas para o pygame."""
  global ESCALA, LARGURA, ALTURA, ZOOM

  novo_x = (x * (2**ZOOM) + ESCALA * LARGURA / 2) + MOV_X * FATOR_MOV_X
  novo_y = (y * (2**ZOOM) + ESCALA * LARGURA / 2) + MOV_Y * FATOR_MOV_Y
  return novo_x, novo_y

def desenhar_2d (superficie, t:int, massas:list, posicoes:list, momentos:list)->None:
  """Dada uma lista de massas e posicoes, desenha os pontos."""
  global COR_PONTO, DENSIDADE, EXIBIR_VETORES
  for corpo, posicao in enumerate(posicoes):
    x,y,_ = posicao[t]
    x,y   = adaptacao_coordenadas(x,y)
    massa = massas[corpo]
    pygame.draw.circle(
      superficie, COR_PONTO, (x,y), massa / DENSIDADE
    )
    # else:
    #   pygame.draw.circle(
    #     superficie, (0, 255, 255), (x,y), massa / DENSIDADE
    #   )

    if EXIBIR_VETORES:
      k = 50
      p = momentos[corpo][t]
      norma = norm(p)
      p_norm = [pi/norma for pi in p]
      draw_arrow(superficie,
                pygame.Vector2(x,y),
                pygame.Vector2(x+k*p_norm[0], y+k*p_norm[1]),
                pygame.Color("dodgerblue"),
                7, 14, 7)

def exibir_debug (tela, texto_debug, fps:float, infos:dict, i:int)->None:
  """Para exibicao de informacoes de desenvolvimento (debug)."""
  global DEBUG_POSICAO, TELA_COR_TEXTO, TAMANHO_FONTE
  
  strings_debug =  []
  strings_debug += [f"FPS: {round(fps, 2)}"]
  strings_debug += [f"D: {round(DENSIDADE,2)}"]
  strings_debug += [f"X: {MOV_X}"]
  strings_debug += [f"Y: {MOV_Y}"]
  strings_debug += [f"z: {2**ZOOM:.2e}"]

  for i, string in enumerate(strings_debug):
    tela.blit(
      texto_debug.render(string, True, TELA_COR_TEXTO),
      [DEBUG_POSICAO[0], DEBUG_POSICAO[1] + i*(TAMANHO_FONTE + 2)]
    ) 

def exibir_evolucao_2d (massas_rel:list, posicoes:list, momentos:list, infos:dict)->None:
  """Exibicao de evolucao de trajetorias em 2d."""
  global FPS

  # Cria uma tela
  tela, superficie, texto_debug = criar_tela()
  clock = pygame.time.Clock()

  # Contador para exibicao dos frames
  i = 0
  tamanho_maximo_contador = len(posicoes[0]) - 1
  estatico = (len(posicoes[0]) == 1)

  # Para controlar a atualizacao da exibicao
  exibir = True

  # Para exibicao de informacoes de dev (debug)
  debug = False

  while True:
    # Fixa a quantidade maxima de frames por segundo
    clock.tick(FPS)

    # Controle de eventos
    acao = controle_eventos(pygame.event.get())
    
    # Sair
    if acao == 1: 
      break
    # Acao de exibir ou nao
    if acao == 2:
      exibir = True
      i = 0
    # Acao de ativar ou desativar debug
    elif acao == 3:
      debug = not debug
    # Acao de pausar
    elif acao == 4:
      if i != tamanho_maximo_contador:
        exibir = not exibir

    # Cor do fundo / limpa
    superficie.fill(TELA_COR_FUNDO)
    
    # Exibicao
    desenhar_2d(superficie, i, massas_rel, posicoes, momentos)

    # Adaptacoes
    tela_redimensionada = pygame.transform.smoothscale(superficie, tela.get_size())
    tela.blit(tela_redimensionada, (0,0))
    pygame.display.flip() # Giro da tela (de ponta cabeca)

    # Exibicao de debug
    if debug:
      exibir_debug(tela, texto_debug, clock.get_fps(), infos, i)

    # Atualiza a tela
    pygame.display.update()

    if exibir and not estatico:
      i += 1

    if i == tamanho_maximo_contador:
      exibir = False
  
  # Encerra
  pygame.quit()