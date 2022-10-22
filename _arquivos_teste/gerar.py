import random


def get_linha():
    limite_inferior = ord('a')
    limite_superior = ord('z')
    r = range(limite_inferior, limite_superior)
    n = random.randint(75, 150)
    c = random.choices(r, k=n)
    linha = ''.join([chr(x) for x in c])
    return linha


def gerar_arquivo(nome, numero_de_linhas):
    with open(nome, 'w') as f:
        for i in range(numero_de_linhas):
            l = get_linha()
            print(l, file=f)


def main():
    gerar_arquivo('cenario_1.txt', 180)
    gerar_arquivo('cenario_2.txt', 180)
    gerar_arquivo('cenario_3.txt', 900)
    gerar_arquivo('cenario_4.txt', 900)
    gerar_arquivo('cenario_5.txt', 4500)
    gerar_arquivo('cenario_6.txt', 4500)


if __name__ == '__main__':
    main()