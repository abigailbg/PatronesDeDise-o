from abc import ABC, abstractmethod

class Guitarra(ABC):
    @abstractmethod
    def tocar(self):
        pass
class GuitarraSencilla(Guitarra):
    def tocar(self):
        pass

class GuitarraAcustica(Guitarra):
    def tocar(self):
        pass

class GuitarraElectrica:
    def grave (self):
        pass
    def agudo(self):
        pass

class GuitarraElectricaAdapter(Guitarra):
    def __init__(self):
        self._guitarraelectrica = GuitarraElectrica()
    def tocar(self):
       pass

class Concierto():
    def __init__(self):
        self.steven = GuitarraSencilla()
        self.saul = GuitarraAcustica()
        self.hector = GuitarraElectricaAdapter()
      


