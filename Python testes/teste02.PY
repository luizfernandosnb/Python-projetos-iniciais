import math
print ('-=' * 20)
print ('Equação de 2º grau')
print ('-=' * 20)
print ('Digite os valores das variaveis na seguinte ordem: a, b, c')
a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))
if a == 0:
     print ('Não é uma equação de 2º grau')
else:
     delta = (b**2) - (4*a*c)
     if delta < 0:
          print ('Não existem raizes reais para essa equação')
     elif delta == 0:
          raiz = -b / (2*a)
          print ('Existe apenas uma raiz real para essa equação: {}'.format(raiz))
     else:
          raiz1 = (-b + math.sqrt(delta)) / (2*a)
          raiz2 = (-b - math.sqrt(delta)) / (2*a)
          print ('As raizes reais para essa equação são: {}, {}'.format(raiz1, raiz2))
