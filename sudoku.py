# pylint: skip-file
import pygame
import random
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
width = cell_size * 9 + minor_grid_size * 6 + major_grid_size * 4 + buffer * 2
height = cell_size * 9 + minor_grid_size * 6 + \
         major_grid_size * 4 + button_height + buffer * 3 + button_border * 2
size = width, height
white = 255, 255, 255
black = 0, 0, 0
gray = 200, 200, 200
green = 0, 175, 0
red = 200, 0, 0
inactive_btn = 51, 255, 255
active_btn = 51, 153, 255
region_dict = []

pygame.display.set_mode((300, height))
pygame.display.set_caption('Kelompok 13 - SUDOKU SOLVER')
screen = "menu"
run = True
lvl = None


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
def draw_grid(area):
    # draw BG
    pygame.draw.line(pygame.display.get_surface(), black, (6, 5),
                     (6, 472), 3)
    pygame.draw.line(pygame.display.get_surface(), black, (5, 6),
                     (472, 6), 3)
    pygame.draw.line(pygame.display.get_surface(), black, (471, 5),
                     (471, 472), 3)
    pygame.draw.line(pygame.display.get_surface(), black, (5, 471),
                     (472, 471), 3)
    jarak = [6, 58, 109, 161, 213, 264, 316, 368, 419, 471]
    # loop 9 times
    # sumbu Y
    for p in range(len(area)):
        for i in range(9):
            for j in range(8):
                if area[p][i][j] == area[p][i][j + 1]:
                    pygame.draw.line(pygame.display.get_surface(), black, (jarak[j + 1], jarak[i]),
                                    (jarak[j + 1], jarak[i + 1]), minor_grid_size)
                else:
                    pygame.draw.line(pygame.display.get_surface(), black, (jarak[j + 1], jarak[i]),
                                    (jarak[j + 1], jarak[i + 1]), major_grid_size)
    # sumbu X
    for p in range(len(area)):
        for i in range(8):
            for j in range(9):
                if area[p][i][j] == area[p][i + 1][j]:
                    pygame.draw.line(pygame.display.get_surface(), black, (jarak[j], jarak[i + 1]),
                                    (jarak[j + 1], jarak[i + 1]), minor_grid_size)
                else:
                    pygame.draw.line(pygame.display.get_surface(), black, (jarak[j], jarak[i + 1]),
                                    (jarak[j + 1], jarak[i + 1]), major_grid_size)


# lvl 2
def draw_grid_lvl2(area):
    # draw BG
    pygame.draw.line(pygame.display.get_surface(), black, (6, 5),
                     (6, 472), 3)
    pygame.draw.line(pygame.display.get_surface(), black, (5, 6),
                     (472, 6), 3)
    pygame.draw.line(pygame.display.get_surface(), black, (471, 5),
                     (471, 472), 3)
    pygame.draw.line(pygame.display.get_surface(), black, (5, 471),
                     (472, 471), 3)
    jarak = [6, 58, 109, 161, 213, 264, 316, 368, 419, 471]
    # loop 9 times
    # sumbu Y
    for p in range(len(area)):
        for i in range(9):
            for j in range(8):
                if area[p][i][j] == area[p][i][j + 1]:
                    pygame.draw.line(pygame.display.get_surface(), black, (jarak[j + 1], jarak[i]),
                                    (jarak[j + 1], jarak[i + 1]), minor_grid_size)
                else:
                    pygame.draw.line(pygame.display.get_surface(), black, (jarak[j + 1], jarak[i]),
                                    (jarak[j + 1], jarak[i + 1]), major_grid_size)
    # sumbu X
    for p in range(len(area)):
        for i in range(8):
            for j in range(9):
                if area[p][i][j] == area[p][i + 1][j]:
                    pygame.draw.line(pygame.display.get_surface(), black, (jarak[j], jarak[i + 1]),
                                    (jarak[j + 1], jarak[i + 1]), minor_grid_size)
                else:
                    pygame.draw.line(pygame.display.get_surface(), black, (jarak[j], jarak[i + 1]),
                                    (jarak[j + 1], jarak[i + 1]), major_grid_size)


# lvl 3
def draw_grid_lvl3():
    lines_drawn = 0
    pos = buffer + major_grid_size + cell_size
    # draw grid with jigsaw pattern

    # pygame.draw.line(pygame.display.get_surface(), black, (pos, buffer),
    #                  (pos, width-buffer-1), minor_grid_size)
    # pygame.draw.line(pygame.display.get_surface(), black, (buffer, pos), (width-buffer-1, pos), minor_grid_size)
    while lines_drawn < 6:
        pygame.draw.line(pygame.display.get_surface(), black, (pos, buffer),
                         (pos, width - buffer - 1), minor_grid_size)
        pygame.draw.line(pygame.display.get_surface(), black, (buffer, pos),
                         (width - buffer - 1, pos), minor_grid_size)

        lines_drawn += 1

        pos += cell_size + minor_grid_size
        if lines_drawn % 2 == 0:
            pos += cell_size + major_grid_size

    for pos in range(buffer + major_grid_size // 2, width, cell_size * 3 + minor_grid_size * 2 + major_grid_size):
        pygame.draw.line(pygame.display.get_surface(), black, (pos, buffer),
                         (pos, width - buffer - 1), major_grid_size)
        pygame.draw.line(pygame.display.get_surface(), black, (buffer, pos),
                         (width - buffer - 1, pos), major_grid_size)


def fill_cells(cells, board):
    font = pygame.font.Font(None, 36)

    for p in range(len(board.board)):
        for row in range(9):
            for col in range(9):
                if board.board[p][row][col].value is None:
                    continue

                if not board.board[p][row][col].editable:
                    font.bold = True
                    text = font.render(f'{board.board[p][row][col].value}', 1, black)

                else:
                    font.bold = False
                    if board.check_move(board.board[p][row][col], board.board[p][row][col].value):
                        text = font.render(
                            f'{board.board[p][row][col].value}', 1, green)
                    else:
                        text = font.render(
                            f'{board.board[p][row][col].value}', 1, red)

                xpos, ypos = cells[row][col].center
                textbox = text.get_rect(center=(xpos, ypos))
                pygame.Surface.blit(pygame.display.get_surface(), text, textbox)


def draw_button(left, top, width, height, border, color, border_color, text):
    pygame.draw.rect(pygame.display.get_surface(), border_color, 
                     (left, top, width + border * 2, height + border * 2))

    button = pygame.Rect(
        left + border,
        top + border,
        width,
        height
    )
    pygame.draw.rect(pygame.display.get_surface(), color, button)

    font = pygame.font.Font(None, 26)
    text = font.render(text, 1, black)
    xpos, ypos = button.center
    textbox = text.get_rect(center=(xpos, ypos))
    pygame.Surface.blit(pygame.display.get_surface(), text, textbox)

    return button


def draw_board(active_cell, cells, game, area):
    global lvl
    if (lvl == 1):
        draw_grid(area)
    elif (lvl == 2):
        draw_grid_lvl2(area)
    elif (lvl == 3):
        draw_grid_lvl3()
    if active_cell is not None:
        pygame.draw.rect(pygame.display.get_surface(), gray, active_cell)

    fill_cells(cells, game)


def dictConv(matrix):
    global region_dict
    for i in range(len(matrix)):
        dict = {}
        for j in range(len(matrix[i])):
            for k in range(len(matrix[i][j])):
                region = f'region_{matrix[i][j][k]}'
                coordinate = (j, k)

                if region in dict:
                    dict[region].append(coordinate)
                else:
                    dict[region] = [coordinate]
        region_dict.append(dict)


def printdict(dict):
    for region, coordinates in dict.items():
        print(region, ":", coordinates)


def find_region(dict,i, j):
    for v, d in dict.items():
        if (i, j) in d:
            return v


def check_sudoku(sudoku):
    if sudoku.get_empty_cell():
        raise ValueError('Game is not complete')

    r = []
    c = []
    b = []
    
    for p in range(len(region_dict)):
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        box_sets = dict.fromkeys(region_dict[p].keys())
        for row in range(9):
            for col in range(9):
                region_key = find_region(region_dict[p], row, col)
                regional_points = region_dict[p][region_key]
                value = sudoku.board[p][row][col].value
                cntRow = 0
                cntCol = 0
                if p > 0 and regional_points == 1 and value in r[p-1][row+6]:
                    cntRow+=1
                if p > 0 and regional_points == 1 and value in r[p-1][col+6]:
                    cntCol+=1
                if value in row_sets[row] or value in col_sets[col] or cntRow > 1 or cntCol > 1:
                    return False
                box_sets[region_key] = set() if box_sets[region_key] is None else box_sets[region_key]
                if value in box_sets[region_key]:
                    return False
                row_sets[row].add(value)
                col_sets[col].add(value)
                box_sets[region_key].add(value)
        r.append(row_sets)
        c.append(col_sets)
        b.append(box_sets)
    return True



def play():
    global screen, run, lvl

    num = random.randint(0, 2)
    if lvl == 1:
        if num == 0:
            data = [
                [
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
            ]
            area = [
                [
                [1, 1, 1, 2, 2, 2, 3, 3, 3],
                [1, 1, 1, 2, 2, 2, 3, 3, 3],
                [1, 1, 1, 2, 2, 2, 3, 3, 3],
                [4, 4, 4, 5, 5, 5, 6, 6, 6],
                [4, 4, 4, 5, 5, 5, 6, 6, 6],
                [4, 4, 4, 5, 5, 5, 6, 6, 6],
                [7, 7, 7, 8, 8, 8, 9, 9, 9],
                [7, 7, 7, 8, 8, 8, 9, 9, 9],
                [7, 7, 7, 8, 8, 8, 9, 9, 9]
                ]
            ]
        elif num == 1:
            data = [
                [
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
            ]
            area = [
                [
                [1, 1, 1, 2, 2, 2, 3, 3, 3],
                [1, 1, 1, 2, 2, 2, 3, 3, 3],
                [1, 1, 1, 2, 2, 2, 3, 3, 3],
                [4, 4, 4, 5, 5, 5, 6, 6, 6],
                [4, 4, 4, 5, 5, 5, 6, 6, 6],
                [4, 4, 4, 5, 5, 5, 6, 6, 6],
                [7, 7, 7, 8, 8, 8, 9, 9, 9],
                [7, 7, 7, 8, 8, 8, 9, 9, 9],
                [7, 7, 7, 8, 8, 8, 9, 9, 9]
                ]
            ]
        else:
            data = [
                [
                [1, 1, 1, 2, 2, 2, 3, 3, 3],
                [1, 1, 1, 2, 2, 2, 3, 3, 3],
                [1, 1, 1, 2, 2, 2, 3, 3, 3],
                [4, 4, 4, 5, 5, 5, 6, 6, 6],
                [4, 4, 4, 5, 5, 5, 6, 6, 6],
                [4, 4, 4, 5, 5, 5, 6, 6, 6],
                [7, 7, 7, 8, 8, 8, 9, 9, 9],
                [7, 7, 7, 8, 8, 8, 9, 9, 9],
                [7, 7, 7, 8, 8, 8, 9, 9, 9]
                ]
            ]
            area = [
                [
                [1, 1, 1, 2, 2, 2, 3, 3, 3],
                [1, 1, 1, 2, 2, 2, 3, 3, 3],
                [1, 1, 1, 2, 2, 2, 3, 3, 3],
                [4, 4, 4, 5, 5, 5, 6, 6, 6],
                [4, 4, 4, 5, 5, 5, 6, 6, 6],
                [4, 4, 4, 5, 5, 5, 6, 6, 6],
                [7, 7, 7, 8, 8, 8, 9, 9, 9],
                [7, 7, 7, 8, 8, 8, 9, 9, 9],
                [7, 7, 7, 8, 8, 8, 9, 9, 9]
                ]
            ]
    elif lvl == 2:
        if num == 0:
            data = [
                [
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
            ]
            area = [
                [
                [1, 2, 2, 2, 3, 3, 3, 3, 3],
                [1, 2, 2, 2, 2, 4, 4, 3, 3],
                [1, 5, 2, 2, 4, 4, 4, 3, 3],
                [1, 5, 5, 4, 4, 4, 6, 6, 6],
                [1, 5, 5, 5, 5, 4, 6, 6, 6],
                [1, 7, 7, 5, 5, 6, 6, 8, 6],
                [1, 7, 7, 7, 7, 8, 8, 8, 8],
                [1, 9, 7, 7, 7, 8, 8, 8, 8],
                [1, 9, 9, 9, 9, 9, 9, 9, 9]
                ]
            ]
        elif num == 1:
            data = [
                [
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
            ]
            area = [
                [
                [1, 2, 2, 2, 3, 3, 3, 3, 3],
                [1, 2, 2, 2, 2, 4, 4, 3, 3],
                [1, 5, 2, 2, 4, 4, 4, 3, 3],
                [1, 5, 5, 4, 4, 4, 6, 6, 6],
                [1, 5, 5, 5, 5, 4, 6, 6, 6],
                [1, 7, 7, 5, 5, 6, 6, 8, 6],
                [1, 7, 7, 7, 7, 8, 8, 8, 8],
                [1, 9, 7, 7, 7, 8, 8, 8, 8],
                [1, 9, 9, 9, 9, 9, 9, 9, 9]
                ]
            ]
        else:
            data = [
                [
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
            ]
            area = [
                [
                [1, 2, 2, 2, 3, 3, 3, 3, 3],
                [1, 2, 2, 2, 2, 4, 4, 3, 3],
                [1, 5, 2, 2, 4, 4, 4, 3, 3],
                [1, 5, 5, 4, 4, 4, 6, 6, 6],
                [1, 5, 5, 5, 5, 4, 6, 6, 6],
                [1, 7, 7, 5, 5, 6, 6, 8, 6],
                [1, 7, 7, 7, 7, 8, 8, 8, 8],
                [1, 9, 7, 7, 7, 8, 8, 8, 8],
                [1, 9, 9, 9, 9, 9, 9, 9, 9]
                ]
            ]

    elif lvl == 3:
        data = [
            [
                [6, 0, 3, 7, 0, 5, 9, 0, 8],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [4, 0, 5, 8, 0, 6, 7, 0, 2],
                [7, 0, 2, 1, 0, 8, 4, 0, 6],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 4, 3, 0, 7, 2, 0, 9],
                [2, 0, 7, 6, 0, 1, 8, 0, 3],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [3, 0, 8, 5, 0, 9, 6, 0, 1]
            ],
            [
                [8, 0, 3, 5, 0, 4, 2, 0, 7],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [6, 0, 1, 9, 0, 7, 3, 0, 5],
                [1, 0, 6, 8, 0, 5, 7, 0, 3],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [7, 0, 9, 3, 0, 1, 5, 0, 6],
                [3, 0, 2, 1, 0, 8, 6, 0, 4],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [9, 0, 7, 4, 0, 2, 8, 0, 1]
            ]
        ]
    else:
        raise Exception("Level Error: Out Of Bound")

    dictConv(area)
    game = Sudoku(data, region_dict)

    # printdict(region_dict[0])

    cells = create_cells()
    active_cell = None
    solve_rect = pygame.Rect(
        buffer,
        height - button_height - button_border * 2 - buffer,
        button_width + button_border * 2,
        button_height + button_border * 2
    )
    pygame.display.set_mode(size)

    while True:

        # Controller
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()

                if reset_btn.collidepoint(mouse_pos):
                    game.reset()

                # if solve_btn.collidepoint(mouse_pos):
                #     pygame.Surface.fill(pygame.display.get_surface(), white)
                #     active_cell = None
                #     draw_board(active_cell, cells, game)
                #     reset_btn = draw_button(
                #         width - buffer - button_border*2 - button_width,
                #         height - button_height - button_border*2 - buffer,
                #         button_width,
                #         button_height,
                #         button_border,
                #         inactive_btn,
                #         black,
                #         'Reset'
                #     )
                #     solve_btn = draw_button(
                #         width - buffer*2 - button_border*4 - button_width*2,
                #         height - button_height - button_border*2 - buffer,
                #         button_width,
                #         button_height,
                #         button_border,
                #         inactive_btn,
                #         black,
                #         'Visual Solve'
                #     )
                #     pygame.display.flip()

                if back_btn.collidepoint(mouse_pos):
                    screen = "level"
                    return

                active_cell = None
                for row in cells:
                    for cell in row:
                        if cell.collidepoint(mouse_pos):
                            active_cell = cell
                # ini harus diganti untuk multisudoku
                if active_cell and not game.board[0][active_cell.row][active_cell.col].editable:
                    active_cell = None

            if event.type == pygame.KEYUP:
                if active_cell is not None:
                    # harus diganti ketika multisudoku
                    if event.key == pygame.K_0 or event.key == pygame.K_KP0:
                        game.board[0][active_cell.row][active_cell.col].value = 0
                    if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                        game.board[0][active_cell.row][active_cell.col].value = 1
                    if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                        game.board[0][active_cell.row][active_cell.col].value = 2
                    if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                        game.board[0][active_cell.row][active_cell.col].value = 3
                    if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                        game.board[0][active_cell.row][active_cell.col].value = 4
                    if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                        game.board[0][active_cell.row][active_cell.col].value = 5
                    if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                        game.board[0][active_cell.row][active_cell.col].value = 6
                    if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                        game.board[0][active_cell.row][active_cell.col].value = 7
                    if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                        game.board[0][active_cell.row][active_cell.col].value = 8
                    if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                        game.board[0][active_cell.row][active_cell.col].value = 9
                    if event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                        game.board[0][active_cell.row][active_cell.col].value = None

        # GUI
        pygame.Surface.fill(pygame.display.get_surface(), white)
        draw_board(active_cell, cells, game, area)
        reset_btn = draw_button(
            width - buffer - button_border * 2 - button_width,
            height - button_height - button_border * 2 - buffer,
            button_width,
            button_height,
            button_border,
            inactive_btn,
            black,
            'Reset'
        )
        solve_btn = draw_button(
            width - buffer * 2 - button_border * 4 - button_width * 2,
            height - button_height - button_border * 2 - buffer,
            button_width,
            button_height,
            button_border,
            inactive_btn,
            black,
            'Visual Solve'
        )

        if reset_btn.collidepoint(pygame.mouse.get_pos()):
            reset_btn = draw_button(
                width - buffer - button_border * 2 - button_width,
                height - button_height - button_border * 2 - buffer,
                button_width,
                button_height,
                button_border,
                active_btn,
                black,
                'Reset'
            )
        if solve_btn.collidepoint(pygame.mouse.get_pos()):
            solve_btn = draw_button(
                width - buffer * 2 - button_border * 4 - button_width * 2,
                height - button_height - button_border * 2 - buffer,
                button_width,
                button_height,
                button_border,
                active_btn,
                black,
                'Visual Solve'
            )

        back_btn = draw_button(
            width - buffer * 3 - button_border * 6 - button_width * 3,
            height - button_height - button_border * 2 - buffer,
            button_width,
            button_height,
            button_border,
            inactive_btn,
            black,
            'Back'
        )
        if back_btn.collidepoint(pygame.mouse.get_pos()):
            back_btn = draw_button(
                width - buffer * 3 - button_border * 6 - button_width * 3,
                height - button_height - button_border * 2 - buffer,
                button_width,
                button_height,
                button_border,
                active_btn,
                black,
                'Back'
            )

        if not game.get_empty_cell():
            if check_sudoku(game):
                font = pygame.font.Font(None, 36)
                text = font.render('Solved!', 1, green)
                textbox = text.get_rect(center=(solve_rect.center))
                pygame.Surface.blit(pygame.display.get_surface() ,text, textbox)

        pygame.display.flip()


def level():
    global screen, run, lvl
    pygame.display.set_mode((300, height))

    while True:

        # Controller
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()

                if lvl1_btn.collidepoint(mouse_pos):
                    screen = "play"
                    lvl = 1
                    return
                if lvl2_btn.collidepoint(mouse_pos):
                    screen = "play"
                    lvl = 2
                    return
                if lvl3_btn.collidepoint(mouse_pos):
                    screen = "play"
                    lvl = 3
                    return
                if back_btn.collidepoint(mouse_pos):
                    screen = "menu"
                    return

        # GUI
        pygame.Surface.fill(pygame.display.get_surface(), white)
        lvl1_btn = draw_button(
            300 / 2 - (button_width + button_border) / 2,
            height - (button_height + button_border) * 9,
            button_width,
            button_height,
            button_border,
            inactive_btn,
            black,
            'Level 1'
        )
        if lvl1_btn.collidepoint(pygame.mouse.get_pos()):
            lvl1_btn = draw_button(
                300 / 2 - (button_width + button_border) / 2,
                height - (button_height + button_border) * 9,
                button_width,
                button_height,
                button_border,
                active_btn,
                black,
                'Level 1'
            )

        lvl2_btn = draw_button(
            300 / 2 - (button_width + button_border) / 2,
            height - (button_height + button_border) * 7,
            button_width,
            button_height,
            button_border,
            inactive_btn,
            black,
            'Level 2'
        )
        if lvl2_btn.collidepoint(pygame.mouse.get_pos()):
            lvl2_btn = draw_button(
                300 / 2 - (button_width + button_border) / 2,
                height - (button_height + button_border) * 7,
                button_width,
                button_height,
                button_border,
                active_btn,
                black,
                'Level 2'
            )

        lvl3_btn = draw_button(
            300 / 2 - (button_width + button_border) / 2,
            height - (button_height + button_border) * 5,
            button_width,
            button_height,
            button_border,
            inactive_btn,
            black,
            'Level 3'
        )
        if lvl3_btn.collidepoint(pygame.mouse.get_pos()):
            lvl3_btn = draw_button(
                300 / 2 - (button_width + button_border) / 2,
                height - (button_height + button_border) * 5,
                button_width,
                button_height,
                button_border,
                active_btn,
                black,
                'Level 3'
            )

        back_btn = draw_button(
            300 / 2 - (button_width + button_border) / 2,
            height - (button_height + button_border) * 3,
            button_width,
            button_height,
            button_border,
            inactive_btn,
            black,
            'Back'
        )
        if back_btn.collidepoint(pygame.mouse.get_pos()):
            back_btn = draw_button(
                300 / 2 - (button_width + button_border) / 2,
                height - (button_height + button_border) * 3,
                button_width,
                button_height,
                button_border,
                active_btn,
                black,
                'Back'
            )

        pygame.display.flip()


def menu():
    global screen, run
    pygame.display.set_mode((300, height))

    while True:

        # Controller
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()

                if play_btn.collidepoint(mouse_pos):
                    screen = "level"
                    return

        # GUI
        pygame.Surface.fill(pygame.display.get_surface(), white)
        play_btn = draw_button(
            300 / 2 - (button_width + button_border) / 2,
            height / 2 - (button_height + button_border) / 2,
            button_width,
            button_height,
            button_border,
            inactive_btn,
            black,
            'Play'
        )
        if play_btn.collidepoint(pygame.mouse.get_pos()):
            play_btn = draw_button(
                300 / 2 - (button_width + button_border) / 2,
                height / 2 - (button_height + button_border) / 2,
                button_width,
                button_height,
                button_border,
                active_btn,
                black,
                'Play'
            )

        pygame.display.flip()


def run():
    global screen, run
    while run:
        if screen == "menu":
            menu()
        elif screen == "level":
            level()
        elif screen == "play":
            play()
        else:
            raise Exception("Error: No Matching Surface")


if __name__ == '__main__':
    run()
