"""
12)КАТКОВА ЕЛИЗАВЕТА ДМИТРИЕВНА
Компьютерная игра эндшпиль «Король, 2 слона-Король, конь, пешка»

Белые:  Кр Слон, Слон
Чёрные: Кр Конь, пешка
"""


"""
To do list
- Рисовать точки, куда можно ходить
- ШАХ МАТ ПАТ в центре
"""


import pygame as pg

from Piece import King, Bishop, Knight, Pawn  # Импортируйте необходимые классы
from Board import Board # потом пофиксить
# Initialize pg
pg.init()

# Set the display mode
screen = pg.display.set_mode((800, 800))

# Set the window title
pg.display.set_caption("Эндшпиль_шахматы")


"""FPS = 60        # число кадров в секунду
clock = pg.time.Clock()
"""


# Create board instance
board_instance = Board()
# Mapping from board piece codes to readable names
piece_names = {
    "wK": "Белый Король",
    "wB": "Белый Слон",
    "bK": "Чёрный Король",
    "bN": "Чёрный Конь",
    "bp": "Чёрная Пешка",
    "wQ": "Белая Ферзь",
    "bQ": "Чёрная Ферзь",
    "wR": "Белая Ладья",
    "bR": "Чёрная Ладья",
    # Add others if needed
}


# Main game loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
            col = mouse_x // 100
            row = mouse_y // 100
            print(col,row)
            if 0 <= row < 8 and 0 <= col < 8:
                cell = board_instance.board[row][col]
                if cell == "--":
                    print(f"Позиция ({col}, {row}): пустая клетка")
                else:
                    name = piece_names.get(cell, f"Неизвестная фигура ({cell})")
                    print(f"Позиция ({col}, {row}): {name}")

    # Рисуем клетки фигур
    for x in range(0, 8):
        for y in range(0, 8):
            if (x + y) % 2 == 0:
                pg.draw.rect(screen, (241, 217, 181), (x * 100, y * 100, 100, 100))
            else:
                pg.draw.rect(screen, (181, 135, 99), (x * 100, y * 100, 100, 100))

    """# Отображаем например белого короля
    white_king_image = pg.image.load("images/wK.png").convert_alpha()
    white_king_img = pg.transform.smoothscale(white_king_image, (100, 100))
    white_king_rect = white_king_img.get_rect(center=(450, 750))
    screen.blit(white_king_img, white_king_rect)"""


    white_king = King("white", (450, 750), "images/wK.png")
    black_king = King("black", (450, 50), "images/bK.png")
    white_bishop1 = Bishop("white", (250, 750), "images/wB.png")
    white_bishop2 = Bishop("white", (550, 750), "images/wB.png")
    black_knight = Knight("black", (650, 50), "images/bN.png")
    black_pawn = Pawn("black", (450, 150), "images/bP.png")

    # Отображаем фигуры
    white_king.draw(screen)
    black_king.draw(screen)
    white_bishop1.draw(screen)
    white_bishop2.draw(screen)
    black_knight.draw(screen)
    black_pawn.draw(screen)

    """# Get mouse position
    mouse_pos = pg.mouse.get_pos()
    print(f"Mouse Position: {mouse_pos}")"""

    # clock.tick(FPS)
    # Update the display
    pg.display.flip()

# Quit pg
pg.quit()