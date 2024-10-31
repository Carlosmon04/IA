class Rectangulo:
    def __init__(self,base : float,altura : float):
        self.base=base
        self.altura=altura
    def area(self):
        a= self.base*self.altura
        print(a)
    def Perimetro(self):
        p= (self.base*2)+(self.altura*2)
        print(p)

rectangulo1=Rectangulo(base=5, altura=3)
rectangulo1.area()
rectangulo1.Perimetro()
