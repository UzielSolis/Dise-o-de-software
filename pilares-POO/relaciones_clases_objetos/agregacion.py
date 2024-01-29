class Arma:

    def __init__(self, name:str, damage_points:int) -> None:
        self.name = name
        self.damage_points = damage_points

    def attack(self) -> int:
        return self.damage_points
    
class Superheroe:

    def __init__(self, name:str, vida:int, defensa:int) -> None:
        self.name = name
        self.vida = vida
        self.defensa = defensa
        self.armas = []

    def agregar_arma(self, arma:Arma) -> None:
        self.armas.append(Arma)