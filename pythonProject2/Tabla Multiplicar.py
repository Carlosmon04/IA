def TablaMultiplicar(n):
    rango=range(1,11)
    print(f'Tabla de multiplicar del {n}')
    for i in rango:

        print(f"{n} x {i} = {int(n)*i}")

numero=input('Ingresa un Numero : ')
Tabla=int(numero)
TablaMultiplicar(numero)