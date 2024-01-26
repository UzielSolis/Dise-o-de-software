from __future__ import annotations
from abc import ABC, abstractmethod

class Figura:

    @abstractmethod
    def perimetro(base, altura) -> float:
        ''' Retorna el perimetro de la figura '''

    @abstractmethod
    def area(base, altura) -> float:
        ''' Retorna el area de la Figura '''

class Rectangulo(Figura):
    ''' Clase para los rectángulos '''

    def __init__(self, base : float, altura : float) -> None:
        ''' Constructor que recibe base y altura del rectángulo '''

        self.base : float = base
        self.altura : float = altura

    def perimetro(self) -> float:
        ''' Regresa el perimetro del rectángulo, base*2 + altura*2 '''
        return ((self.base*2) + (self.altura*2))

    def area(self) -> float:
        ''' Regresa el área del rectángulo, base*altura '''
        return self.base*self.altura

class Triangulo(Figura):
    ''' Clase para los triángulos '''

    def __init__(self, base : float, altura : float) -> None:
        ''' Constructor que recibe base y altura del triángulo '''

        self.base : float = base
        self.altura : float = altura

    def perimetro(self) -> float:
        ''' Regresa el perimetro del triángulo, 
        Se toma en cuenta que los lados laterales del triangulo son iguales '''
        return (self.altura*2) + self.base

    def area(self) -> float:
        ''' Regresa el área del triángulo, (base*altura)/2 '''
        return (self.base*self.altura) / 2

class Circulo(Figura):
    ''' Clase para los circulos '''

    def __init__(self, radio : float) -> None:
        ''' Constructor que recibe el radio del circulo '''

        self.Pi : float = 3.1416
        self.radio : float = radio

    def perimetro(self) -> float:
        ''' Regresa el perimetro del circulo, 2*Pi*radio'''
        return 2*self.Pi*self.radio

    def area(self) -> float:
        ''' Regresa el área del ciruclo, Pi*r al cuadrado'''
        return self.Pi*(self.radio**2)

rectangulo = Rectangulo(24.5, 12.5)
triangulo = Triangulo(15.6, 18.9)
circulo = Circulo(7.5)

for figuras in [rectangulo, triangulo, circulo]:
    print(figuras.perimetro())
    print(figuras.area())