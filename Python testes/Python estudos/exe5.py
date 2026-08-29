print ('==' * 15)
print ('------Comercio Universal------')
print ('==' * 15)
avanco = 'S'
soma = 0 
menor_valor = 0
nome = ' '
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
print (f'O valor total gasto é: R$ {soma:.2f}')
print (f'O produto de menor valor seria {nome} de custo: R$ {menor_valor}')