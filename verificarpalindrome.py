# Requisitos para o desenvolvimento
# 1. lê-se igualmente de trás para frente. ok
# 2. desconsiderando espaços e pontoações. ok
# 3. Utilize try-except
# 4. Utilize a função isinstance()
import string

try:
    # Solicita uma frase ao usuário
    frase = input("Digite uma frase bíblica: ").strip()

    # Verifica se a entrada é uma string válida
    if not isinstance(frase, str) or frase.isdigit():
        raise ValueError("Entrada inválida! Digite apenas texto.")

    # Remove pontuações e espaços em branco
    frase_limpa = frase.translate(str.maketrans("", "", string.punctuation)).replace(" ", "")

    # Inverte a frase limpa
    frase_invertida = frase_limpa[::-1]

    # Exibe o resultado
    print(f"Frase invertida sem espaços e pontuações: {frase_invertida}")

except ValueError as e:
    print(f"Erro: {e}")

except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")

else:
    print("Programa executado com sucesso!")

finally:
    print("O programa foi finalizado.")

