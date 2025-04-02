def soma(a: int, b: int) -> int:
    return a + b

resultado = soma(2, "maycon")  # Erro detectado pelo mypy
print(resultado)


