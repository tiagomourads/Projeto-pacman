import os
from random import randint
from time import sleep

# Aqui inserimos as dimenções do layout.

largura = 10 
altura = 10

# Criamos as variaveis e atribuimos os valores referentes ao pac-man e a comida.

pacman = 'O'
comida = 'X'

# Posição inicial do Pac-man
posicao_pacman = [randint(0, largura - 1), randint(0, altura - 1)]

# Posição inicial da comida no layout

posicao_comida = [randint(0, largura - 1), randint(0, altura - 1)]

# Comando onde a comida vai aparecer aleatoriamente no layout 
def reposicionar_comida():
    posicao_comida[0] = randint(0, largura - 1)
    posicao_comida[1] = randint(0, altura - 1)

# Definimos essa função para a movimentação do pac-man em direção a comida

def mover_pacman():
    x_pacman, y_pacman = posicao_pacman
    x_comida, y_comida = posicao_comida
    sleep(0.3)
    if x_pacman < x_comida:
        x_pacman += 1
    elif x_pacman > x_comida:
        x_pacman -= 1
    elif y_pacman < y_comida:
        y_pacman += 1
    elif y_pacman > y_comida:
        y_pacman -= 1
    
    # Essas linhas de código servem para limitadas como coordenadas do Pac-Man dentro dos limites do layout
    
    posicao_pacman[0] = max(0, min(x_pacman, largura - 1))
    posicao_pacman[1] = max(0, min(y_pacman, altura - 1))

# Definimos mais uma função para a exibição do layout

def exibir_layout():
    os.system('cls') # Foi importado o (os) para limpar o terminal e só exibir um layout com o pac-man se movimentando
    for coluna in range(altura):
        for linha in range(largura):
            if [linha, coluna] == posicao_pacman:
                # Se o resto da divisão for igual a 0 o pac-man vai ficar Maiúsculo, caso contrário será Minúsculo 
                print(pacman.upper() if (linha + coluna) % 2 == 0 else pacman.lower(), end=' ') 
            elif [linha, coluna] == posicao_comida:
             # Gerar a comida no local correto    
                print(comida, end=' ')
            else:
            # Caso contrario exibir o layout com varios pontos (.)
                print('.', end=' ')
        print()
# Esse é o loop principal do jogo,significa que o jogo continuar sendo executado até que uma condição seja atendida.
while True:
    exibir_layout()
    mover_pacman()
# Quando essa condição for atendida, o jogo começa novamente, por isso chamamos a função reposicionar_comida.
    if posicao_pacman == posicao_comida:
        reposicionar_comida()

