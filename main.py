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

movements_history = []


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

pygame.display.set_icon(piece_image["w-N"])

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
piece_positions.append(PiecePosition(color="w", piece="N", position="b1"))
piece_positions.append(PiecePosition(color="w", piece="N", position="g1"))
piece_positions.append(PiecePosition(color="w", piece="B", position="c1"))
piece_positions.append(PiecePosition(color="w", piece="B", position="f1"))
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
piece_positions.append(PiecePosition(color="b", piece="N", position="b8"))
piece_positions.append(PiecePosition(color="b", piece="N", position="g8"))
piece_positions.append(PiecePosition(color="b", piece="B", position="c8"))
piece_positions.append(PiecePosition(color="b", piece="B", position="f8"))
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


def get_piece_on_position(position, conditional_piece_positions=None):
    if conditional_piece_positions is None:
        conditional_piece_positions = piece_positions

    for piece_position in conditional_piece_positions:
        if piece_position.position == position:
            return piece_position

    return None


def print_tabletop(conditional_piece_positions=None):
    if conditional_piece_positions is None:
        conditional_piece_positions = piece_positions

    cols = ["a", "b", "c", "d", "e", "f", "g", "h"]
    lines = ["8", "7", "6", "5", "4", "3", "2", "1"]

    print()
    for x, line in enumerate(lines):
        for y, col in enumerate(cols):

            piece = get_piece_on_position(col + line, conditional_piece_positions)

            if (x + y) % 2 == 0:
                print(
                    "\033[0;"
                    + ("37" if piece is not None and piece.color == "w" else "30")
                    + ";43m"
                    + " "
                    + (piece.piece if piece is not None else " ")
                    + " "
                    + "\033[0m",
                    end="",
                )
            else:
                print(
                    "\033[0;"
                    + ("37" if piece is not None and piece.color == "w" else "30")
                    + ";42m"
                    + " "
                    + (piece.piece if piece is not None else " ")
                    + " "
                    + "\033[0m",
                    end="",
                )

        print()


def am_i_in_check(my_color, conditional_piece_positions: List[PiecePosition]):

    my_king_position = ""

    for piece_position in conditional_piece_positions:
        if piece_position.color == my_color and piece_position.piece == "K":
            my_king_position = piece_position.position

    for piece_position in conditional_piece_positions:
        if piece_position.color != my_color:
            if piece_position.piece != "P":
                movements = get_valid_movements(
                    piece_position, True, conditional_piece_positions
                )
            else:
                movements = []
                direction = 1
                if piece_position.color == "b":
                    direction = -1

                left_piece = None
                right_piece = None

                number = letter_to_number(piece_position.position[0]) - 1
                if number >= 0:
                    movements.append(
                        number_to_letter(number)
                        + str(int(piece_position.position[1]) + (1 * direction))
                    )

                number = letter_to_number(piece_position.position[0]) + 1
                if number <= 7:
                    movements.append(
                        number_to_letter(number)
                        + str(int(piece_position.position[1]) + (1 * direction))
                    )

            if my_king_position in movements:
                return True

    return False


def get_valid_movements(
    piece, looking_enemy_movements=False, conditional_piece_positions=None
):

    valid_movements = []

    # pawn
    if piece.piece.upper() == "P":

        # direction
        direction = 1
        if piece.color == "b":
            direction = -1

        # default movement ahead
        ## if you are in the initial position, you can move 2 houses/squares
        position = piece.position[0] + str(int(piece.position[1]) + (1 * direction))
        if (
            (piece.color == "w" and piece.position[1] == "2")
            or (piece.color == "b" and piece.position[1] == "7")
        ) and get_piece_on_position(
            position,
            conditional_piece_positions,
        ) is None:

            conditional_piece_positions2 = change_a_piece_position_for_valid_movements(
                piece, position
            )

            if not am_i_in_check(piece.color, conditional_piece_positions2):
                valid_movements.append(position)

            position = piece.position[0] + str(int(piece.position[1]) + (2 * direction))
            if (
                get_piece_on_position(
                    position,
                    conditional_piece_positions,
                )
                is None
            ):
                conditional_piece_positions2 = (
                    change_a_piece_position_for_valid_movements(piece, position)
                )

                if not am_i_in_check(piece.color, conditional_piece_positions2):
                    valid_movements.append(position)

        ## if you aren't on the initial position, you can move only 1 house/square
        elif (
            get_piece_on_position(
                position,
                conditional_piece_positions,
            )
            is None
        ):
            conditional_piece_positions2 = change_a_piece_position_for_valid_movements(
                piece, position
            )

            if not am_i_in_check(piece.color, conditional_piece_positions2):
                valid_movements.append(position)

        # the 'capture' movement
        ## default capture
        left_piece = None
        right_piece = None

        number = letter_to_number(piece.position[0]) - 1
        if number >= 0:
            left_piece = get_piece_on_position(
                number_to_letter(number)
                + str(int(piece.position[1]) + (1 * direction)),
                conditional_piece_positions,
            )

        number = letter_to_number(piece.position[0]) + 1
        if number <= 7:
            right_piece = get_piece_on_position(
                number_to_letter(number)
                + str(int(piece.position[1]) + (1 * direction)),
                conditional_piece_positions,
            )

        if left_piece is not None and left_piece.color != piece.color:

            conditional_piece_positions2 = change_a_piece_position_for_valid_movements(
                piece, left_piece.position
            )

            if not am_i_in_check(piece.color, conditional_piece_positions2):
                valid_movements.append(left_piece.position)

        if right_piece is not None and right_piece.color != piece.color:
            conditional_piece_positions2 = change_a_piece_position_for_valid_movements(
                piece, right_piece.position
            )

            if not am_i_in_check(piece.color, conditional_piece_positions2):
                valid_movements.append(right_piece.position)

        ## en passant capture
        if (piece.position[1] == "5" and piece.color == "w") or (
            piece.position[1] == "4" and piece.color == "b"
        ):
            last_movement = movements_history[-1]
            if (
                last_movement["piece"].piece == "P"
                and abs(int(last_movement["from"][1]) - int(last_movement["to"][1]))
                == 2
            ):
                number = letter_to_number(piece.position[0])
                possible_en_passant = letter_to_number(last_movement["to"][0])

                if abs(number - possible_en_passant) == 1:
                    position = last_movement["to"][0] + str(
                        int(piece.position[1]) + (1 * direction)
                    )
                    conditional_piece_positions2 = (
                        change_a_piece_position_for_valid_movements(piece, position)
                    )

                    if not am_i_in_check(piece.color, conditional_piece_positions2):
                        valid_movements.append(position)

    # knight
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

            target_piece = get_piece_on_position(position, conditional_piece_positions)

            if (
                target_piece
                and target_piece.color == piece.color
                and not looking_enemy_movements
            ):
                continue

            if looking_enemy_movements:
                valid_movements.append(position)
                continue

            conditional_piece_positions2 = change_a_piece_position_for_valid_movements(
                piece, position
            )

            if not am_i_in_check(piece.color, conditional_piece_positions2):
                valid_movements.append(position)

    # rook or queen
    if piece.piece.upper() == "R" or piece.piece.upper() == "Q":
        x = letter_to_number(piece.position[0])
        y = int(piece.position[1])

        target_x = x - 1

        already_first_break = False

        while target_x >= 0:
            target_letter = number_to_letter(target_x)
            position = target_letter + str(y)

            target_piece = get_piece_on_position(position, conditional_piece_positions)

            if target_piece is not None:
                if target_piece.color != piece.color:
                    valid_movements.append(position)
                break

            conditional_piece_positions2 = change_a_piece_position_for_valid_movements(
                piece, position
            )

            if looking_enemy_movements or not am_i_in_check(
                piece.color, conditional_piece_positions2
            ):
                valid_movements.append(position)

            target_x -= 1

        target_x = x + 1

        while target_x <= 7:
            target_letter = number_to_letter(target_x)

            position = target_letter + str(y)

            target_piece = get_piece_on_position(position, conditional_piece_positions)

            if target_piece is not None:
                if target_piece.color != piece.color:
                    valid_movements.append(position)
                break

            conditional_piece_positions2 = change_a_piece_position_for_valid_movements(
                piece, position
            )

            if looking_enemy_movements or not am_i_in_check(
                piece.color, conditional_piece_positions2
            ):
                valid_movements.append(position)

            target_x += 1

        target_y = y - 1

        while target_y >= 1:
            target_letter = number_to_letter(x)
            position = target_letter + str(target_y)

            target_piece = get_piece_on_position(position, conditional_piece_positions)

            if target_piece is not None:
                if target_piece.color != piece.color:
                    valid_movements.append(position)
                break

            conditional_piece_positions2 = change_a_piece_position_for_valid_movements(
                piece, position
            )

            if looking_enemy_movements or not am_i_in_check(
                piece.color, conditional_piece_positions2
            ):
                valid_movements.append(position)

            target_y -= 1

        target_y = y + 1

        while target_y <= 8:
            target_letter = number_to_letter(x)

            position = target_letter + str(target_y)

            target_piece = get_piece_on_position(position, conditional_piece_positions)

            if target_piece is not None:
                if target_piece.color != piece.color:
                    valid_movements.append(position)
                break

            conditional_piece_positions2 = change_a_piece_position_for_valid_movements(
                piece, position
            )

            if looking_enemy_movements or not am_i_in_check(
                piece.color, conditional_piece_positions2
            ):
                valid_movements.append(position)

            target_y += 1

    # bishop or queen
    if piece.piece.upper() == "B" or piece.piece.upper() == "Q":
        x = letter_to_number(piece.position[0])
        y = int(piece.position[1])

        target_x = x - 1
        target_y = y - 1

        while target_x >= 0 and target_y >= 1:
            target_letter = number_to_letter(target_x)
            position = target_letter + str(target_y)

            target_piece = get_piece_on_position(position, conditional_piece_positions)

            if target_piece is not None:
                if target_piece.color != piece.color:
                    valid_movements.append(position)
                break

            conditional_piece_positions2 = change_a_piece_position_for_valid_movements(
                piece, position
            )

            if looking_enemy_movements or not am_i_in_check(
                piece.color, conditional_piece_positions2
            ):
                valid_movements.append(position)

            target_x -= 1
            target_y -= 1

        target_x = x + 1
        target_y = y - 1

        while target_x <= 7 and target_y >= 1:
            target_letter = number_to_letter(target_x)
            position = target_letter + str(target_y)

            target_piece = get_piece_on_position(position, conditional_piece_positions)

            if target_piece is not None:
                if target_piece.color != piece.color:
                    valid_movements.append(position)
                break

            conditional_piece_positions2 = change_a_piece_position_for_valid_movements(
                piece, position
            )

            if looking_enemy_movements or not am_i_in_check(
                piece.color, conditional_piece_positions2
            ):
                valid_movements.append(position)

            target_x += 1
            target_y -= 1

        target_x = x - 1
        target_y = y + 1

        while target_x >= 0 and target_y <= 8:
            target_letter = number_to_letter(target_x)
            position = target_letter + str(target_y)

            target_piece = get_piece_on_position(position, conditional_piece_positions)

            if target_piece is not None:
                if target_piece.color != piece.color:
                    valid_movements.append(position)
                break

            conditional_piece_positions2 = change_a_piece_position_for_valid_movements(
                piece, position
            )

            if looking_enemy_movements or not am_i_in_check(
                piece.color, conditional_piece_positions2
            ):
                valid_movements.append(position)

            target_x -= 1
            target_y += 1

        target_x = x + 1
        target_y = y + 1

        while target_x <= 7 and target_y <= 8:
            target_letter = number_to_letter(target_x)
            position = target_letter + str(target_y)

            target_piece = get_piece_on_position(position, conditional_piece_positions)

            if target_piece is not None:
                if target_piece.color != piece.color:
                    valid_movements.append(position)
                break

            conditional_piece_positions2 = change_a_piece_position_for_valid_movements(
                piece, position
            )

            if looking_enemy_movements or not am_i_in_check(
                piece.color, conditional_piece_positions2
            ):
                valid_movements.append(position)

            target_x += 1
            target_y += 1

    # king
    if piece.piece.upper() == "K":
        x = letter_to_number(piece.position[0])
        y = int(piece.position[1])

        targets = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]

        for target in targets:

            target_x = x + target[0]
            target_y = y + target[1]

            if target_x > 7 or target_x < 0:
                continue

            if target_y > 8 or target_y < 1:
                continue

            target_letter = number_to_letter(target_x)
            position = target_letter + str(target_y)

            target_piece = get_piece_on_position(position, conditional_piece_positions)

            if target_piece is None or target_piece.color != piece.color:

                conditional_piece_positions2 = (
                    change_a_piece_position_for_valid_movements(piece, position)
                )

                if looking_enemy_movements or not am_i_in_check(
                    piece.color, conditional_piece_positions2
                ):
                    valid_movements.append(position)

    return valid_movements


def change_a_piece_position_for_valid_movements(
    piece: PiecePosition, to_conditional_position: str
):

    conditional_piece_positions = []

    for piece_position in piece_positions:
        if (
            piece_position.piece == piece.piece
            and piece_position.color == piece.color
            and piece_position.position == piece.position
        ):
            conditional_piece_positions.append(
                PiecePosition(piece.color, piece.piece, to_conditional_position)
            )
        elif piece_position.position != to_conditional_position:
            conditional_piece_positions.append(piece_position)

    return conditional_piece_positions


selected_piece = (-1, -1)
valid_movements = []

turn = "w"
promote_dialog = False

while True:

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:

            if promote_dialog:
                x = event.pos[0] / 100
                y = event.pos[1] / 100

                if 4.5 > y > 3.5:
                    if 3 > x > 2:
                        for piece_position in piece_positions:
                            if piece_position.position == movements_history[-1]["to"]:
                                piece_position.piece = "Q"
                                promote_dialog = False
                    if 4 > x > 3:
                        for piece_position in piece_positions:
                            if piece_position.position == movements_history[-1]["to"]:
                                piece_position.piece = "R"
                                promote_dialog = False
                    if 5 > x > 4:
                        for piece_position in piece_positions:
                            if piece_position.position == movements_history[-1]["to"]:
                                piece_position.piece = "B"
                                promote_dialog = False
                    if 6 > x > 5:
                        for piece_position in piece_positions:
                            if piece_position.position == movements_history[-1]["to"]:
                                piece_position.piece = "N"
                                promote_dialog = False

            else:
                letter = number_to_letter(event.pos[0] // 100)
                number = 8 - (event.pos[1] // 100)
                piece = get_piece_on_position(letter + str(number))

                # selected a piece to move
                if piece and piece.color == turn:
                    selected_piece = (
                        event.pos[0] // 100,
                        event.pos[1] // 100,
                    )
                    valid_movements = get_valid_movements(piece)
                    continue

                # selected a place to move the piece
                if selected_piece[0] != -1:

                    if letter + str(number) not in valid_movements:
                        continue

                    piece_letter = number_to_letter(selected_piece[0])
                    piece_number = 8 - (selected_piece[1])
                    old_piece = get_piece_on_position(piece_letter + str(piece_number))
                    from_position = old_piece.position
                    old_piece.position = letter + str(number)

                    # default capture
                    if piece and piece.color != turn:
                        piece_positions.remove(piece)

                    # capture by en passant
                    if (
                        old_piece.piece == "P"
                        and from_position[0] != old_piece.position[0]
                        and piece is None
                    ):
                        piece_positions.remove(movements_history[-1]["piece"])

                    selected_piece = (-1, -1)
                    valid_movements = []
                    movements_history.append(
                        {
                            "piece": old_piece,
                            "from": from_position,
                            "to": old_piece.position,
                        }
                    )

                    if old_piece.piece == "P" and (
                        old_piece.position[1] == "1" or old_piece.position[1] == "8"
                    ):
                        promote_dialog = True

                    if turn == "w":
                        turn = "b"
                    else:
                        turn = "w"

                    print_tabletop()
                    if am_i_in_check(turn, piece_positions):
                        print("voce esta em check")

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

    if promote_dialog:
        pygame.draw.rect(
            gameDisplay,
            (255, 255, 255),
            (block_size * 2, block_size * 3, block_size * 4, block_size * 2),
            0,
        )
        pygame.draw.rect(
            gameDisplay,
            (0, 0, 0),
            (block_size * 2, block_size * 3, block_size * 4, block_size * 2),
            1,
        )

        promote_color = "b"

        if turn == "b":
            promote_color = "w"

        gameDisplay.blit(
            piece_image[promote_color + "-Q"],
            (
                (2 * block_size) + center_piece_img,
                (3.5 * block_size) + center_piece_img,
            ),
        )

        gameDisplay.blit(
            piece_image[promote_color + "-R"],
            (
                (3 * block_size) + center_piece_img,
                (3.5 * block_size) + center_piece_img,
            ),
        )

        gameDisplay.blit(
            piece_image[promote_color + "-B"],
            (
                (4 * block_size) + center_piece_img,
                (3.5 * block_size) + center_piece_img,
            ),
        )

        gameDisplay.blit(
            piece_image[promote_color + "-N"],
            (
                (5 * block_size) + center_piece_img,
                (3.5 * block_size) + center_piece_img,
            ),
        )

    pygame.display.update()