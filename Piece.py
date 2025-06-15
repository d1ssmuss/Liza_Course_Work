import pygame as pg



pg.init()

# Базовый класс Фигуры, далее от него будем наследоваться...
class Piece:
    def __init__(self, color, position, path_iamge):
        self.color = color  # цвет фигуры, например 'white' или 'black'
        self.path_image = path_iamge # путь спрайта
        self.position = position  # текущая позиция на доске (например, (x, y))
        self.image = self.load_image() # загружаем изображения
        self.rect = self.image.get_rect(center = self.position) # создаем прямоугольник для позиционирования

    def load_image(self):
        """Загружает изображение фигуры и возвращает его."""
        image = pg.image.load(self.path_image).convert_alpha()
        return pg.transform.smoothscale(image, (100, 100))  # масштабируем изображение
    def draw(self, screen):
        """Отображает фигуру на экране."""
        screen.blit(self.image, self.rect)

class King(Piece):

    # направления
    """directions = [
        (1, -1),  (1, 0),   (1, 1),
        (0, -1),           (0, 1),
        (-1, -1), (-1, 0), (-1, 1)
    ]"""
    def get_valid_move(self):
        # pg.draw.circle(screen, (0, 255, 0), (100, 100), 50)
        # я должен здесь получать координаты фигуры и найти координаты доступных ходов(если фигура стоит на клетке как ограждение, то она мешает)
        
        pass
    pass


class Queen(Piece):
    pass


class Knight(Piece):
    pass


class Bishop(Piece):
    pass


class Rook(Piece):
    pass

class Pawn(Piece):
    pass


if __name__ == "__main__":
    k = King("white", (450, 750), "images/wK.png")
