#Harol Felipe Sánchez Cano
class Pelicula:
    def __init__(self, codigo=0, titulo="", duracion=0, director="", prestada=False):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__duracion = duracion
        self.__director = director
        self.__prestada = prestada

    def get_codigo(self):
        return self.__codigo

    def get_titulo(self):
        return self.__titulo

    def get_duracion(self):
        return self.__duracion

    def get_director(self):
        return self.__director

    def is_prestada(self):
        return self.__prestada

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_duracion(self, duracion):
        self.__duracion = duracion

    def set_director(self, director):
        self.__director = director

    def set_prestada(self, prestada):
        self.__prestada = prestada

    def prestar(self):
        if not self.__prestada:
            self.__prestada = True
            return "La película ha sido prestada."
        else:
            return "La película ya estaba prestada."

    def devolver(self):
        if self.__prestada:
            self.__prestada = False
            return "La película ha sido devuelta."
        else:
            return "La película no estaba prestada."

    def costo_reproduccion(self, tarifa_por_minuto):
        return self.__duracion * tarifa_por_minuto

    def __str__(self):
        estado = "está prestada" if self.__prestada else "no está prestada"
        return (f"La película {self.__codigo} titulada \"{self.__titulo}\" dirigida por {self.__director} "
                f"dura {self.__duracion} minutos y {estado}.")

    def __eq__(self, otra_pelicula):
        if isinstance(otra_pelicula, Pelicula):
            return self.__codigo == otra_pelicula.get_codigo()
        return False

if __name__ == "__main__":
    peli1 = Pelicula(101, "Interstellar", 169, "Christopher Nolan")
    peli2 = Pelicula(102, "Inception", 148, "Christopher Nolan")
    peli3 = Pelicula(101, "Interstellar - Edición Especial", 169, "Christopher Nolan")

    print(peli1)
    print(peli2)
    print(peli3)

    print(peli1.prestar())
    print(peli1.prestar())
    print(peli1.devolver())

    print("Costo de reproducción:", peli2.costo_reproduccion(8000))

    print("¿peli1 y peli3 tienen el mismo código?", peli1 == peli3)
