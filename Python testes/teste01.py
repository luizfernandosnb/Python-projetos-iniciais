import random

print('-=' * 20)
print('Jogo de Ímpar ou Par')
print('-=' * 20)
print('Digite 1 para Ímpar e 2 para Par')

escolha = int(input('Digite sua escolha: '))

if escolha == 1:
    print('Você escolheu Ímpar e a máquina escolheu Par')

    jogador = int(input('Digite um número para jogar: '))
    maquina = random.randint(1, 100)

    resultado = jogador + maquina

    print(f'Você jogou {jogador} e a máquina jogou {maquina}')

    if resultado % 2 == 0:
        print(f'O resultado é {resultado} e é PAR')
        print('Você perdeu!')
    else:
        print(f'O resultado é {resultado} e é ÍMPAR')
        print('Você ganhou!')

elif escolha == 2:
    print('Você escolheu Par e a máquina escolheu Ímpar')

    jogador = int(input('Digite um número para jogar: '))
    maquina = random.randint(1, 100)

    resultado = jogador + maquina

    print(f'Você jogou {jogador} e a máquina jogou {maquina}')

    if resultado % 2 == 0:
        print(f'O resultado é {resultado} e é PAR')
        print('Você ganhou!')
    else:
        print(f'O resultado é {resultado} e é ÍMPAR')
        print('Você perdeu!')

else:
    print('Escolha inválida! Digite 1 para Ímpar ou 2 para Par.')