"""
Visualizacao de informacoes em graficos com matplotlib

Objetivos:
  Funcoes para visualizar graficos atraves do matplotlib.

Modificado:
  09 de julho de 2024

Autoria:
  oap
"""

__version__ = "20240709"
__author__  = "oap"

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx
from os import mkdir
from pathlib import Path
from time import time
from numpy import arange
import src.interface.saida as saida
from config.config_matplotlib import *

def exibir_trajetorias_2d (corpos:list, eixo_x:int=0, eixo_y:int=1)->None:
  """Plot de trajetorias 2d dada uma lista de corpos (dicts)."""
  for corpo in corpos:
    posicoes = list(zip(*corpo["posicoes"]))
    x, y = posicoes[eixo_x], posicoes[eixo_y]
    plt.scatter(x[-1],y[-1])
    plt.plot(x,y)
  plt.show()

def exibir_trajetorias_3d (corpos:list)->None:
  """Plot (scatter) das posicoes iniciais de uma lista de corpos em 3d"""
  fig = plt.figure()
  ax = fig.add_subplot(projection="3d")
  for corpo in corpos:
    x,y,z = list(zip(*corpo["posicoes"]))
    ax.scatter(x[0],y[0],z[0])
    ax.plot(x,y,z)
  plt.show()

def exibir_pontos_2d (corpos:list, eixo_x:int=0, eixo_y:int=1)->None:
  """Plot (scatter) das posicoes iniciais de uma lista de corpos em 2d"""
  for corpo in corpos:
    posicoes = list(zip(*corpo["posicoes"]))
    x, y = posicoes[eixo_x], posicoes[eixo_y]
    plt.scatter(x[0],y[0])
  plt.show()

def exibir_pontos_3d (corpos:list)->None:
  """Plot (scatter) das posicoes iniciais de uma lista de corpos em 3d"""
  fig = plt.figure()
  ax = fig.add_subplot(projection="3d")
  for corpo in corpos:
    x,y,z = list(zip(*corpo["posicoes"]))
    ax.scatter(x[0],y[0],z[0])
  plt.show()


def atualizar_2d (t, inicio:int, comprimento:int, ax, posicoes:list, eixo_x:int=0, eixo_y:int=1)->None:
  """Atualizacao dos frames 2d."""
  # Limpa o desenho
  ax.clear()
  ax.set_xlim([-5,5])
  ax.set_ylim([-5,5])

  inicio_intervalo = inicio * comprimento
  final_intervalo  = (inicio+1) * comprimento

  # Plota
  for corpo in posicoes:
    pos = list(zip(*corpo))
    # x, y = pos[eixo_x][inicio_intervalo:final_intervalo], pos[eixo_y][inicio_intervalo:final_intervalo]
    x, y = pos[eixo_x][inicio_intervalo:final_intervalo], pos[eixo_y][inicio_intervalo:final_intervalo]
    if len(x) == 0: return 
    # Posicoes
    ax.scatter(x[t],y[t], c="black")
    
    # Plot do rastro
    # tamanho_rastro = round(comprimento / 2)
    # ax.plot(x[t-tamanho_rastro:t], y[t-tamanho_rastro:t], c="black")


def animacao_trajetorias_2d (corpos:list, eixo_x:int=0, eixo_y:int=1, maximo:int=-1)->None:
  """Geracao de animacao 2d das trajetorias de uma lista de corpos (dicts)."""
  # Diretorio
  if not Path(DIR_SAIDA).is_dir():
    mkdir(DIR_SAIDA)
  pasta = str(round(time())) 
  mkdir(f'{DIR_SAIDA}/{pasta}')
  
  # Delimitacao dos intervalos
  posicoes = [corpo["posicoes"][:maximo] for corpo in corpos]

  # Plots dos GIFs individuais
  frames = 240
  intervalo_frames = 10
  qntd_passos_total = len(posicoes[0])
  qntd_passos       = round(qntd_passos_total / frames)

  saida.info(f"Serao gerados {qntd_passos} arquivos .gif")
  t0 = time()
  for i in range(qntd_passos-1):
    # Plots
    fig = plt.figure(dpi=FIG_DPI)
    ax = fig.add_subplot()
    # Funcao auxiliar
    local_atualizar_2d = lambda t: atualizar_2d(t, i, frames, ax, posicoes, eixo_x, eixo_y)
    # Animacao
    animacao = animation.FuncAnimation(fig, local_atualizar_2d, arange(frames), interval=intervalo_frames, repeat=False)
    
    if WRITER == "FFMPEG":
      writervideo = animation.FFMpegFileWriter(fps=WRITER_FPS, metadata=WRITER_METADATA, bitrate=WRITER_BITRATE)
    elif WRITER == "PILLOW":
      writervideo = animation.PillowWriter(fps=WRITER_FPS, bitrate=WRITER_BITRATE)

    animacao.save(f"{DIR_SAIDA}/{pasta}/frame{i}.mp4", writer=writervideo)
    if i == 0:
      print(f"Tempo: {time()-t0}s")
      print(f"Tempo estimado: {qntd_passos * (time()-t0)}s")

  # Agora gera um arquivo de video
  arquivos = []
  diretorio = lambda i: f"{DIR_SAIDA}/{pasta}/frame{i}.mp4"
  for i in range(qntd_passos-1):
    clipe = VideoFileClip(diretorio(i))  # Clipe .gif
    clipe.fx(vfx.speedx, 2)              # Velocidade 2x
    arquivos.append(clipe)
  
  # Concatena e salva
  video_final = concatenate_videoclips(arquivos)
  video_final.write_videofile(f"{DIR_SAIDA}/{pasta}/video.mp4")