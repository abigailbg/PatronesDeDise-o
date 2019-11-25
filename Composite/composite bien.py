from abc import ABC, abstractmethod
class Peliculas(ABC):
    @abstractmethod
    def reproduccion(self):
        pass
class Usuario(Peliculas):
    print('Preparado para reproducir pelicula')
    
class AlbumPeliculas(Peliculas):
    def __init__(self):
        self._children = set()
    def reproduccion(self):
        for child in self._children:
            child.reproduccion()
    def add(self, peliculas):
        self._children.add(peliculas)
    def remove(self, peliculas):
        self._children.discard(peliculas)

class Movie(Peliculas):
    def reproduccion(self):
        print('Reproducción solo sin entrar a tu Album')

def main():
    movie = Movie()
    album = AlbumPeliculas()
    album.add(movie)
    album.reproduccion()

if __name__ == "__main__":
    main()
