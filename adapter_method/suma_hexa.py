# Esta implementación utiliza la herencia, porque la clase adaptadora hereda
# de ambos objetos al mismo tiempo. Ten en cuenta que esta opción sólo puede
# implementarse en lenguajes de programación que soporten la herencia múltiple

# Clase principal en funcionamiento
from abc import ABC


class Entero(ABC):
    @classmethod
    def sumar(cls, *numeros: int) -> int:
        """Suma n cantidad de números enteros"""
        suma = 0
        for numero in numeros:
            suma += numero
        return suma


# Adapter
class HexadecimalToEntero(Entero):
    @classmethod
    def sumar(cls, *numeros: str) -> int:
        """Suma n cantidad de números hexadecimales"""
        suma = 0
        for numero in numeros:
            # Convertir de hexadecimal a entero antes de sumar
            suma += int(numero, 16)
        return suma


if __name__ == "__main__":
    print(f"La suma de 1 + 2 + 3 = {Entero.sumar(1, 2, 3)}")
    # Debes pasar al menos un número hexadecimal como argumento, por ejemplo:
    print(
        f'La suma hexa de 0xA + 0x2 + 0x3 = {HexadecimalToEntero.sumar("0xA", "0x2", "0x3")}'
    )
