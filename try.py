try:
    resultado = str(input("Digite seu nome completo"))
    resultado = resultado.__len__()
except TypeError as erro:
    print(erro)
else:
    print("leu a string com sucesso!")
    print(resultado)
finally:
    exit()
    