# Jogo da adivinhação

from random import randint

print('****************************************')
print('Seja bem vindo ao jogo de adivinhação')
print('****************************************')

print('\n')

numero_secreto = randint (1, 5)
numero_escolhido = 0

while True:
    try:
        numero_escolhido = int(input('Escolha um numero de 1 a 5: '))
    except:
        print('Você escolheu um número inválido!')
    else:
        if numero_escolhido not in (1, 2, 3, 4, 5):
            print('O número precisa estar entre 1 e 5!')
            continue
        elif numero_escolhido == numero_secreto:
            print(f'Parabéns! Você descobriu que o número secreto era o {numero_secreto}!')
            break
        else:
            print('Você não acertou o número!')
