# Solicita ao usuário que insira dois valores booleanos (True ou False)
bool1 = input("Digite True ou False para o primeiro valor: ").strip().capitalize()
bool2 = input("Digite True ou False para o segundo valor: ").strip().capitalize()

# Converte as strings de entrada para valores booleanos
bool1 = bool1 == "True"
bool2 = bool2 == "True"

# Realiza a operação OR
resultado = bool1 or bool2

# Exibe o resultado
print(f"Resultado de {bool1} OR {bool2} é: {resultado}")

# or
# v v = v
# v f = v
# f v = v
# f f = f