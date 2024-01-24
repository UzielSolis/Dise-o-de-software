# 18 de enero - POO basic

class Gato:
    ''' Esta es una clase simple '''

    NUMERO_DE_COLAS: int = 1
    
    def __init__(self, nombre: str, edad: int, color: str) -> None:
        ''' Constructor de la clase Gato '''
        self.nombre: str = nombre
        self.edad: int = edad
        self.color: str = color

    def __str__(self) -> str:
        ''' Dunder Method or Magic Method
            Retorna la representación de mi objeto en STR 
        '''
        return f'El gato se llama {self.nombre}, tiene {self.edad} años y es de color {self.color}'    

    @classmethod
    def set_colas(cls, numero_de_colas: int) -> None:
        ''' Define el numero de colas para todos los Gatos '''
        cls.NUMERO_DE_COLAS = numero_de_colas

    @staticmethod
    def puedo_jugar(hh24:int) -> bool:
        ''' Retorna True si mi gato puede jugar dependiendo de la hora  '''
        if hh24 > 7 and hh24 < 18:
            return True
        else:
            return False

    def comer(self, comida:str) -> str:
        ''' Retorna un string de que esta comiendo el gato '''
        return f'El gato {self.nombre} esta comiendo {comida}'

tom = Gato('Tom', 5, 'gris')
print(tom.puedo_jugar(8))

print(tom.comer('pollo'))