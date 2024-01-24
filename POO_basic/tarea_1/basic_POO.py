class vehiculos:

    def __init__(self, color:str, marca:str, año:int) -> None:
        ''' Constructor de la clase vehiculos  '''
        self.color: str = color
        self.marca: str = marca
        self.año: int = año
        self.numero_de_ruedas: int = 0
        self.gasolina:bool = False

    def __str__(self) -> str:
        ''' Dunder Method or Magic Method
            Retorna la representación de mi objeto en STR 
        '''
        return f'El vehículo color {self.color} es de la marca {self.marca} del año {self.año}'
    
    def set_ruedas(self, numero_de_ruedas) -> None:
        ''' Define el número de ruedas que tiene el vehículo'''
        self.numero_de_ruedas = numero_de_ruedas

    def get_ruedas(self) -> int:
        ''' Regresa el numero de ruedas que tiene el vehiculo '''
        return self.numero_de_ruedas

    def llenar_gas(self) -> bool:
        ''' Retorna True para confirmar que se lleno de gas el vehículo '''
        self.gasolina = True
        return True
    
    def mover_vehiculo(self, distancia:int) -> str:
        ''' Método que regresa un string, que esta avisando si su vehiculo se movió correctamente o no '''
        if self.gasolina == True and distancia > 100:
            self.gasolina = False
            return f'El vehículo se ha movido una distancia de {distancia} km, se quedo sin gas el vehículo '
        
        elif self.gasolina == True and distancia <= 100:
            return f'El vehículo se ha movido una distancia de {distancia} km'
        
        else:
            return f'El vehículo no se pudo mover ya que se quedo sin gas'

carro = vehiculos('gris', 'honda', 2022)
print(carro)
print(carro.get_ruedas())
carro.set_ruedas(4)
print(carro.get_ruedas())
print(carro.llenar_gas())
print(carro.mover_vehiculo(101))
print(carro.mover_vehiculo(10))