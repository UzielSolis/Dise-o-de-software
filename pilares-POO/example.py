# 25 de enero de 2024, los cuatro pilares de POO
from __future__ import annotations
from abc import ABC

class TransporteAereo(ABC):
    ''' Interface de cualquier transporte aereo '''

    def volar(self) -> str:
        return 'volando...'

class Avion(TransporteAereo):
    ''' Subclase avion '''

    def __init__(self) -> None:
        self.color: str = "blanco"
        self.marca: str = "airbus"

    def volar(self) -> str:
        return super().volar() + ' el avion'

class Helicoptero(TransporteAereo):
    ''' Subclase helicoptero '''

    def __init__(self) -> None:
        self.potencia: str = "800hp"

    def volar(self) -> str:
        return super().volar() + ' el helicoptero'

class DronParaHumanos(TransporteAereo):
    ''' Clase principal del drone para humanos '''

    def __init__(self) -> None:
        self.numero_asientos: int = 2

    def volar(self) -> str:
        return super().volar() + ' el dron para humanos'

class AvionPapel(TransporteAereo):
    ''' clase aislada de la interface '''
    pass

class Aeropuerto:
    ''' clase que consume transportes aereos '''

    def aceptar(self, transporte: TransporteAereo) -> bool:
        ''' Retorna True si el transporte pertenece a TransporteAereo,
        en ese caso, puede aterrizar '''
        return isinstance(transporte, TransporteAereo)
    
    def volar(self, transporte: TransporteAereo) -> None:
        ''' Se asume que los objetos del aeropuerto pueden volar '''
        if self.aceptar(transporte):
            return transporte.volar()
        else:
            raise Exception('No se puede subir al aeropuerto')
    
avion = Avion()
heli = Helicoptero()
dron = DronParaHumanos()
avion_papel = AvionPapel()

benito_juarez = Aeropuerto()
print(benito_juarez.volar(avion))
print(benito_juarez.volar(heli))
print(benito_juarez.volar(dron))
print(benito_juarez.volar(avion_papel))