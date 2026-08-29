print ('==' * 15)
print ('------Comercio Universal------')
print ('==' * 15)
avanco = 'S'
soma = 0 
menor_valor = 0
nome = ' '
total = 0
while avanco == 'S':
    i = str(input('Digite o nome do produto: ')).strip()
    v = float(input('Digite o valor do produto: ').replace(',', '.'))
    avanco = str(input('Deseja continuar? [S/N]')).upper().strip()
    print ('==' * 15)
    if menor_valor == 0:
        menor_valor = v
        nome = i
    if menor_valor > v:
        menor_valor = v
        nome = i
    soma = v + soma
    if v >= 1000:
        total += 1
print (f'No total você comprou {total} de produtos com valor superior ou igual a R$ 1000,00.')
print (f'O produto de menor valor seria {nome} de custo: R$ {menor_valor}')
print (f'O valor total gasto é: R$ {soma:.2f}')