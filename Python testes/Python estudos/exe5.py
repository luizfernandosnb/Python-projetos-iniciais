print ('==' * 15)
print ('------Comercio Universal------')
print ('==' * 15)
avanco = 'S'
while avanco == 'S':
    item = str(input('Digite o nome do produto: ')).strip()
    valor = int(input('Digite o valor do produto: '))
    avanco = str(input('Deseja continuar? [S/N]')).upper().strip()
    print ('==' * 15)
