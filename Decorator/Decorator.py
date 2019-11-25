from abc import ABC, abstractmethod

class Pizza(ABC):
    @abstractmethod
    def precio(self):
        pass
class Cliente(Pizza):
    print('Compra Pizza')

class IngredientesExtras(Pizza, ABC):
    def __init__(self, pizza):
        self._pizza = pizza

    @abstractmethod
    def precio(self):
        pass

class ExtraQueso(IngredientesExtras):
    def precio(self):
        self._pizza.precio()
    


class ExtraSalsa(IngredientesExtras):
    def precio(self):
        self._pizza.precio()


class PizzaNormal(Pizza):
    def precio(self):
        print('Precio proporcional a una pizza normal')

def main():
    concrete_pizza = PizzaNormal()
    concrete_pizza_a = ExtraQueso(concrete_pizza)
    concrete_pizza_b = ExtraSalsa(concrete_pizza_a)
    concrete_pizza_b.precio()

if __name__ == "__main__":
    main()
