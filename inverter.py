# Solicita ao usuário que insira um valor booleano (True ou False)
valor = input("Digite True ou False: ").strip().capitalize()

# Converte a entrada para um valor booleano
booleano = valor == "True"

# Inverte o valor booleano
invertido = not booleano

# Exibe o resultado
print(f"O valor invertido de {booleano} é {invertido}")
