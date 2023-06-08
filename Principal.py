import os
from random import randint
from time import sleep

# Aqui inserimos as dimenções do Grid.

largura = 10 
altura = 10

# Criamos as variaveis e atribuimos os valores referentes ao pac-man e a comida.

pacman = 'O'
comida = 'X'

# Posição inicial do Pac-man
posicao_pacman = [randint(0, largura - 1), randint(0, altura - 1)]

# Posição inicial da comida no Grid

posicao_comida = [randint(0, largura - 1), randint(0, altura - 1)]

# Definimos essa função para a comida reposicionar aleatoriamente no Grid
def reposicionar_comida():
    posicao_comida[0] = randint(0, largura - 1)
    posicao_comida[1] = randint(0, altura - 1)

# Definimos essa função para a movimentação do pac-man em direção a comida

def mover_pacman():
    moverX_pacman, moverY_pacman = posicao_pacman
    moverX_comida, moverY_comida = posicao_comida
    sleep(0.3)
    if moverX_pacman < moverX_comida:
        moverX_pacman += 1
    elif moverX_pacman > moverX_comida:
        moverX_pacman -= 1
    elif moverY_pacman < moverY_comida:
        moverY_pacman += 1
    elif moverY_pacman > moverY_comida:
        moverY_pacman -= 1
    
    # Essas linhas de código serve para limitar, como coordenadas do Pac-Man dentro dos limites do Grid
    
    posicao_pacman[0] = max(0, min(moverX_pacman, largura - 1))
    posicao_pacman[1] = max(0, min(moverY_pacman, altura - 1))

# Definimos mais uma função para a exibição do Grid

def exibir_Grid():
    os.system('cls') # Foi importado o (os) para limpar o terminal e só exibir um Grid com o pac-man se movimentando
    for coluna in range(altura):
        for linha in range(largura):
            if [linha, coluna] == posicao_pacman:
                # Se o resto da divisão for igual a 0 o pac-man vai ficar Maiúsculo, caso contrário será Minúsculo 
                print(pacman.upper() if (linha + coluna) % 2 == 0 else pacman.lower(), end=' ') 
            elif [linha, coluna] == posicao_comida:
             # Gerar a comida no local correto    
                print(comida, end=' ')
            else:
            # Caso contrario exibir o Grid com varios pontos (.)
                print('.', end=' ')
        print()
# Esse é o loop principal do jogo,significa que o jogo vai continuar sendo executado até que uma condição seja atendida.
while True:
    exibir_Grid()
    mover_pacman()
# Quando essa condição for atendida, o jogo começa novamente, por isso chamamos a função reposicionar_comida.
    if posicao_pacman == posicao_comida:
        reposicionar_comida()

