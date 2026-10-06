def sumar(a, b):
    return a + b

def multiplicar(a, b):
    # Error intencional: restamos en lugar de multiplicar
    return a - b 

if __name__ == "__main__":
    print(f"Resultado de la suma 2 + 3: {sumar(2, 3)}")