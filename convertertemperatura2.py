

try:
    celsius = float(input("Digite a tenperatura em Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C é igual a {fahrenheit}°F")
except ValueError:
    print("Erro tipo de variavel ")
else:
    print("Programa executou com sucesso!")
finally:
    print("Programa finalidado")
