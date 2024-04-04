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

    def agregar_ingredientes(self, Ingrediente) -> None:
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

    @abstractmethod
    def preparar_masa(self) -> None:
        self.estructura.agregar_ingrediente("Masa")

    @abstractmethod
    def agregar_salsa(self) -> None:
        self.estructura.agregar_ingrediente("Salsa")

    @abstractmethod
    def agregar_queso(self) -> None:
        self.estructura.agregar_ingrediente("Queso")

    @abstractmethod
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

    def __init__(self, constructor: PizzeriaBuilder) -> None:
        self._constructor = constructor

    @property
    def producto(self) -> PizzeriaBuilder:
        return self._producto

    @producto.setter
    def producto(self, producto: PizzeriaBuilder) -> None:
        self._producto = producto

    def descripcion(self, nombre_modelo):
        print(f"-I- Preparando orden de{nombre_modelo}")

    def construirPizza(self) -> None:
        self._constructor.preparar_masa()
        self._constructor.agregar_salsa()
        self._constructor.agregar_queso()
        self._constructor.agregar_ingrediente("Pepperoni")
        self._constructor.orilla_rellena("Queso")

    def construirCalzone(self) -> None:
        self._constructor.preparar_masa()
        self._constructor.agregar_salsa()
        self._constructor.agregar_queso()
        self._constructor.agregar_ingrediente("Pepperoni")
        self._constructor.cerrar_calzone()

    def obtener_estructura(self) -> Estructura:
        return self._constructor.estructura


class Hawaiana:

    def __init__(self, constructor: PizzeriaBuilder) -> None:
        self._constructor = constructor

    @property
    def producto(self) -> PizzeriaBuilder:
        return self._producto

    @producto.setter
    def producto(self, producto: PizzeriaBuilder) -> None:
        self._producto = producto

    def descripcion(self, nombre_modelo):
        print(f"-I- Preparando orden de{nombre_modelo}")

    def construirPizza(self) -> None:
        self._constructor.preparar_masa()
        self._constructor.agregar_salsa()
        self._constructor.agregar_queso()
        self._constructor.agregar_ingrediente("Piña")
        self._constructor.agregar_ingrediente("Jamón")
        self._constructor.orilla_rellena("Queso")

    def construirCalzone(self) -> None:
        self._constructor.preparar_masa()
        self._constructor.agregar_salsa()
        self._constructor.agregar_queso()
        self._constructor.agregar_ingrediente("Piña")
        self._constructor.agregar_ingrediente("Jamón")
        self._constructor.cerrar_calzone()

    def obtener_estructura(self) -> Estructura:
        return self._constructor.estructura


if __name__ == "__main__":

    print("hola")
