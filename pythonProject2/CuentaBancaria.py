class CuentaBancaria:
    saldo=0
    def __init__(self,titular):
        self.titular=titular

    def Depositar(self,valor):
        self.saldo=self.saldo+valor
        print(f"Se han Depositado {valor} a {self.titular}")

    def Retirar(self,valor):
        if valor<0:
            print("No Aceptamos Cantidades negativas")
        else:
         if self.saldo>=valor:
            self.saldo=self.saldo-valor
            print(f"Se han Retirado {valor} a {self.titular}")
         else:
            print('No hay Fondos para retirar esa cantidad')

    def mostrar_saldo(self):
        print(f"Monto de Cuenta : {self.saldo}")

cuenta=CuentaBancaria("Xiomara")
cuenta.mostrar_saldo()
cuenta.Depositar(5)
cuenta.Retirar(2)
cuenta.mostrar_saldo()
cuenta.Depositar(5)
cuenta.mostrar_saldo()
cuenta.Retirar(2)
cuenta.mostrar_saldo()
cuenta.Retirar(7)
