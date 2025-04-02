try:
    num = 10
    texto = "Ola"
    resultado = num + texto  # Isso vai gerar um erro
except TypeError:
    print("Erro: Tipos de dados incompatíveis.")
else:
    print("Programa executado com sucesso!")
finally:
    print("Programa finalidado")