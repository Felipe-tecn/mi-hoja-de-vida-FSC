from pelicula import Pelicula 

def main():

    peli1 = Pelicula(1001, "Lalaland", 128, "Damien Chazelle")
    peli2 = Pelicula(1002, "El Señor de los Anillos", 201, "Peter Jackson")
    peli3 = Pelicula(1001, "Lalaland - Edición Extendida", 190, "Damien Chazelle")

    print(peli1)
    print(peli2)
    print(peli3)

    print(peli1.prestar())
    print(peli1.prestar()) 

    print(peli1.devolver())
    print(peli1.devolver()) 

    tarifa = 8000
    print(f"Costo de reproducción de '{peli2.get_titulo()}': ${peli2.costo_reproduccion(tarifa)}")

    print("¿peli1 y peli3 tienen el mismo código?", peli1 == peli3)

if __name__ == "__main__":
    main()
