import math
print ('-=' * 20)
print ('Equação de 2º grau')
print ('-=' * 20)
print ('Digite os valores das variaveis na seguinte ordem: a, b, c')
while True:
    try:
        a = float(input('Digite o valor de A: '))
        b = float(input('Digite o valor de B: '))
        c = float(input('Digite o valor de C: '))
        break
    except ValueError:
        print('Os Valores digitados não são válidos. Por favor, digite números válidos para A, B e C.')
def equacao_segundo_grau(a,b,c):
    if a == 0:
        return 'Não é um equação de 2º grau'
    else:
        delta = (b**2)-(4*a*c)
        if delta < 0:
            return 'Não existem raizes reais para está equação'
        elif delta == 0:
            raiz = -b / (2*a)
            return f'Existe appenas uma raiz rael para está equação: {raiz}'
        else:
            raiz1 = (-b + math.sqrt(delta)) / (2*a)
            raiz2 = (-b - math.sqrt(delta)) / (2*a)
            return f'As raizes reais para está equação são: {raiz1:.2f}, {raiz2:.2f}'
print('=-'* 20)
print('Resultado da equação de 2º grau')
print('=-'* 20)
print(f'Para uma equação de 2º grau com a={a}, b={b}, c={c}:')
print(equacao_segundo_grau(a,b,c))
print('=-'* 20)
print('Outros resultados da equação de 2º grau')
print('=-'* 20)
print('Para uma equação de 2º grau com a=1, b=-3, c=2:')
print(equacao_segundo_grau(1, -3, 2))
print('=-'* 20)
print('Para uma equação de 2º grau com a=1, b=2, c=5:')
print(equacao_segundo_grau(1, 2, 5))
print('=-'* 20)
print('Para uma equação de 2º grau com a=0, b=2, c=5:')
print(equacao_segundo_grau(0, 2, 5))

