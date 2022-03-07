import random as rd

print('bem vindo ao jogo de advinhação, aqui voce tera que acertar um chute para um numero aleatorio')

numero_aleatorio = rd.randrange (1,100)
total_tentativas = 4

print(numero_aleatorio)
# o print acima serve para testar o código

for rodada in range(1, total_tentativas, 1):
    tentativa = int(input("digite um numero :"))

    if tentativa == numero_aleatorio:
        print("acertou!!!!!!!!")
        break
    elif tentativa < 1 or tentativa > 100:
        print("voce inseriu um numero invalido, favor inserir um valor entre 1 e 100")
        break
    else:
        print("infelizmente dessa vez voce não acertou, tente mais uma vez")
        if rodada == 3:
            break

print("fim de jogo")

