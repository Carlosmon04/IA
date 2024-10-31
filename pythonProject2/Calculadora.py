class calculadora:
    def sumar(self) :
        print("Escriba 'E' si desea dejar de sumar numeros ")
        x='S'
        y=0
        while x!='E':

             x=input("Ingrese numero a sumar : ")
             if x != 'E':

              y= y = int(x)+int(y)
        print(y)

    def resta(self):
        print("Escriba 'E' si desea dejar de Restar numeros ")
        x = input("Ingrese numero a restar : ")
        if x == 'E':
            print(0)
            return
        y = int(x)
        while True:
            x = input("Ingrese numero a restar : ")
            if x == 'E':
                break
            y -= int(x)
        print(y)

    def multiplicar(self) :
        print("Escriba 'E' si desea dejar de Multiplicar numeros ")
        x = 'S'
        y = 1
        while x != 'E':

            x = input("Ingrese numero a multiplicar : ")
            if x != 'E':
                y *= int(x)
        print(y)
    def dividir(self):
        print("Escriba 'E' si desea dejar de Dividir numeros ")
        x = input("Ingrese numero a dividir : ")
        if x == 'E':
            print(0)
            return
        y = int(x)
        while True:
            x = input("Ingrese numero a dividir : ")
            if x == 'E':
                break
            try:
                y /= int(x)
            except ZeroDivisionError:
                print("SYNTAX ERROR")
                y="ERROR"
                return

        print(y)

Texas=calculadora()
Texas.sumar()
Texas.resta()
Texas.multiplicar()
Texas.dividir()
