def es_primo(numero):
    rango=range(1,numero+1)
    contador=0
    for i in rango:
        if numero%i==0:
            contador=contador+1

    if contador==2:
        print('Es Primo')
    else:
        print("NO es primo")

dato=input('Ingrese un numero : ')
numero=int(dato)
es_primo(numero)