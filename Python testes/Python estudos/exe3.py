print('Soma dos numero impares multiplos de 3 entre 1 a 500')
soma = sum(i for i in range (1, 501) if i % 3 == 0 and i % 2 != 0)
print (f'O valor da soma é {soma}')