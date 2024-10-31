class Libro:
    def __init__(self,titulo : str,autor : str,year,paginas):
        self.titulo=titulo
        self.autor=autor
        self.year=year
        self.paginas=paginas
    def mostrar_informacion(self):
        print(f"Este libro se llama {self.titulo} creado por {self.autor}"
              f" en el año {self.year}, y contiene {self.paginas} paginas.")

Librito = (
    Libro(titulo="Las Aventuras de Carlitos",
          autor='Carlos Montoya',
          year=2018,
          paginas=669))
Librito.mostrar_informacion()