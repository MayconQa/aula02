data_entrada = input("Digite uma data no formato dd/mm/aaaaa: ")

try:
    dia, mes, ano = data_entrada.split("/")

    print(f"Dia: {dia}")
    print(f"Mês: {mes}")
    print(f"Ano: {ano}")
except ValueError:
    print("Formato Inválido")
    

