# Construir una función que reciba un valor entero como parámetro y que determine si su último dígito es 4.

def mostar_ultimo_digito(n):
    if n%10==4:
        print(f"El ultimo dígito de {n} es cuatro")
    else:
        print(f"El ultimo dígito de {n} no es cuatro")
           


n=int(input("Ingrese un número entero\n"))
mostar_ultimo_digito(n)