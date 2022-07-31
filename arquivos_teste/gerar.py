import random


def get_linha():
    limite_inferior = ord('a')
    limite_superior = ord('z')
    r = range(limite_inferior, limite_superior)
    c = random.choices(r, k=200)
    linha = ''.join([chr(x) for x in c])
    return linha


def gerar_arquivo(nome, numero_de_linhas):
    with open(nome, 'w') as f:
        for i in range(numero_de_linhas):
            l = get_linha()
            print(l, file=f)


def main():
    gerar_arquivo('arquivo_teste_1.txt', 300)
    gerar_arquivo('arquivo_teste_2.txt', 600)
    gerar_arquivo('arquivo_teste_3.txt', 1000)


if __name__ == '__main__':
    main()