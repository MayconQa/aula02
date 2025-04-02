def soma(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        raise TypeError("Os valores devem ser inteiros!")

print(soma(2, 3))  # ✅ Funciona
print(soma(2, "3"))  # ❌ TypeError
