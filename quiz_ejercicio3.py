def verificar_curiosidad_matematica(n):
    suma=0
    rta=f"La suma n primeros números impares: "
    for i in range(1,n*2,2):
        suma+=i
        if suma==n**2:
            rta+=f"{i} = {suma}"
            break
        rta+=f"{i} + "
    return(n**2,rta)
n=int(input("Dígite un número entero positivo:\n"))
print(verificar_curiosidad_matematica(n))

def verificar(n):
    lista=list(range(1,2*n,2))
    suma=sum(lista)
    return (print(f"{n}^2={n**2}",f"que es la suma de {' + '.join(map(str, lista))}",f"= {suma}"))

verificar(n)