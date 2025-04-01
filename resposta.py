expressa1 = input("Digite True ou false para primeira expressão").strip().capitalize()
expressao2 = input("Digite True ou false para segunda expressão").strip().capitalize()

expressa1 = expressa1 == "True"
expressao2 = expressao2 == "True"

resultado = expressa1 and expressao2

# Exibe o resultado
print(f"Resultado de {expressa1} AND {expressao2} é: {resultado}")


# v v = v
# v f = f
# f v = f
# f f = f
