import numpy as np
import sys
from time import sleep


def bordas_nulas(matriz):
    lado = len(matriz) - 1
    matriz[0, :] = 0
    matriz[lado, :] = 0
    matriz[ :, 0 ] = 0
    matriz[ :, lado] = 0
    return matriz


def media_das_temperaturas(matriz, lin, col):
    vizinhos = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, 0), (0, -1), (1, -1), (1, 0), (1, 1)]
    soma = 0
    conta_vizinhos = 0
    linhas, colunas = np.shape(matriz)

    if matriz[lin, col] == 0:
        return 0

    for x, y in vizinhos:
        linha, coluna = lin + x, col + y
        
        if -1 < linha < linhas and -1 < coluna < colunas:
            numero_a_ser_somado = matriz[linha, coluna]
            
            if numero_a_ser_somado != 0:
                soma += numero_a_ser_somado
                conta_vizinhos += 1
    
    return round(soma / conta_vizinhos, 2)


def passa_uma_geracao(matriz):
    matriz_nova = np.copy(matriz)
    for posicao, _ in np.ndenumerate(matriz):
        matriz_nova[posicao] = media_das_temperaturas(matriz, posicao[0], posicao[1])
    return matriz_nova


def imprimir_temperaturas(matriz, geracao):
    sys.stdout.write("\033[F" * (len(matriz) + 1)) 
    sys.stdout.write(f"Geração: {geracao}\n")
    for linha in matriz:
        sys.stdout.write(" ".join(f" {celula:05.2f} " for celula in linha) + "\n")
    sys.stdout.flush()


def limpa_tela():
    sys.stdout.write("\033[H\033[J")


def regras():
    limpa_tela()
    print("""Aqui vai uma breve explicação:
          
O Jogo da Temperatura simula a evolução das temperaturas em uma matriz
de células. As células possuem valores de temperatura geradas de forma 
aleatória e, a cada geração, a temperatura de cada célula é alterada com base 
na média das temperaturas de seus vizinhos.

Regras de temperatura:

1. Cada célula tem até 8 vizinhos ao seu redor, incluindo diagonalmente.
2. A temperatura de cada célula é alterada para a média das temperaturas
dos seus vizinhos, exceto para os vizinhos com temperatura igual a 0.
3. Se a temperatura de uma célula for 0, ela permanecerá 0 nas próximas
gerações.
4. O objetivo é observar como as temperaturas se estabilizam ao longo do
tempo.

A matriz é uma grade quadrada de células que começa com temperaturas
aleatórias entre 1 e 100. A cada geração, as células terão suas temperaturas
ajustadas de acordo com as regras descritas. O programa continua até que as
temperaturas se estabilizem.

Você pode escolher o tamanho da matriz, e o programa exibirá a evolução
das temperaturas a cada geração.

Pressione Enter para começar...""")


limpa_tela()

while True:
    resposta = input("Já usou este programa antes? [Sim / Não]").lower()
    if resposta in "sim":
        break
    elif resposta in ["não", "nao", "n"]:
        regras()
        input()
        break
    else:
        limpa_tela()
        print("DIGITE UMA RESPOSTA VÁLIDA")

while True:
    try:
        tamanho =  int(input("Tamano da matriz: "))
        break
    except:
        limpa_tela() 
        print("DIGITE UM INTEIRO")

matriz = bordas_nulas(np.random.randint(1, 100, size=(tamanho,tamanho))).astype(float)
matriz_zeros = np.zeros((tamanho, tamanho))

geracao = 0
limpa_tela()

while True:
    imprimir_temperaturas(matriz, geracao)

    geracao_passada = np.copy(matriz)
    geracao += 1
    matriz = passa_uma_geracao(matriz)
    
    sleep(0.1)

    if np.array_equal(matriz, geracao_passada):
        break

print(f"\nMédia de temperatura: {np.mean(matriz[matriz != 0]):.2f}")
print(f"Geração Final: {geracao}")