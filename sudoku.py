import pygame
import sys
from solver import Sudoku
import random

pygame.init()

cell_size = 50
minor_grid_size = 1
major_grid_size = 3
buffer = 5
button_height = 50
button_width = 125
button_border = 2
width = cell_size*9 + minor_grid_size*6 + major_grid_size*4 + buffer*2
height = cell_size*9 + minor_grid_size*6 + \
    major_grid_size*4 + button_height + buffer*3 + button_border*2
size = width, height
white = 255, 255, 255
black = 0, 0, 0
gray = 200, 200, 200
green = 0, 175, 0
red = 200, 0, 0
inactive_btn = 51, 255, 255
active_btn = 51, 153, 255

# screen = pygame.display.set_mode(size)
# menuscreen = pygame.display.set_mode(size)
pygame.display.set_caption('Kelompok 13 - SUDOKU SOLVER')


class RectCell(pygame.Rect):
    def __init__(self, left, top, row, col):
        super().__init__(left, top, cell_size, cell_size)
        self.row = row
        self.col = col


def create_cells():
    cells = [[] for _ in range(9)]

    row = 0
    col = 0
    left = buffer + major_grid_size
    top = buffer + major_grid_size

    while row < 9:
        while col < 9:
            cells[row].append(RectCell(left, top, row, col))

            left += cell_size + minor_grid_size
            if col != 0 and (col + 1) % 3 == 0:
                left = left + major_grid_size - minor_grid_size
            col += 1

        top += cell_size + minor_grid_size
        if row != 0 and (row + 1) % 3 == 0:
            top = top + major_grid_size - minor_grid_size
        left = buffer + major_grid_size
        col = 0
        row += 1

    return cells


# lvl 1
def draw_grid(screen):
    lines_drawn = 0
    pos = buffer + major_grid_size + cell_size

    while lines_drawn < 6:
        pygame.draw.line(screen, black, (pos, buffer),
                         (pos, width-buffer-1), minor_grid_size)
        pygame.draw.line(screen, black, (buffer, pos),
                         (width-buffer-1, pos), minor_grid_size)
        # print("pos= ", pos, "buffer= ", buffer, "width= ", width, "cell_size= ", cell_size,
        #       "minor_grid_size= ", minor_grid_size, "major_grid_size= ", major_grid_size, "\n")

        lines_drawn += 1

        pos += cell_size + minor_grid_size
        if lines_drawn % 2 == 0:
            pos += cell_size + major_grid_size

    pygame.draw.line(screen, black, (6, 5),
                     (6, 472), 3)
    pygame.draw.line(screen, black, (5, 6),
                     (472, 6), 3)
    pygame.draw.line(screen, black, (471, 5),
                     (471, 472), 3)
    pygame.draw.line(screen, black, (5, 471),
                     (472, 471), 3)

    # kel1
    pygame.draw.line(screen, black, (58, 5),
                     (58, 472), 3)

    # kel2
    pygame.draw.line(screen, black, (109, 419),
                     (472, 419), 3)
    pygame.draw.line(screen, black, (58, 368),
                     (109, 368), 3)
    pygame.draw.line(screen, black, (109, 368),
                     (109, 419), 3)

    # kel3
    pygame.draw.line(screen, black, (58, 264),
                     (161, 264), 3)
    pygame.draw.line(screen, black, (161, 316),
                     (264, 316), 3)
    pygame.draw.line(screen, black, (161, 264),
                     (161, 316), 3)
    pygame.draw.line(screen, black, (264, 316),
                     (264, 419), 3)

    # kel4
    pygame.draw.line(screen, black, (264, 316),
                     (368, 316), 3)
    pygame.draw.line(screen, black, (368, 264),
                     (419, 264), 3)
    pygame.draw.line(screen, black, (419, 316),
                     (471, 316), 3)
    pygame.draw.line(screen, black, (368, 264),
                     (368, 316), 3)
    pygame.draw.line(screen, black, (419, 264),
                     (419, 316), 3)

    # kel5
    pygame.draw.line(screen, black, (264, 264),
                     (316, 264), 3)
    pygame.draw.line(screen, black, (316, 161),
                     (471, 161), 3)
    pygame.draw.line(screen, black, (316, 161),
                     (316, 264), 3)
    pygame.draw.line(screen, black, (264, 264),
                     (264, 316), 3)

    # kel6
    pygame.draw.line(screen, black, (213, 58),
                     (368, 58), 3)

    pygame.draw.line(screen, black, (213, 6),
                     (213, 58), 3)
    pygame.draw.line(screen, black, (368, 58),
                     (368, 161), 3)

    # kel7
    # draw line 58, 109 to 109, 109
    pygame.draw.line(screen, black, (58, 109),
                     (109, 109), 3)
    # draw line 109,109 to 109,161
    pygame.draw.line(screen, black, (109, 109),
                     (109, 161), 3)
    # draw line 109,161 to 161,161
    pygame.draw.line(screen, black, (109, 161),
                     (161, 161), 3)
    # draw line 161,161 to 161,213
    pygame.draw.line(screen, black, (161, 161),
                     (161, 213), 3)
    # draw line 161,213 to 316,213
    pygame.draw.line(screen, black, (161, 213),
                     (264, 213), 3)
    # draw line 316,213 to 316,316
    pygame.draw.line(screen, black, (264, 213),
                     (264, 316), 3)

    # kel 8
    # draw line 161,161 to 213,161
    pygame.draw.line(screen, black, (161, 161),
                     (213, 161), 3)
    # draw line 213,161 to 213,109
    pygame.draw.line(screen, black, (213, 161),
                     (213, 109), 3)
    # draw line 213,109 to 264,109
    pygame.draw.line(screen, black, (213, 109),
                     (264, 109), 3)
    # draw line 264,109 to 264,58
    pygame.draw.line(screen, black, (264, 109),
                     (264, 58), 3)
    # draw line 264,58 to 368,58`

    for pos in range(buffer+major_grid_size//2, width, cell_size*3 + minor_grid_size*2 + major_grid_size):
        # print("pos= ",pos, "buffer= ", buffer, "width= ", width, "cell_size= ", cell_size, "minor_grid_size= ", minor_grid_size, "major_grid_size= ", major_grid_size,"\n")
        if pos == 6:
            continue
        if pos == 471:
            continue
        pygame.draw.line(screen, black, (pos, buffer),
                         (pos, width-buffer-1), minor_grid_size)
        pygame.draw.line(screen, black, (buffer, pos),
                         (width-buffer-1, pos), minor_grid_size)

# lvl 2


def draw_grid_lvl2(screen):
    lines_drawn = 0
    pos = buffer + major_grid_size + cell_size
    # draw grid with jigsaw pattern

    # pygame.draw.line(screen, black, (pos, buffer),
    #                  (pos, width-buffer-1), minor_grid_size)
    # pygame.draw.line(screen, black, (buffer, pos), (width-buffer-1, pos), minor_grid_size)
    while lines_drawn < 6:
        pygame.draw.line(screen, black, (pos, buffer),
                         (pos, width-buffer-1), minor_grid_size)
        pygame.draw.line(screen, black, (buffer, pos),
                         (width-buffer-1, pos), minor_grid_size)

        lines_drawn += 1

        pos += cell_size + minor_grid_size
        if lines_drawn % 2 == 0:
            pos += cell_size + major_grid_size

    for pos in range(buffer+major_grid_size//2, width, cell_size*3 + minor_grid_size*2 + major_grid_size):
        pygame.draw.line(screen, black, (pos, buffer),
                         (pos, width-buffer-1), major_grid_size)
        pygame.draw.line(screen, black, (buffer, pos),
                         (width-buffer-1, pos), major_grid_size)

# lvl 3


def draw_grid_lvl3(screen):
    lines_drawn = 0
    pos = buffer + major_grid_size + cell_size
    # draw grid with jigsaw pattern

    # pygame.draw.line(screen, black, (pos, buffer),
    #                  (pos, width-buffer-1), minor_grid_size)
    # pygame.draw.line(screen, black, (buffer, pos), (width-buffer-1, pos), minor_grid_size)
    while lines_drawn < 6:
        pygame.draw.line(screen, black, (pos, buffer),
                         (pos, width-buffer-1), minor_grid_size)
        pygame.draw.line(screen, black, (buffer, pos),
                         (width-buffer-1, pos), minor_grid_size)

        lines_drawn += 1

        pos += cell_size + minor_grid_size
        if lines_drawn % 2 == 0:
            pos += cell_size + major_grid_size

    for pos in range(buffer+major_grid_size//2, width, cell_size*3 + minor_grid_size*2 + major_grid_size):

        pygame.draw.line(screen, black, (pos, buffer),
                         (pos, width-buffer-1), major_grid_size)
        pygame.draw.line(screen, black, (buffer, pos),
                         (width-buffer-1, pos), major_grid_size)


def fill_cells(cells, board, screen):
    font = pygame.font.Font(None, 36)

    for row in range(9):
        for col in range(9):
            if board.board[row][col].value is None:
                continue

            if not board.board[row][col].editable:
                font.bold = True
                text = font.render(f'{board.board[row][col].value}', 1, black)

            else:
                font.bold = False
                if board.check_move(board.board[row][col], board.board[row][col].value):
                    text = font.render(
                        f'{board.board[row][col].value}', 1, green)
                else:
                    text = font.render(
                        f'{board.board[row][col].value}', 1, red)

            xpos, ypos = cells[row][col].center
            textbox = text.get_rect(center=(xpos, ypos))
            screen.blit(text, textbox)


def draw_button(left, top, width, height, border, color, border_color, text, screen):
    pygame.draw.rect(screen, border_color, (left, top,
                     width+border*2, height+border*2))

    button = pygame.Rect(
        left+border,
        top+border,
        width,
        height
    )
    pygame.draw.rect(screen, color, button)

    font = pygame.font.Font(None, 26)
    text = font.render(text, 1, black)
    xpos, ypos = button.center
    textbox = text.get_rect(center=(xpos, ypos))
    screen.blit(text, textbox)

    return button


def draw_board(active_cell, cells, game, screen):
    draw_grid(screen)
    if active_cell is not None:
        pygame.draw.rect(screen, gray, active_cell)

    fill_cells(cells, game, screen)


def check_sudoku(sudoku):
    if sudoku.get_empty_cell():
        raise ValueError('Game is not complete')

    row_sets = [set() for _ in range(9)]
    col_sets = [set() for _ in range(9)]
    box_sets = [set() for _ in range(9)]

    for row in range(9):
        for col in range(9):
            box = (row // 3) * 3 + col // 3
            value = sudoku.board[row][col].value

            if value in row_sets[row] or value in col_sets[col] or value in box_sets[box]:
                return False

            row_sets[row].add(value)
            col_sets[col].add(value)
            box_sets[box].add(value)

    return True


def play(lvl):
    if lvl == 1:
        data = [
            [0, 0, 0, 9, 0, 0, 0, 3, 0],
            [3, 0, 6, 0, 2, 0, 0, 4, 0],
            [2, 0, 4, 0, 0, 3, 1, 0, 6],
            [0, 7, 0, 0, 5, 1, 0, 8, 0],
            [0, 3, 1, 0, 6, 0, 0, 5, 7],
            [5, 0, 9, 0, 0, 0, 6, 0, 0],
            [4, 1, 0, 0, 0, 2, 0, 7, 8],
            [7, 6, 3, 0, 0, 5, 4, 0, 0],
            [9, 2, 8, 0, 0, 4, 0, 0, 1]
        ]
    elif lvl == 2:
        data = [
            [0, 2, 0, 0, 0, 6, 8, 0, 0],
            [4, 8, 0, 0, 0, 7, 6, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 4, 0],
            [8, 0, 7, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 8, 6, 4, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 3, 0, 8],
            [0, 1, 0, 0, 4, 0, 0, 0, 0],
            [0, 0, 2, 5, 0, 0, 0, 7, 9],
            [0, 0, 8, 9, 0, 0, 0, 3, 0]
        ]
    elif lvl == 3:
        # TBA
        data = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
    else:
        raise Exception("Level Error: Out Of Bound")

    game = Sudoku(data)
    cells = create_cells()
    active_cell = None
    solve_rect = pygame.Rect(
        buffer,
        height-button_height - button_border*2 - buffer,
        button_width + button_border*2,
        button_height + button_border*2
    )
    screen = pygame.display.set_mode(size)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()

                if reset_btn.collidepoint(mouse_pos):
                    game.reset()

                # if solve_btn.collidepoint(mouse_pos):
                #     screen.fill(white)
                #     active_cell = None
                #     draw_board(active_cell, cells, game, screen)
                #     reset_btn = draw_button(
                #         width - buffer - button_border*2 - button_width,
                #         height - button_height - button_border*2 - buffer,
                #         button_width,
                #         button_height,
                #         button_border,
                #         inactive_btn,
                #         black,
                #         'Reset',
                #         screen
                #     )
                #     solve_btn = draw_button(
                #         width - buffer*2 - button_border*4 - button_width*2,
                #         height - button_height - button_border*2 - buffer,
                #         button_width,
                #         button_height,
                #         button_border,
                #         inactive_btn,
                #         black,
                #         'Visual Solve',
                #         screen
                #     )
                #     pygame.display.flip()

                if back_btn.collidepoint(mouse_pos):
                    screen.fill(white)
                    pygame.display.set_mode((300, height))
                    return

                active_cell = None
                for row in cells:
                    for cell in row:
                        if cell.collidepoint(mouse_pos):
                            active_cell = cell

                if active_cell and not game.board[active_cell.row][active_cell.col].editable:
                    active_cell = None

            if event.type == pygame.KEYUP:
                if active_cell is not None:
                    if event.key == pygame.K_0 or event.key == pygame.K_KP0:
                        game.board[active_cell.row][active_cell.col].value = 0
                    if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                        game.board[active_cell.row][active_cell.col].value = 1
                    if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                        game.board[active_cell.row][active_cell.col].value = 2
                    if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                        game.board[active_cell.row][active_cell.col].value = 3
                    if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                        game.board[active_cell.row][active_cell.col].value = 4
                    if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                        game.board[active_cell.row][active_cell.col].value = 5
                    if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                        game.board[active_cell.row][active_cell.col].value = 6
                    if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                        game.board[active_cell.row][active_cell.col].value = 7
                    if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                        game.board[active_cell.row][active_cell.col].value = 8
                    if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                        game.board[active_cell.row][active_cell.col].value = 9
                    if event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                        game.board[active_cell.row][active_cell.col].value = None

        screen.fill(white)

        draw_board(active_cell, cells, game, screen)

        reset_btn = draw_button(
            width - buffer - button_border*2 - button_width,
            height - button_height - button_border*2 - buffer,
            button_width,
            button_height,
            button_border,
            inactive_btn,
            black,
            'Reset',
            screen
        )
        solve_btn = draw_button(
            width - buffer*2 - button_border*4 - button_width*2,
            height - button_height - button_border*2 - buffer,
            button_width,
            button_height,
            button_border,
            inactive_btn,
            black,
            'Visual Solve',
            screen
        )

        if reset_btn.collidepoint(pygame.mouse.get_pos()):
            reset_btn = draw_button(
                width - buffer - button_border*2 - button_width,
                height - button_height - button_border*2 - buffer,
                button_width,
                button_height,
                button_border,
                active_btn,
                black,
                'Reset',
                screen
            )
        if solve_btn.collidepoint(pygame.mouse.get_pos()):
            solve_btn = draw_button(
                width - buffer*2 - button_border*4 - button_width*2,
                height - button_height - button_border*2 - buffer,
                button_width,
                button_height,
                button_border,
                active_btn,
                black,
                'Visual Solve',
                screen
            )

        back_btn = draw_button(
            width - buffer*3 - button_border*6 - button_width*3,
            height - button_height - button_border*2 - buffer,
            button_width,
            button_height,
            button_border,
            inactive_btn,
            black,
            'Back',
            screen
        )
        if back_btn.collidepoint(pygame.mouse.get_pos()):
            back_btn = draw_button(
                width - buffer*3 - button_border*6 - button_width*3,
                height - button_height - button_border*2 - buffer,
                button_width,
                button_height,
                button_border,
                active_btn,
                black,
                'Back',
                screen
            )

        if not game.get_empty_cell():
            if check_sudoku(game):
                font = pygame.font.Font(None, 36)
                text = font.render('Solved!', 1, green)
                textbox = text.get_rect(center=(solve_rect.center))
                screen.blit(text, textbox)

        pygame.display.flip()


def level():
    screen = pygame.display.set_mode((300, height))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()

                if lvl1_btn.collidepoint(mouse_pos):
                    screen.fill(white)
                    pygame.display.flip()
                    play(1)
                if lvl2_btn.collidepoint(mouse_pos):
                    screen.fill(white)
                    pygame.display.flip()
                    play(2)
                if lvl3_btn.collidepoint(mouse_pos):
                    screen.fill(white)
                    pygame.display.flip()
                    play(3)
                if back_btn.collidepoint(mouse_pos):
                    screen.fill(white)
                    pygame.display.flip()
                    return

        screen.fill(white)

        lvl1_btn = draw_button(
            300/2 - (button_width+button_border)/2,
            height - (button_height+button_border)*9,
            button_width,
            button_height,
            button_border,
            inactive_btn,
            black,
            'Level 1',
            screen
        )
        if lvl1_btn.collidepoint(pygame.mouse.get_pos()):
            lvl1_btn = draw_button(
                300/2 - (button_width+button_border)/2,
                height - (button_height+button_border)*9,
                button_width,
                button_height,
                button_border,
                active_btn,
                black,
                'Level 1',
                screen
            )

        lvl2_btn = draw_button(
            300/2 - (button_width+button_border)/2,
            height - (button_height+button_border)*7,
            button_width,
            button_height,
            button_border,
            inactive_btn,
            black,
            'Level 2',
            screen
        )
        if lvl2_btn.collidepoint(pygame.mouse.get_pos()):
            lvl2_btn = draw_button(
                300/2 - (button_width+button_border)/2,
                height - (button_height+button_border)*7,
                button_width,
                button_height,
                button_border,
                active_btn,
                black,
                'Level 2',
                screen
            )

        lvl3_btn = draw_button(
            300/2 - (button_width+button_border)/2,
            height - (button_height+button_border)*5,
            button_width,
            button_height,
            button_border,
            inactive_btn,
            black,
            'Level 3',
            screen
        )
        if lvl3_btn.collidepoint(pygame.mouse.get_pos()):
            lvl3_btn = draw_button(
                300/2 - (button_width+button_border)/2,
                height - (button_height+button_border)*5,
                button_width,
                button_height,
                button_border,
                active_btn,
                black,
                'Level 3',
                screen
            )

        back_btn = draw_button(
            300/2 - (button_width+button_border)/2,
            height - (button_height+button_border)*3,
            button_width,
            button_height,
            button_border,
            inactive_btn,
            black,
            'Back',
            screen
        )
        if back_btn.collidepoint(pygame.mouse.get_pos()):
            back_btn = draw_button(
                300/2 - (button_width+button_border)/2,
                height - (button_height+button_border)*3,
                button_width,
                button_height,
                button_border,
                active_btn,
                black,
                'Back',
                screen
            )

        pygame.display.flip()


def menu():
    screen = pygame.display.set_mode((300, height))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()

                if play_btn.collidepoint(mouse_pos):
                    screen.fill(white)
                    pygame.display.flip()
                    level()

        screen.fill(white)

        play_btn = draw_button(
            300/2 - (button_width+button_border)/2,
            height/2 - (button_height+button_border)/2,
            button_width,
            button_height,
            button_border,
            inactive_btn,
            black,
            'Play',
            screen
        )
        if play_btn.collidepoint(pygame.mouse.get_pos()):
            play_btn = draw_button(
                300/2 - (button_width+button_border)/2,
                height/2 - (button_height+button_border)/2,
                button_width,
                button_height,
                button_border,
                active_btn,
                black,
                'Play',
                screen
            )

        pygame.display.flip()


if __name__ == '__main__':
    # play()
    menu()
