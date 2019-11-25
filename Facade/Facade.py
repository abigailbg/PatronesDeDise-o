#Este trata de un Menu de una fonda el cual tiene dos submenus, y estos a su vez se dividen en dos en el clasico o el especial de la fonda; ayua a que el
#consumidor realice elija de una manera más sencilla ya que esta dividida en subsecciones.
class MenuFonda:
    def __init__(self):
        self._submenu_1 = Submenu1()
        self._submenu_2 = Submenu2()

    def tipos(self):
        self._submenu_1.clasico1()
        self._submenu_1.especial2()
        self._submenu_2.clasico1()
        self._submenu_2.especial2()


class Submenu1:
    def clasico1(self):
        print('Este es el munú clasico del submenu uno de la fonda')
    def especial2(self):
        print('Este es el munú especial del submenu uno de la fonda')


class Submenu2:
    def clasico1(self):
        print('Este es el munú clasico del submenu dos de la fonda')
    def especial2(self):
        print('Este es el munú especial del submenu dos de la fonda')


def main():
    menu = MenuFonda()
    menu.tipos()

if __name__ == "__main__":
    main()
