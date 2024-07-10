# 🪐gf-analise🎲
Para análise dos dados dos gravidade-fortran!

Para instalar
```
pip install -r requirements.txt
```

## 📌 Objetivos
- [X] Leitura dos arquivos de saída dos GFs:
  - [X] Valores iniciais;
  - [X] Dados de simulação;
- [X] Órbitas:
  - [X] Visualização 2D das órbitas;
  - [X] Visualização 3D das órbitas;
  - [X] Geração de vídeo 2D das órbitas;
  - [ ] Geração de vídeo 3D das órbitas;
- [ ] Estatísticas básicas:
  - [ ] Cálculo das integrais primeiras;
  - [ ] Visualização com evolução temporal;
- [X] Testes.

## ⚙️ Funcionalidades

### ❓ Ajuda
Na dúvida, rode:
```shell
py main.py -h
```
Ou consulte o arquivo "language/ajuda.txt". O texto abaixo é uma versão mais prolongada do texto de ajuda.

### 🎨 Motores

O programa permite utilizar diferente motores de geração de visualização 2D e 3D das simulações. Nas opções de visualização (vistas adiante), é possível informar o motor desejado através do argumento `-m` (ou `--motor`):

```shell
py main.py [opcoes] -m [motor] caminho/do/arquivo.txt
```

Os motores disponíveis no momento são:
- [Matplotlib](https://matplotlib.org/);
- [PyGame](https://pygame.org).


### 💿 Valores iniciais
A entrada de arquivos de valores iniciais é feita da seguinte maneira:

```shell
python main.py -vi [opcoes] caminho/do/arquivo.txt
```
As opções disponíveis no momento são:

- (`-e2d`, `--exibir-2d`) `<args>`: Exibe os pontos em 2D. Como argumentos, é possível informar os eixos que se deseja utilizar como abscisass e ordenadas (`01`, `02`, `12`, `10`, `20`, `21`). Por padrão é `01` (xy usual);

- (`-e3d`, `--exibir-3d`): Exibe os pontos em 3D.

Também é possível informar o motor escolhido. Para visualização de valores iniciais, os disponíveis são o PyGame e o Matplotlib.

Dada a escolha de ações, também é possível informar o motor. Há um exemplo no diretório "exemplos". Para rodá-lo em 2d utilizando o PyGame, por exemplo, use:

```shell
python main.py -vi -e2d -m pygame ./exemplos/valor_inicial.txt
```

### 📀 Dados de simulações
A entrada de dados de simulações é feita da seguinte maneira:

```shell
python main.py -ds [opcoes] caminho/do/arquivo.csv
```

#### 📈 Visualização
As opções disponíveis para visualização no momento são:

- (`-e2d`, `--exibir-2d`) `<args>`: Exibe as trajetórias em 2D. Como argumentos, é possível informar os eixos que se deseja utilizar como abscissas e ordenadas (`01`, `02`, `12`, `10`, `20`, `21`). Por padrão é `01` (xy usual);
- (`-e3d`, `--exibir-3d`): Exibe as trajetórias em 3D.
- (`-s2d`, `--salvar-2d`) `<args>`: Salva animações com as trajetórias em 2D. Como argumentos, também é possível informar os eixos.

Também é possível informar o motor escolhido. Porém, ao menos por enquanto, o PyGame só está disponível para o `-e2d`, sendo o matplotlib utilizado neste e nos outros.


#### 📊 Estatísticas
Em breve...


## 📝 Testes
Para rodar uma bateria de testes:
```shell
python main.py -tt
```
ou
```shell
python main.py --testes
```
