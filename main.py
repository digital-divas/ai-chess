import os
from typing import List

import pygame

pygame.init()

fps = 30
clock = pygame.time.Clock()

tabletop_size = 800

gameDisplay = pygame.display.set_mode((tabletop_size, tabletop_size))
pygame.display.set_caption("ai-chess")

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


def get_valid_movements(piece):

    valid_movements = []

    if piece.piece.upper() == "P" and piece.color == "w":
        if piece.position[1] == "2":
            valid_movements.append(piece.position[0] + "3")
            valid_movements.append(piece.position[0] + "4")
        else:
            valid_movements.append(piece.position[0] + str(int(piece.position[1]) + 1))

    if piece.piece.upper() == "P" and piece.color == "b":
        if piece.position[1] == "7":
            valid_movements.append(piece.position[0] + "6")
            valid_movements.append(piece.position[0] + "5")
        else:
            valid_movements.append(piece.position[0] + str(int(piece.position[1]) - 1))

    if piece.piece.upper() == "N":
        x = letter_to_number(piece.position[0])
        y = piece.position[1]

        possibilities = [
            (int(x) + 2, int(y) + 1),
            (int(x) + 1, int(y) + 2),
            (int(x) - 2, int(y) + 1),
            (int(x) - 1, int(y) + 2),
            (int(x) - 2, int(y) - 1),
            (int(x) - 1, int(y) - 2),
            (int(x) + 2, int(y) - 1),
            (int(x) + 1, int(y) - 2),
        ]

        for possibility in possibilities:

            if possibility[1] < 1 or possibility[1] > 8:
                continue

            if possibility[0] < 0 or possibility[0] > 7:
                continue

            position = number_to_letter(possibility[0]) + str(possibility[1])

            target_piece = get_piece_on_position(position)

            if target_piece and target_piece.color == piece.color:
                continue

            valid_movements.append(position)

    if piece.piece.upper() == "R":
        x = letter_to_number(piece.position[0])
        y = int(piece.position[1])

        target_x = x - 1

        while target_x >= 0:
            target_letter = number_to_letter(target_x)
            position = target_letter + str(y)

            target_piece = get_piece_on_position(position)

            if target_piece is not None:
                if target_piece.color != piece.color:
                    valid_movements.append(position)
                break

            valid_movements.append(position)

            target_x -= 1

        target_x = x + 1

        while target_x <= 7:
            target_letter = number_to_letter(target_x)

            position = target_letter + str(y)

            target_piece = get_piece_on_position(position)

            if target_piece is not None:
                if target_piece.color != piece.color:
                    valid_movements.append(position)
                break

            valid_movements.append(position)

            target_x += 1

        target_y = y - 1

        while target_y >= 1:
            target_letter = number_to_letter(x)
            position = target_letter + str(target_y)

            target_piece = get_piece_on_position(position)

            if target_piece is not None:
                if target_piece.color != piece.color:
                    valid_movements.append(position)
                break

            valid_movements.append(position)

            target_y -= 1

        target_y = y + 1

        while target_y <= 8:
            target_letter = number_to_letter(x)

            position = target_letter + str(target_y)

            target_piece = get_piece_on_position(position)

            if target_piece is not None:
                if target_piece.color != piece.color:
                    valid_movements.append(position)
                break

            valid_movements.append(position)

            target_y += 1

    return valid_movements


selected_piece = (-1, -1)
valid_movements = []

turn = "w"

while True:

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            letter = number_to_letter(event.pos[0] // 100)
            number = 8 - (event.pos[1] // 100)
            piece = get_piece_on_position(letter + str(number))

            if piece and piece.color == turn:
                selected_piece = (event.pos[0] // 100, event.pos[1] // 100)
                valid_movements = get_valid_movements(piece)
                continue

            if selected_piece[0] != -1:

                if letter + str(number) not in valid_movements:
                    continue

                piece_letter = number_to_letter(selected_piece[0])
                piece_number = 8 - (selected_piece[1])
                old_piece = get_piece_on_position(piece_letter + str(piece_number))
                old_piece.position = letter + str(number)

                if piece and piece.color != turn:
                    piece_positions.remove(piece)

                selected_piece = (-1, -1)
                valid_movements = []

                if turn == "w":
                    turn = "b"
                else:
                    turn = "w"

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

    for valid_movement in valid_movements:
        x = letter_to_number(valid_movement[0])
        y = 8 - int(valid_movement[1])
        position = (
            int((x * block_size) + (block_size / 2)),
            int((y * block_size) + (block_size / 2)),
        )
        pygame.draw.circle(
            gameDisplay,
            (100, 150, 100),
            position,
            14,
        )
        pygame.draw.circle(
            gameDisplay,
            (0, 0, 0),
            position,
            15,
            1,
        )

    pygame.display.update()