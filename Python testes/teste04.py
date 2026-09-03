print ('==' * 14)
print (' ------Corrida Maluca------ ')
print ('==' * 14)
start = 'N'
def cadastrar_corredores():
    corredores = []
    while True:
        nome = input("Nome do corredor: ")
        altura = float(input("Altura (em metros, ex: 1.75): "))
        peso = float(input("Peso (em kg): "))
        sexo = input("Sexo (M/F): ").strip().upper()

        corredor = {
            "nome": nome,
            "altura": altura,
            "peso": peso,
            "sexo": sexo
        }
        corredores.append(corredor)

        continuar = input("Cadastrar outro corredor? (s/n): ").strip().lower()
        if continuar != "s":
            break

    return corredores