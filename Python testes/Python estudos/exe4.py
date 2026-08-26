print('-=' * 30)

print('Verificador de perfil:')

print('-=' * 30)

idade = []
sexo = []
nome = []

for _ in range(4):
    print('-='*30)
    print('--Formulario--')
    print('-='*30)
    n = str(input('Digite seu nome: '))
    s = int(input('Digite seu sexo "0" se for do sexo masculino e digite "1" se for do sexo feminino: '))
    i = int(input('Digite sua idade: '))

    idade.append(i)
    sexo.append(s)
    nome.append(n)

media = sum(idade) / len(idade)

mulher = sexo.count(1)

maior_idade = max(idade)

print(f'A média das idades apresentadas é {media}')
print(f'A quantidade de mulheres no grupo é {mulher}')
print(f'A maior idade do grupo é {maior_idade}')