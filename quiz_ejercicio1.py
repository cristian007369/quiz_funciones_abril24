# Construir una función que reciba un valor entero como parámetro y muestra la tabla de multiplicar de dicho valor recibido.

def generar_tabla_mult(n):
    print(f"Tabla del {n}:")
    for i in range(1,11):
        print(f"{n}x{i}={i*n}")


n=int(input("Dígite un valor para hacer su tabla\n"))
generar_tabla_mult(n)