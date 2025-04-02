
try:
    # Solicita dois números ao usuário
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    # Verifica se os números são diferentes
    if num1 != num2:
        print("Os números são diferentes.")
    else:
        print("Os números são iguais.")

except ValueError:
    print("Erro: Você deve digitar apenas números válidos.")

else:
    print("Leitura dos números realizada com sucesso!")

finally:
     print("Programa finalizado.")


