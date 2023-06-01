import random
import time

largura = 20
altura = 20
pacman = 'o'
comida = 'X'
posicao_pacman = [random.randint(0, largura - 1), random.randint(0, altura - 1)]

def mover_pacman():
    x_pacman, y_pacman = posicao_pacman
    x_comida, y_comida = posicao_comida
    time.sleep(0.8)
    if x_pacman < x_comida:
        x_pacman += 1
    elif x_pacman > x_comida:
        x_pacman -= 1
    elif y_pacman < y_comida:
        y_pacman += 1
    elif y_pacman > y_comida:
        y_pacman -= 1

    posicao_pacman[0] = max(0, min(x_pacman, largura - 1))
    posicao_pacman[1] = max(0, min(y_pacman, altura - 1))
time.sleep(2)
def exibir_tabuleiro():
    for y in range(altura):
        for x in range(largura):
            if [x, y] == posicao_pacman:
                print(pacman.upper() if (x + y) % 2 == 0 else pacman.lower(), end=' ')
            elif [x, y] == posicao_comida:
                print(comida, end=' ')
            else:
                print('.', end=' ')
        print()


# Reposiciona a comida em um local aleatório
def reposicionar_comida():
    posicao_comida[0] = random.randint(0, largura - 1)
    posicao_comida[1] = random.randint(0, altura - 1)


# Posição inicial da comida
posicao_comida = [random.randint(0, largura - 1), random.randint(0, altura - 1)]

while True:
    exibir_tabuleiro()
    mover_pacman()

    if posicao_pacman == posicao_comida:
        print("Pac-Man comeu a comida!")
        reposicionar_comida()
        time.sleep(2)
    print("\n") # dar um espaço entre o tabuleiro
