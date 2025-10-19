import pygame
from pygame import Surface
import os

pygame.mixer.init()
size = (500,500)
# Chess board
CHESS_BOARD_IMG: Surface = pygame.image.load(os.path.join("Assets", "blue.png"))
CHESS_BOARD: Surface = pygame.transform.scale(CHESS_BOARD_IMG, (600, 600))

# Chess pieces
WHITE_PAWN: Surface = pygame.image.load(os.path.join("Assets", "white-pawn.png"))
WHITE_ROOK: Surface = pygame.image.load(os.path.join("Assets", "white-rook.png"))
WHITE_KNIGHT: Surface = pygame.image.load(os.path.join("Assets", "white-knight.png"))
WHITE_QUEEN: Surface = pygame.image.load(os.path.join("Assets", "white-queen.png"))

WB: Surface = pygame.image.load(os.path.join("Assets", "white-bishop.png"))


WHITE_BISHOP: Surface = pygame.image.load(os.path.join("Assets", "wB.png"))
WHITE_BISHOP: Surface = pygame.transform.smoothscale(WHITE_BISHOP, size=size)
WHITE_KING: Surface = pygame.image.load(os.path.join("Assets", "wK.png"))
WHITE_KING: Surface = pygame.transform.smoothscale(WHITE_KING, size=size)


BLACK_PAWN: Surface = pygame.image.load(os.path.join("Assets", "bp.png"))
BLACK_PAWN: Surface = pygame.transform.smoothscale(BLACK_PAWN, size=size)
BLACK_ROOK: Surface = pygame.image.load(os.path.join("Assets", "bR.png"))
BLACK_ROOK: Surface = pygame.transform.smoothscale(BLACK_ROOK, size=size)
BLACK_KNIGHT: Surface = pygame.image.load(os.path.join("Assets", "bN.png"))
BLACK_KNIGHT: Surface = pygame.transform.smoothscale(BLACK_KNIGHT, size=size)
BLACK_BISHOP: Surface = pygame.image.load(os.path.join("Assets", "bB.png"))
BLACK_BISHOP: Surface = pygame.transform.smoothscale(BLACK_BISHOP, size=size)
BLACK_QUEEN: Surface = pygame.image.load(os.path.join("Assets", "bQ.png"))
BLACK_QUEEN: Surface = pygame.transform.smoothscale(BLACK_QUEEN, size=size)
BLACK_KING: Surface = pygame.image.load(os.path.join("Assets", "bK.png"))
BLACK_KING: Surface = pygame.transform.smoothscale(BLACK_KING, size=size)




# Icons
FLIP_ICON: Surface = pygame.transform.scale(
    pygame.image.load(os.path.join("Assets", "flip-board.png")), (28, 28)
)
ON_BUTTON: Surface = pygame.image.load(os.path.join("Assets", "on-button.png"))
OFF_BUTTON: Surface = pygame.image.load(os.path.join("Assets", "off-button.png"))
RESET_BUTTON: Surface = pygame.image.load(os.path.join("Assets", "reset.png"))

# Sounds
MOVE_SOUND = pygame.mixer.Sound(os.path.join("Assets", "Move.wav"))
