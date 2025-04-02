# Exercício 23: Calculadora Simples
# Desenvolva uma calculadora simples que aceite duas entradas numéricas 
# e um operador (+, -, *, /) do usuário. Use try-except para lidar com 
# divisões por zero e entradas não numéricas. Utilize if-elif-else para 
# realizar a operação matemática baseada no operador fornecido. Imprima 
# o resultado ou uma mensagem de erro apropriada.

try:
    numero1 = float(input("Digite número: "))
    
    while True:
        operador = input("Selecione o operador (+, -, *, /): ")
        if operador in ["+", "-", "*", "/"]:
            break
        print("Operador inválido! Aceita apenas +, -, * ou /.")

    numero2 = float(input("Digite número: "))

    print(f"{numero1} {operador} {numero2} = ", end="")

    if operador == "+":
        print(numero1 + numero2)
    elif operador == "-":
        print(numero1 - numero2)
    elif operador == "*":
        print(numero1 * numero2)
    elif operador == "/":
        if numero2 != 0:
            print(numero1 / numero2)
        else:
            print("Erro: Divisão por zero não é permitida.")

except ValueError:
    print("Erro: Digite apenas números.")
else:
    print("Programa executado com sucesso!")
finally: 
    print("Programa finalizado.")
