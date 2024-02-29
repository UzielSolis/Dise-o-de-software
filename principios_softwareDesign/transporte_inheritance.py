from __future__ import annotations
from abc import ABC

class Transporte():
    def __init__(self, motor:Motor, chofer:Chofer):
        '''Constructor de la clase Transporte'''
        if motor == 'combustion':
            self.motor = MotorCombustion()
        elif motor == 'electrico':
            self.motor = MotorElectrico()
        else:
            raise ValueError('Motor no valido')

        self.chofer = chofer

    def entregar(self, destino, carga) -> str:
        '''Entrega la carga en el destino'''
        return (f'Entregando {carga} en {destino}')
    
# Motores
class Motor(ABC):

    def mover(self) -> None:
        '''Mover motor'''

class MotorCombustion(Motor):

    def mover(self) -> str:
        '''Mover motor de combustion'''
        return 'Mover motor de combustion'
    
class MotorElectrico(Motor):

    def mover(self) -> str:
        '''Mover motor electrico'''
        return 'Mover motor electrico'
    
# Chofer
class Chofer(ABC):

    def manejar(self) -> None:
        '''Manejar'''

class Robot(Chofer):

    def manejar(self) -> str:
        '''Manejar robot'''
        return 'Manejar robot'
    
class Humano(Chofer):

    def manejar(self) -> str:
        '''Manejar persona'''
        return 'Manejar Humano'

# Ejemplo de uso
chofer_1 = Humano()

prius = Transporte('combustion', chofer_1)
print(prius.entregar('GDL', 'carro'))
print(prius.motor.mover())
print(prius.chofer.manejar())