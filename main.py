import os
from typing import List

import pygame

pygame.init()

fps = 30
clock = pygame.time.Clock()

tabletop_size = 800

gameDisplay = pygame.display.set_mode((tabletop_size, tabletop_size))

block_size = tabletop_size / 8


class PiecePosition(object):
    def __init__(self, color: str, piece: str, position: str):
        self.color = color
        self.piece = piece
        self.position = position

    def __repr__(self):
        return f"<PiecePosition - color: {self.color} - piece: {self.piece} - position: {self.position} >"


piece_image = {
    "w-P": pygame.image.load(os.path.join("icons", "w-pawn.png")),
    "b-P": pygame.image.load(os.path.join("icons", "b-pawn.png")),
    "w-R": pygame.image.load(os.path.join("icons", "w-rook.png")),
    "b-R": pygame.image.load(os.path.join("icons", "b-rook.png")),
    "w-B": pygame.image.load(os.path.join("icons", "w-bishop.png")),
    "b-B": pygame.image.load(os.path.join("icons", "b-bishop.png")),
    "w-N": pygame.image.load(os.path.join("icons", "w-knight.png")),
    "b-N": pygame.image.load(os.path.join("icons", "b-knight.png")),
    "w-Q": pygame.image.load(os.path.join("icons", "w-queen.png")),
    "b-Q": pygame.image.load(os.path.join("icons", "b-queen.png")),
    "w-K": pygame.image.load(os.path.join("icons", "w-king.png")),
    "b-K": pygame.image.load(os.path.join("icons", "b-king.png")),
}

image_size = 96
center_piece_img = (block_size - 96) / 2

piece_positions: List[PiecePosition] = []

piece_positions.append(PiecePosition(color="w", piece="P", position="a2"))
piece_positions.append(PiecePosition(color="w", piece="P", position="b2"))
piece_positions.append(PiecePosition(color="w", piece="P", position="c2"))
piece_positions.append(PiecePosition(color="w", piece="P", position="d2"))
piece_positions.append(PiecePosition(color="w", piece="P", position="e2"))
piece_positions.append(PiecePosition(color="w", piece="P", position="f2"))
piece_positions.append(PiecePosition(color="w", piece="P", position="g2"))
piece_positions.append(PiecePosition(color="w", piece="P", position="h2"))
piece_positions.append(PiecePosition(color="w", piece="R", position="a1"))
piece_positions.append(PiecePosition(color="w", piece="R", position="h1"))
piece_positions.append(PiecePosition(color="w", piece="B", position="b1"))
piece_positions.append(PiecePosition(color="w", piece="B", position="g1"))
piece_positions.append(PiecePosition(color="w", piece="N", position="c1"))
piece_positions.append(PiecePosition(color="w", piece="N", position="f1"))
piece_positions.append(PiecePosition(color="w", piece="Q", position="d1"))
piece_positions.append(PiecePosition(color="w", piece="K", position="e1"))

piece_positions.append(PiecePosition(color="b", piece="P", position="a7"))
piece_positions.append(PiecePosition(color="b", piece="P", position="b7"))
piece_positions.append(PiecePosition(color="b", piece="P", position="c7"))
piece_positions.append(PiecePosition(color="b", piece="P", position="d7"))
piece_positions.append(PiecePosition(color="b", piece="P", position="e7"))
piece_positions.append(PiecePosition(color="b", piece="P", position="f7"))
piece_positions.append(PiecePosition(color="b", piece="P", position="g7"))
piece_positions.append(PiecePosition(color="b", piece="P", position="h7"))
piece_positions.append(PiecePosition(color="b", piece="R", position="a8"))
piece_positions.append(PiecePosition(color="b", piece="R", position="h8"))
piece_positions.append(PiecePosition(color="b", piece="B", position="b8"))
piece_positions.append(PiecePosition(color="b", piece="B", position="g8"))
piece_positions.append(PiecePosition(color="b", piece="N", position="c8"))
piece_positions.append(PiecePosition(color="b", piece="N", position="f8"))
piece_positions.append(PiecePosition(color="b", piece="Q", position="d8"))
piece_positions.append(PiecePosition(color="b", piece="K", position="e8"))


def letter_to_number(letter):
    if letter.upper() == "A":
        return 0
    if letter.upper() == "B":
        return 1
    if letter.upper() == "C":
        return 2
    if letter.upper() == "D":
        return 3
    if letter.upper() == "E":
        return 4
    if letter.upper() == "F":
        return 5
    if letter.upper() == "G":
        return 6
    if letter.upper() == "H":
        return 7


def number_to_letter(number):
    if number == 0:
        return "a"
    if number == 1:
        return "b"
    if number == 2:
        return "c"
    if number == 3:
        return "d"
    if number == 4:
        return "e"
    if number == 5:
        return "f"
    if number == 6:
        return "g"
    if number == 7:
        return "h"


def get_piece_on_position(position):
    for piece_position in piece_positions:
        if piece_position.position == position:
            return piece_position

    return None


selected_piece = (-1, -1)

turn = "w"

while True:

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            letter = number_to_letter(event.pos[0] // 100)
            number = 8 - (event.pos[1] // 100)
            piece = get_piece_on_position(letter + str(number))

            if piece and piece.color == turn:
                selected_piece = (event.pos[0] // 100, event.pos[1] // 100)
                continue

            if selected_piece[0] != -1:
                # valid movement
                piece_letter = number_to_letter(selected_piece[0])
                piece_number = 8 - (selected_piece[1])
                old_piece = get_piece_on_position(piece_letter + str(piece_number))
                old_piece.position = letter + str(number)

                if piece and piece.color != turn:
                    piece_positions.remove(piece)

                selected_piece = (-1, -1)

                if turn == "w":
                    turn = "b"
                else:
                    turn = "w"

                print(piece_positions)
                continue

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    gameDisplay.fill((128, 128, 128))

    # draw tabletop
    for x in range(0, 8):
        for y in range(0, 8):

            if selected_piece[0] == x and selected_piece[1] == y:
                pygame.draw.rect(
                    gameDisplay,
                    (155, 255, 155),
                    (x * block_size, y * block_size, block_size, block_size),
                    0,
                )

            elif (x + y) % 2 == 0:
                pygame.draw.rect(
                    gameDisplay,
                    (255, 255, 255),
                    (x * block_size, y * block_size, block_size, block_size),
                    0,
                )

    # draw pieces on tabletop
    for piece_position in piece_positions:
        img = piece_image[piece_position.color + "-" + piece_position.piece]

        gameDisplay.blit(
            img,
            (
                (letter_to_number(piece_position.position[0]) * block_size)
                + center_piece_img,
                ((8 - int(piece_position.position[1])) * block_size) + center_piece_img,
            ),
        )

    pygame.display.update()