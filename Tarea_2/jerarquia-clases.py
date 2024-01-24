class Character:
    ''' Crea un objeto del tipo personaje '''

    LIFE = 100

    def __init__(self, name:str, gender:str, raza:str, age:int) -> None:
        ''' Constructor de la clase Character '''
        self.name : str = name
        self.gender : str = gender
        self.raza : str = raza
        self.age : int = age

    def detalles(self) -> str:
        ''' Regresa los detalles asociados a un personaje '''
        return '{} es un personaje {} de {} años, cuya raza es {}.'.format(
            self.name,
            self.gender,
            self.age,
            self.raza
        )
    
    def move(self) -> bool:
        ''' Regresa True para indicar que se movio el personaje '''
        return True
    
    def attack(self, arma:str) -> int:
        ''' Regresa la cantidad de damage que hizo el personaje '''
        if arma == "sword":
            return 10
        elif arma == "Bow":
            return 6
        elif arma == "dagger":
            return 5
        else:
            return 2
    
    @classmethod
    def takingDamage(cls) -> str:
        ''' Se retorna el valor que sufrio el personaje al recibir un ataque '''
        tmp = cls.LIFE
        return f'El personaje sufrio 10 de daño, {tmp} - 10 = {(tmp - 10)}'

class Berserker(Character):
    ''' Crea un objeto del tipo berserker '''

    LIFE = 150

    def __init__(self, name: str, gender: str, raza: str, age: int, height:str, shield:bool) -> None:
        ''' Constructor de la clase berserker '''
        super().__init__(name, gender, raza, age)
        self.height : str = height
        self.shield : bool = shield

    def charge(self) -> int:
        ''' Metodo que regresa la cantidad de damage que hizo la habilidad '''
        return super().attack('sword') + 10
    
    def scream(self) -> str:
        ''' Metodo que regresa cuanta vida recupero el berserker '''
        return f'Berserker ha recuperado 50 puntos de vida'

user = Berserker("Casca", "women", "Human", 25, 170, False)
print(user.detalles())
print(user.takingDamage())
print(user.move())
print(user.attack('sword'))
print(user.charge())
print(user.scream())