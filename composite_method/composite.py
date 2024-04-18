from abc import ABC
from random import randrange


# Interfase del componente
class Elemento(ABC):
    """Interfase del elemento componente"""

    def costo(self) -> int:
        """Retorna el costo en entero del elemento en la estructura de arbol"""
        pass

    def mostrar(self, indent: int = 0) -> str:
        """Muestra la estructura de arbol a partir de este elemento"""
        pass


class Videojuego(Elemento):
    """Clase que representa el último elemento de la estructura de arbol"""

    COSTO_MIN = 1000
    COSTO_MAX = 2000

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self._costo = randrange(Videojuego.COSTO_MIN, Videojuego.COSTO_MAX)

    def costo(self) -> int:
        """Retorna el costo en entero del elemento en la estructura de arbol"""
        return self._costo

    def mostrar(self, indent: int = 0) -> str:
        """Muestra la estructura de arbol a partir de este elemento"""
        return (
            " " * indent + "- " + self.nombre + " $" + str(self._costo) + "\n"
        )


# Composite (Contenedor)
class Compañia(Elemento):
    """Clase composite que contiene elementos"""

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre
        self.hijos: list = []

    def agregar(self, elemento: Elemento) -> None:
        """Agrega elementos a nuestra estructura de arbol"""
        self.hijos.append(elemento)

    def eliminar(self, elemento: Elemento) -> None:
        """Remueve elementos del composite"""
        self.hijos.remove(elemento)

    def costo(self) -> int:
        """Retorna el costo en entero del elemento en la estructura de arbol"""
        costo_total = 0
        for hijo in self.hijos:
            costo_total += hijo.costo()
        return costo_total

    def mostrar(self, indent: int = 0) -> str:
        """Muestra la estructura de arbol a partir de este elemento"""
        detalle_hijos = " " * indent + "+ " + self.nombre + "\n"
        for hijo in self.hijos:
            detalle_hijos += " " * indent + hijo.mostrar(indent + 2)
        return detalle_hijos


if __name__ == "__main__":
    compañias = Compañia("Compañias de videojuegos")
    xbox = Compañia("Xbox")
    playstation = Compañia("PlayStation")
    nintendo = Compañia("Nintendo")
    microsoft = Compañia("Microsoft")
    blizzard = Compañia("Blizzard")

    microsoft.agregar(xbox)

    xbox.agregar(Videojuego("Halo"))
    xbox.agregar(Videojuego("Gears of War"))
    xbox.agregar(Videojuego("Forza Horizon"))

    playstation.agregar(Videojuego("God of War"))
    playstation.agregar(Videojuego("The Last of Us"))
    playstation.agregar(Videojuego("Uncharted"))

    nintendo.agregar(Videojuego("Mario Kart"))
    nintendo.agregar(Videojuego("Zelda"))
    nintendo.agregar(Videojuego("Smash Bros"))

    compañias.agregar(xbox)
    compañias.agregar(playstation)
    compañias.agregar(nintendo)
    compañias.agregar(microsoft)

    print(microsoft.mostrar())
    print(microsoft.costo())
