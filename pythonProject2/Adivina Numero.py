import random

print("Hola Adivina el Numero Aleatorio entre 1 y 100 ")
numero= random.randint(1,100)
##print(numero) quite los comentarios para ver el numero de un solo
x=0
contador=0
while x!=numero:
    x=input("Trate de Adivinarlo : ")
    x=int(x)
    contador+=1
    if x>numero:
        print('El numero es menor')
    elif x<numero:
        print("El numero es mayor ")
print(f"Porfin pudiste, el numero era {numero} y ocupaste {contador} intentos ")
