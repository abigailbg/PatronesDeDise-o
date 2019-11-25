from abc import ABC, abstractmethod

class CulpableNoCulpable:
    def __init__(self):
        self._observers = set()
        self._subject_state = None

    def attach(self, juez):
        juez._subject = self
        self._observers.add(juez)

    def detach(self, juez):
        juez._subject = None
        self._observers.discard(juez)

    def _notify(self):
        for juez in self._observers:
            juez.update(self._subject_state)

    @property
    def subject_state(self):
        return self._subject_state

    @subject_state.setter
    def subject_state(self, arg):
        self._subject_state = arg
        self._notify()


class Juez(ABC):

    def __init__(self):
        self._subject = None
        self._juez_state = None

    @abstractmethod
    def update(self, arg):
        pass
    
class Individuo(Juez):
    print('Persona que será juzgada por un Juez')


class Jurado(Juez):

    def update(self, arg):
        self._juez_state = arg

def main():
    subject = CulpableNoCulpable()
    concrete_juez = Jurado()
    subject.attach(concrete_juez)
    subject.subject_state = 123


if __name__ == "__main__":
    main()
