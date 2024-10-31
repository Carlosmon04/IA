
def fibonacci(n):

    if n<2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def imprimir_numeros(n):
    rango = range(0,n)
    for i in rango:
        print(f"{fibonacci(i)} ", end='')

ingresar = input("Ingrese el limite : ")
z=int(ingresar)
imprimir_numeros(z)