# Exercício 24: Classificador de Números
# Escreva um programa que solicite ao usuário para digitar um número. Utilize try-except para 
# assegurar que a entrada seja numérica e utilize if-elif-else para classificar o número como 
# "positivo", "negativo" ou "zero". Adicionalmente, identifique se o número é "par" ou "ímpar".



while True:
    try:
        numero = float(input("Digite um número: "))
        print(f"Você digitou: {numero}")

        #Classificação do número
        if numero > 0:
            print("O número é positivo.")
        elif numero < 0:
            print("O número é negativo.")
        else:
            print("O número é zero.")
        
        opcao = input("Deseja continuar? (s para sair / qualquer outra tecla para continuar): ").lower()
        if opcao == 's':
            print("Programa finalizado!")
            break
    except ValueError:
        print("Erro: Digite apenas números válidos!")