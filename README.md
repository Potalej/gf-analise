# gf-analise
Para análise dos dados dos gravidade-fortran!

## Objetivos
- [X] Leitura dos arquivos de saída dos GFs:
  - [X] Valores iniciais;
  - [X] Dados de simulação;
- [ ] Estatísticas básicas:
  - [ ] Cálculo das integrais primeiras;
  - [ ] Visualização com evolução temporal;
- [X] Órbitas:
  - [X] Visualização 2D das órbitas;
  - [X] Visualização 3D das órbitas;
  - [ ] Geração de vídeo 2D das órbitas;
  - [X] Geração de vídeo 3D das órbitas;
- [X] Testes.

## Funcionalidades

## Motores

O programa permite utilizar diferente motores de geração de visualização 2D e 3D das simulações. Nas opções de visualização (vistas adiante), é possível informar o motor desejado através do argumento `-m` (ou `--motor`):

```shell
py main.py [opcoes] -m [motor] caminho/do/arquivo.txt
```

Os motores disponíveis no momento são:
- [Matplotlib](https://matplotlib.org/);
- [PyGame](https://pygame.org).

### Valores iniciais
A entrada de arquivos de valores iniciais é feita da seguinte maneira:

```shell
python main.py -vi [opcoes] caminho/do/arquivo.txt
```

As opções disponíveis no momento são:

- (`-e2d`, `--exibir-2d`) `<args>`: Exibe os pontos em 2D. Como argumentos, é possível informar os eixos que se deseja utilizar como abscisass e ordenadas (`01`, `02`, `12`, `10`, `20`, `21`). Por padrão é `01` (xy usual);

- (`-e3d`, `--exibir-3d`): Exibe os pontos em 3D.

No momento o único motor disponível para visualização estática é 
Dada a escolha de ações, também é possível informar o motor. Há um exemplo no diretório "exemplos". Para rodá-lo em 2d utilizando o PyGame, por exemplo, use:

```shell
python main.py -vi -e2d -m pygame ./exemplos/valor_inicial.txt
```

## Testes

Para rodar uma bateria de testes:
```shell
python main.py -tt
```
ou
```shell
python main.py --testes
```