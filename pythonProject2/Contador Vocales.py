def contar_vocales(frase : str):
    contador=0
    rango=range(1,len(frase))
    for i in rango:
        if frase[i] in 'aeiouAEIOU':
            contador+=1
    return contador

cadena = input("Ingrese una frase : ")
print(f"La cantidad de vocales es : {contar_vocales(cadena)}")
