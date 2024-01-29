class Empresa:

    def __init__(self, name:str) -> None:
        self.name = name

class Persona:

    def __init__(self, nombre:str, empresa:Empresa) -> None:
        self.nombre = nombre
        self.empresa = empresa  # Aqui esta la asociación

    def get_work(self) -> str:
        return self.empresa.name
    
empresa = Empresa("oracle")
humano = Persona("uziel", empresa)
print(humano.get_work())