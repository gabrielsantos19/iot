import random


def get_linha():
    limite_inferior = ord('a')
    limite_superior = ord('z')
    r = range(limite_inferior, limite_superior)
    c = random.choices(r, k=125)
    linha = ''.join([chr(x) for x in c])
    return linha


def gerar_arquivo(nome, numero_de_linhas):
    with open(nome, 'w') as f:
        for i in range(numero_de_linhas):
            l = get_linha()
            print(f"{i:04}_{l}", file=f)


def main():
    gerar_arquivo('cenario_1.txt', 30)
    gerar_arquivo('cenario_2.txt', 30)
    gerar_arquivo('cenario_3.txt', 900)
    gerar_arquivo('cenario_4.txt', 900)


if __name__ == '__main__':
    main()