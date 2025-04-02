# ## Exercício 25: Conversão de Tipo com Validação
# 25. Crie um script que solicite ao usuário uma lista de números separados por vírgula. 
# O programa deve converter a string de entrada em uma lista de números inteiros. Utilize 
# try-except para tratar a conversão de cada número e validar que cada elemento da lista 
# convertida é um inteiro. Se a conversão falhar ou um elemento não for um inteiro, imprima 
# uma mensagem de erro. Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.

while True:
    try:
        # Solicita a entrada do usuário
        numero_entrada = input("Digite uma lista de números inteiros separados por vírgula: ")

        # Converte a entrada para uma lista de inteiros, validando cada elemento
        numeros = [int(num.strip()) for num in numero_entrada.split(",")]

        # Exibe a lista de inteiros
        print("Lista de números inteiros:", numeros)

    except ValueError:
        print("Erro: Certifique-se de digitar apenas números inteiros separados por vírgula.")
        continue  # Volta para o início do loop para nova tentativa

    # Pergunta ao usuário se deseja continuar ou sair
    opcao = input("Deseja continuar? (s para sair / qualquer outra tecla para continuar): ").lower()
    if opcao == 's':
        print("Programa finalizado!")
        break
