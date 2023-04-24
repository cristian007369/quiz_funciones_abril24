# Construir una función que reciba un valor entero como parámetro y que determine si su último dígito es 4.

def mostar_ultimo_digito(n):
    e=n
    n=n%10
    if n==4:
        print(f"El ultimo dígito de {e} es cuatro1")
    else:
        print(f"El ultimo dígito de {e} no es cuatro")
           


n=int(input("Ingrese un número entero\n"))
mostar_ultimo_digito(n)