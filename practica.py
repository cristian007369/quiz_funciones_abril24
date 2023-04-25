n=int(input(""))
impares = list(range(1, 2*n, 2))
suna=sum(impares)
print(impares)
print(suna)

def verificar_curiosidad_matematica(n):
    impares = list(range(1, 2*n, 2))
    suma = sum(impares[:n])
    rta = f"La suma de los {n} primeros números impares: {'+'.join(map(str, impares[:n]))} = {suma}"
    cuadrado = n**2
    return cuadrado, rta

n = int(input("Dígite un número entero positivo:\n"))
print(verificar_curiosidad_matematica(n))

def verificar_curiosidad_matematica(n):
    suma = 0
    rta = f"La suma n primeros números impares: "
    cuadrado = n ** 2
    for i in range(1, n ** 2, 2):
        suma += i
        if i == n * 2 - 1:
            rta += f"{i} = {suma}"
            break
        rta += f"{i} + "
    return (cuadrado, rta)

n = int(input("Dígite un número entero positivo:\n"))
print(verificar_curiosidad_matematica(n))

def verificar_curiosidad_matematica(n):
    impares = list(range(1, 2 * n, 2))
    suma = n ** 2
    rta = f"La suma de los {n} primeros números impares: {' + '.join(map(str, impares[:n]))} = {suma}"
    return n**2, rta

n = int(input("Dígite un número entero positivo:\n"))
print(verificar_curiosidad_matematica(n))