from abc import ABC, abstractmethod
from enum import Enum


# 3.- Productos
# Los Productos son los objetos resultantes.
# Los productos construidos por distintos objetos constructores no tienen que
# pertenecer a la misma jerarquía de clases o interfaz.
class Estructura(ABC):
    def __init__(self, descripcion: str = None) -> None:
        self._ingredientes = []
        self._descripcion = descripcion

    @property
    def descripcion(self) -> str:
        return self.descripcion

    @property
    def Ingredientes(self) -> list:
        return self._ingredientes

    @descripcion.setter
    def descripcion(self, valor):
        self._descripcion = valor

    def agregar_ingrediente(self, Ingrediente) -> None:
        print(f"-I- Colocando {Ingrediente}...")
        self._ingredientes.append(Ingrediente)

    def __str__(self) -> None:
        return self._descripcion


class PizzaCuadrada(Estructura):
    def __init__(self):
        super().__init__("Pizza cuadrada")


class PizzaCircular(Estructura):
    def __init__(self):
        super().__init__("Pizza circular")


class Calzone(Estructura):
    def __init__(self):
        super().__init__("Calzone")


# 1- Interface constructora (Builder)
# La interfaz Constructora declara pasos de construcción de producto que todos
# los tipos de objetos constructores tienen en común.
class PizzeriaBuilder(ABC):
    @property
    def estructura(self):
        return self._estructura

    def preparar_masa(self) -> None:
        self.estructura.agregar_ingrediente("Masa")

    def agregar_salsa(self) -> None:
        self.estructura.agregar_ingrediente("Salsa")

    def agregar_queso(self) -> None:
        self.estructura.agregar_ingrediente("Queso")

    def agregar_ingrediente(self, ingrediente: str) -> None:
        self.estructura.agregar_ingrediente(f"{ingrediente}")


# 2.- Constructores concretos
# Los Constructores Concretos ofrecen distintas implementaciones de los pasos
# de construcción. Los constructores concretos pueden crear productos que no
# siguen la interfaz común.
class Pizza(PizzeriaBuilder):

    class FormaPizza(Enum):
        CIRCULAR = PizzaCircular()
        CUADRADA = PizzaCuadrada()

    def __init__(self, tipo: FormaPizza) -> None:
        self._estructura = tipo.value

    def orilla_rellena(self, relleno: str) -> None:
        self.estructura.agregar_ingrediente(f"Orilla rellena de {relleno}")


class Calzone(PizzeriaBuilder):

    def __init__(self) -> None:
        self._estructura = Calzone()

    def cerrar_calzone(self) -> None:
        self.estructura.agregar_ingrediente("Calzone cerrado")


# 4.- Directores
# La clase Directora define el orden en el que se invocarán los pasos de
# construcción, por lo que puedes crear y reutilizar configuraciones específicas
# de los productos.
class Pepperoni:

    def __init__(self) -> None:
        self._producto = None

    @property
    def producto(self) -> PizzeriaBuilder:
        return self._producto

    @producto.setter
    def producto(self, producto: PizzeriaBuilder) -> None:
        self._producto = producto

    def descripcion(self, nombre_modelo):
        print(f"-I- Preparando orden de{nombre_modelo}")

    def construirPizza(self) -> None:
        self.producto.preparar_masa()
        self.producto.agregar_salsa()
        self.producto.agregar_queso()
        self.producto.agregar_ingrediente("Pepperoni")
        self.producto.orilla_rellena("Queso")

    def construirCalzone(self) -> None:
        self.producto.preparar_masa()
        self.producto.agregar_salsa()
        self.producto.agregar_queso()
        self.producto.agregar_ingrediente("Pepperoni")
        self.producto.cerrar_calzone()

    def obtener_estructura(self) -> Estructura:
        return self.producto.estructura


class Hawaiana:

    def __init__(self) -> None:
        self._producto = None

    @property
    def producto(self) -> PizzeriaBuilder:
        return self._producto

    @producto.setter
    def producto(self, producto: PizzeriaBuilder) -> None:
        self._producto = producto

    def descripcion(self, nombre_modelo):
        print(f"-I- Preparando orden de{nombre_modelo}")

    def construirPizza(self) -> None:
        self.producto.preparar_masa()
        self.producto.agregar_salsa()
        self.producto.agregar_ingrediente("Piña")
        self.producto.agregar_ingrediente("Jamón")
        self.producto.orilla_rellena("Queso")

    def construirCalzone(self) -> None:
        self.producto.preparar_masa()
        self.producto.agregar_salsa()
        self.producto.agregar_queso()
        self.producto.agregar_ingrediente("Piña")
        self.producto.agregar_ingrediente("Jamón")
        self.producto.cerrar_calzone()

    def obtener_estructura(self) -> Estructura:
        return self.producto.estructura


if __name__ == "__main__":

    dominos = Pepperoni()

    dominos.producto = Pizza(Pizza.FormaPizza.CIRCULAR)
    dominos.construirPizza()
    print(dominos.obtener_estructura())
