from __future__ import annotations

class Canal:

    CANAL = 1

    def __init__(self, name:str) -> None:
        self.name: str = name

    @staticmethod
    def broadcast():
        return "Broadcasting a channel"
    
    def changing_channel(self) -> int:
        self.CANAL += 1
        return self.CANAL

class Videocasetera:

    def __init__(self, disk:str) -> None:
        self.disk: str = disk

    def useChannel(self):
        return Canal.broadcast()  # Función que esta dependiendo de un método de la clase Canal
    
    def getChannel(self):
        return Canal.CANAL

vcr = Videocasetera("disk1")
print(vcr.useChannel())
print(vcr.getChannel())