from abc import ABC, abstractmethod


# -----------------------------------------------------------------------------
# 1.- Interface (Componente)
# -----------------------------------------------------------------------------
# Es opcional
# El Componente declara la interfaz común tanto para wrappers como para objetos
# envueltos
# -----------------------------------------------------------------------------
class Etiquetas(ABC):
    @abstractmethod
    def usar(self) -> str:
        pass


# -----------------------------------------------------------------------------
# 2.- Componentes Concretos
# -----------------------------------------------------------------------------
# Componente Concreto es una clase de objetos envueltos. Definen el
# comportamiento básico, que los decoradores pueden alterar
# -----------------------------------------------------------------------------
class Html(Etiquetas):
    def usar(self) -> str:
        return "{}"


# -----------------------------------------------------------------------------
# 3.- Clase Decoradora
# -----------------------------------------------------------------------------
# La clase Decoradora Base tiene un campo para referenciar un objeto envuelto.
# El tipo del campo debe declararse como la interfaz del componente para que
# pueda contener tanto los componentes concretos como los decoradores.
# La clase decoradora base delega todas las operaciones al objeto envuelto.
# -----------------------------------------------------------------------------
class Decorator:

    def __init__(self, etiquetas: Etiquetas) -> None:
        self._etiquetas = etiquetas

    @property
    def etiqueta(self) -> str:
        return self._etiquetas


# -----------------------------------------------------------------------------
# 4.- Decoradores Concretos
# -----------------------------------------------------------------------------
# Los Decoradores Concretos definen funcionalidades adicionales que se pueden
# añadir dinámicamente a los componentes. Los decoradores concretos sobrescriben
# métodos de la clase decoradora base y ejecutan su comportamiento, ya sea antes
# o después de invocar al método padre.
# -----------------------------------------------------------------------------
class Bold(Decorator):
    def usar(self) -> str:
        return "<strong>{}</strong>".format(self.etiqueta.usar())


class Italic(Decorator):
    def usar(self) -> str:
        return "<i>{}</i>".format(self.etiqueta.usar())


class Underline(Decorator):
    def usar(self) -> str:
        return "<u>{}</u>".format(self.etiqueta.usar())


# -----------------------------------------------------------------------------
# Cliente
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    texto_1 = Html()
    texto_2 = Html()
    texto_3 = Html()
    texto_4 = Html()

    negrita = Bold(texto_1)
    print(negrita.usar())

    italica = Italic(texto_2)
    print(italica.usar())

    subrayado = Underline(texto_3)
    print(subrayado.usar())

    negrita_italica = Bold(Italic(texto_4))
    print(negrita_italica.usar())
