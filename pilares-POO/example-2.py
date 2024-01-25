# 25 de enero de 2024, los cuatro pilares de POO
from __future__ import annotations
from abc import ABC, abstractmethod

class Animal(ABC):
    ''' clase abstracta '''

    #@abstractmethod
    def hacer_sonido(self) -> str:
        ''' Retorna el sonido del animalito '''
        return self.sonido

class Gato(Animal):
    ''' Subclase de la clase abstracta Animal '''

    def __init__(self) -> None:
        self.sonido = "meow!"
    
class Perro(Animal):
    ''' otra subclase de animal '''

    def __init__(self) -> None:
        self.sonido = "woof!"

    
tom = Gato()
benji = Perro()

for animal in [tom, benji, Gato()]:
    print(animal.hacer_sonido())