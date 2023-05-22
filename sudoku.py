# pylint: skip-file
import pygame
import random
import sys
import time
from solver import Sudoku

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
    def __init__(self, papan, left, top, row, col):
        super().__init__(left, top, cell_size, cell_size)
        self.row = row
        self.col = col
        self.papan = papan


def create_cells(data):
    cells = []
    p = 0
    while p < len(data):
        cells.append([])
        row = 0
        col = 0
        left = buffer + major_grid_size + (p*310)
        top = buffer + major_grid_size + (p*310)
        while row < 9:
            cells[p].append([])
            while col < 9:
                cells[p][row].append(RectCell(p, left, top, row, col))

                left += cell_size + minor_grid_size
                if col != 0 and (col + 1) % 3 == 0:
                    left = left + major_grid_size - minor_grid_size
                col += 1

            top += cell_size + minor_grid_size
            if row != 0 and (row + 1) % 3 == 0:
                top = top + major_grid_size - minor_grid_size
            left = buffer + major_grid_size + (p*310)
            col = 0
            row += 1
        p += 1

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
def draw_grid_lvl3(area):
    # draw BG
    # Diagonal
    pygame.draw.line(pygame.display.get_surface(), black, (5, 6),
                     (472, 6), 3)
    pygame.draw.line(pygame.display.get_surface(), black, (471, 316),
                     (472+316, 316), 3)
    pygame.draw.line(pygame.display.get_surface(), black, (5, 471),
                     (316, 471), 3)
    pygame.draw.line(pygame.display.get_surface(), black, (316, 471+316),
                     (472+316, 471+316), 3)
    # Horizontal
    pygame.draw.line(pygame.display.get_surface(), black, (6, 5),
                     (6, 472), 3)
    pygame.draw.line(pygame.display.get_surface(), black, (316, 471),
                     (316, 472+316), 3)
    pygame.draw.line(pygame.display.get_surface(), black, (471, 5),
                     (471, 316), 3)
    pygame.draw.line(pygame.display.get_surface(), black, (471+316, 316),
                     (471+316, 472+316), 3)

    jarak = [6, 58, 109, 161, 213, 264, 316, 368,
             419, 471, 523, 574, 626, 678, 729, 781]
    # 6, 58, 109, 161, 213, 264, 316, 368, 419, 471, 523, 574, 626, 678, 729, 781
    #  52   51  52   52    51   52   52  51   52   52   51  52   52    51   52
    # loop 9 times
    # sumbu Y
    for p in range(len(area)):
        for i in range(9):
            for j in range(8):
                if area[p][i][j] == area[p][i][j + 1]:
                    pygame.draw.line(pygame.display.get_surface(), black, (jarak[(j + 1)+(p*6)], jarak[i+(p*6)]),
                                     (jarak[(j + 1)+(p*6)], jarak[(i + 1)+(p*6)]), minor_grid_size)
                else:
                    pygame.draw.line(pygame.display.get_surface(), black, (jarak[(j + 1)+(p*6)], jarak[i+(p*6)]),
                                     (jarak[(j + 1)+(p*6)], jarak[(i + 1)+(p*6)]), major_grid_size)
    # sumbu X
    for p in range(len(area)):
        for i in range(8):
            for j in range(9):
                if area[p][i][j] == area[p][i + 1][j]:
                    pygame.draw.line(pygame.display.get_surface(), black, (jarak[j+(p*6)], jarak[(i + 1)+(p*6)]),
                                     (jarak[(j + 1)+(p*6)], jarak[(i + 1)+(p*6)]), minor_grid_size)
                else:
                    pygame.draw.line(pygame.display.get_surface(), black, (jarak[j+(p*6)], jarak[(i + 1)+(p*6)]),
                                     (jarak[(j + 1)+(p*6)], jarak[(i + 1)+(p*6)]), major_grid_size)


def fill_cells(cells, board):
    font = pygame.font.Font(None, 36)

    for p in range(len(board.board)):
        for row in range(9):
            for col in range(9):
                if board.board[p][row][col].value is None:
                    continue

                if not board.board[p][row][col].editable:
                    font.bold = True
                    text = font.render(
                        f'{board.board[p][row][col].value}', 1, black)

                else:
                    font.bold = False
                    if board.check_move(board.board[p][row][col], board.board[p][row][col].value):
                        text = font.render(
                            f'{board.board[p][row][col].value}', 1, green)
                    else:
                        text = font.render(
                            f'{board.board[p][row][col].value}', 1, red)

                xpos, ypos = cells[p][row][col].center
                textbox = text.get_rect(center=(xpos, ypos))
                pygame.Surface.blit(
                    pygame.display.get_surface(), text, textbox)


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
        draw_grid_lvl3(area)
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


def find_region(dict, i, j):
    for v, d in dict.items():
        if (i, j) in d:
            return v

# def visual_solve(game, cells, area):
#     cell = game.get_empty_cell()

#     if not cell:
#         return True

#     for p in range(len(area)):
#         for val in range(1, 10):
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     sys.exit()

#             cell.value = val

#             pygame.Surface.fill(pygame.display.get_surface(), white)
#             draw_board(None, cells, game, area)
#             cell_rect = cells[p][cell.row][cell.col]
#             pygame.draw.rect(pygame.display.get_surface(), red, cell_rect, 5)
#             pygame.display.update([cell_rect])
#             time.sleep(0.05)

#             if not game.check_move(cell, val):
#                 cell.value = None
#                 continue

#             pygame.Surface.fill(pygame.display.get_surface(), white)
#             pygame.draw.rect(pygame.display.get_surface(), green, cell_rect, 5)
#             draw_board(None, cells, game, area)
#             pygame.display.update([cell_rect])
#             if visual_solve(game, cells, area):
#                 return True

#             cell.value = None

#     pygame.Surface.fill(pygame.display.get_surface(), white)
#     pygame.draw.rect(pygame.display.get_surface(), white, cell_rect, 5)
#     draw_board(None, cells, game, area)
#     pygame.display.update([cell_rect])
#     return False


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
                    cntRow += 1
                if p > 0 and regional_points == 1 and value in r[p-1][col+6]:
                    cntCol += 1
                if value in row_sets[row] or value in col_sets[col] or cntRow > 1 or cntCol > 1:
                    return False
                box_sets[region_key] = set(
                ) if box_sets[region_key] is None else box_sets[region_key]
                if value in box_sets[region_key]:
                    return False
                row_sets[row].add(value)
                col_sets[col].add(value)
                box_sets[region_key].add(value)
        r.append(row_sets)
        c.append(col_sets)
        b.append(box_sets)
    return True


N = 9


def isSafe(grid, row, col, num):

    for x in range(9):
        if grid[row][x] == num:
            return False

    for x in range(9):
        if grid[x][col] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True


def solveSudoku(grid, row, col):

    if (row == N - 1 and col == N):
        return True

    if col == N:
        row += 1
        col = 0

    if grid[row][col] > 0:
        return solveSudoku(grid, row, col + 1)
    for num in range(1, N + 1, 1):

        if isSafe(grid, row, col, num):

            grid[row][col] = num

            if solveSudoku(grid, row, col + 1):
                return True

        grid[row][col] = 0
    return False


def hint(game, len_p, len_r, len_c, data, area):
    data2 = [
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
    solveSudoku(data2, 0, 0)
    if len_p > 1:
        p = random.randrange(0, len_p-1)
    else:
        p = len_p-1
    r = random.randrange(0, len_r-1)
    c = random.randrange(0, len_c-1)
    val = random.randrange(1, 9)
    game.board[p][r][c].value = data2[r][c]


def play():
    global screen, run, lvl
    num = random.randint(0, 2)
    if lvl == 1:
        pygame.display.set_mode(
            (width + button_width + button_border*2 + buffer*2, 472 + buffer))
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
                    [0, 9, 5, 0, 7, 8, 3, 4, 2],
                    [0, 0, 0, 0, 4, 1, 0, 6, 0],
                    [4, 6, 7, 0, 3, 9, 5, 0, 1],
                    [0, 8, 0, 4, 0, 0, 0, 0, 0],
                    [5, 0, 6, 0, 0, 0, 2, 9, 0],
                    [0, 0, 0, 0, 9, 0, 8, 0, 5],
                    [8, 0, 4, 9, 0, 0, 0, 0, 3],
                    [0, 0, 0, 0, 5, 0, 0, 2, 0],
                    [0, 5, 1, 3, 6, 0, 0, 0, 0]
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
                    [3, 7, 4, 2, 0, 8, 5, 0, 1],
                    [0, 0, 5, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 9, 0, 0, 1, 0, 8, 0, 0],
                    [2, 0, 8, 9, 0, 0, 7, 0, 5],
                    [7, 5, 0, 0, 2, 4, 1, 9, 0],
                    [5, 0, 0, 7, 0, 2, 9, 0, 0],
                    [0, 0, 9, 3, 8, 1, 2, 0, 7],
                    [0, 0, 7, 4, 0, 9, 6, 1, 0]
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
        pygame.display.set_mode(
            (width + button_width + button_border*2 + buffer*2, 472 + buffer))
        if num == 0:
            data = [
                [
                    [7, 0, 0, 8, 2, 3, 0, 9, 0],
                    [0, 0, 3, 0, 0, 0, 0, 0, 8],
                    [0, 0, 0, 9, 0, 6, 0, 5, 0],
                    [2, 0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 5, 0, 0],
                    [0, 0, 0, 0, 5, 0, 0, 0, 2],
                    [0, 7, 0, 1, 0, 8, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0, 2, 0, 0],
                    [0, 6, 0, 2, 7, 5, 0, 0, 4]
                ]
            ]
            area = [
                [
                    [1, 1, 1, 1, 3, 3, 3, 3, 3],
                    [2, 1, 1, 1, 3, 3, 3, 4, 4],
                    [2, 1, 2, 1, 2, 5, 3, 4, 4],
                    [2, 2, 2, 2, 2, 5, 5, 4, 4],
                    [7, 7, 5, 5, 5, 5, 5, 4, 4],
                    [7, 7, 7, 6, 6, 5, 6, 4, 6],
                    [7, 7, 7, 8, 6, 6, 6, 6, 6],
                    [7, 8, 8, 8, 9, 9, 9, 9, 9],
                    [8, 8, 8, 8, 8, 9, 9, 9, 9]
                ]
            ]
        elif num == 1:
            data = [
                [
                    [5, 0, 0, 7, 0, 0, 0, 9, 2],
                    [0, 0, 0, 0, 3, 0, 1, 0, 0],
                    [0, 8, 6, 0, 0, 0, 0, 0, 7],
                    [0, 0, 0, 8, 9, 0, 0, 0, 0],
                    [1, 2, 0, 0, 0, 0, 0, 3, 5],
                    [0, 0, 0, 0, 4, 1, 0, 0, 0],
                    [7, 0, 0, 0, 0, 0, 3, 8, 0],
                    [0, 0, 3, 0, 1, 0, 0, 0, 0],
                    [8, 5, 0, 0, 0, 9, 0, 0, 1]
                ]
            ]
            area = [
                [
                    [1, 1, 6, 6, 7, 7, 8, 8, 8],
                    [1, 1, 6, 6, 6, 7, 7, 8, 8],
                    [1, 1, 6, 5, 6, 7, 7, 8, 8],
                    [1, 5, 6, 5, 7, 7, 9, 8, 8],
                    [1, 5, 6, 5, 7, 9, 9, 9, 9],
                    [1, 5, 5, 5, 5, 9, 9, 9, 4],
                    [2, 2, 2, 2, 3, 4, 4, 9, 4],
                    [2, 2, 2, 3, 3, 3, 4, 4, 4],
                    [2, 2, 3, 3, 3, 3, 3, 4, 4]
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
        pygame.display.set_mode((width+316, height+316))
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
            ],
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
        raise Exception("Level Error: Out Of Bound")

    dictConv(area)
    game = Sudoku(data, region_dict)
    # printdict(region_dict[0])

    cells = create_cells(data)
    active_cell = None
    solve_rect = pygame.Rect(
        buffer,
        height - button_height - button_border * 2 - buffer,
        button_width + button_border * 2,
        button_height + button_border * 2
    )

    if lvl != 3:
        btn_x = width + buffer
        reset_x = btn_x
        solve_x = btn_x
        hint_x = btn_x
        back_x = btn_x

        reset_y = buffer
        solve_y = button_height + button_border*2 + buffer*3
        hint_y = button_height*2 + button_border*4 + buffer*5
        back_y = button_height*3 + button_border*6 + buffer*7
    else:
        btn_x = (width+316)/2 - (button_width*4 + button_border*8 + buffer*6)/2
        reset_x = btn_x
        solve_x = btn_x + (button_width + button_border*2 + buffer*2)
        hint_x = btn_x + (button_width*2 + button_border*4 + buffer*4)
        back_x = btn_x + (button_width*3 + button_border*6 + buffer*6)

        btn_y = (height+316) - (button_height + button_border*2 + buffer)
        reset_y = btn_y
        solve_y = btn_y
        hint_y = btn_y
        back_y = btn_y

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
                #     draw_board(active_cell, cells, game, area)
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
                #     visual_solve(game, cells, area)

                if back_btn.collidepoint(mouse_pos):
                    screen = "level"
                    return

                if hint_btn.collidepoint(mouse_pos):
                    hint(game, len(data), len(data[0]), len(
                        data[0][0]), data, area)

                active_cell = None
                for p in cells:
                    for row in p:
                        for cell in row:
                            if cell.collidepoint(mouse_pos):
                                active_cell = cell
                # ini harus diganti untuk multisudoku
                if active_cell and not game.board[active_cell.papan][active_cell.row][active_cell.col].editable:
                    active_cell = None

            if event.type == pygame.KEYUP:
                if active_cell is not None:
                    # harus diganti ketika multisudoku
                    if event.key == pygame.K_0 or event.key == pygame.K_KP0:
                        game.board[active_cell.papan][active_cell.row][active_cell.col].value = 0
                    if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                        game.board[active_cell.papan][active_cell.row][active_cell.col].value = 1
                    if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                        game.board[active_cell.papan][active_cell.row][active_cell.col].value = 2
                    if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                        game.board[active_cell.papan][active_cell.row][active_cell.col].value = 3
                    if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                        game.board[active_cell.papan][active_cell.row][active_cell.col].value = 4
                    if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                        game.board[active_cell.papan][active_cell.row][active_cell.col].value = 5
                    if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                        game.board[active_cell.papan][active_cell.row][active_cell.col].value = 6
                    if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                        game.board[active_cell.papan][active_cell.row][active_cell.col].value = 7
                    if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                        game.board[active_cell.papan][active_cell.row][active_cell.col].value = 8
                    if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                        game.board[active_cell.papan][active_cell.row][active_cell.col].value = 9
                    if event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                        game.board[active_cell.papan][active_cell.row][active_cell.col].value = None

        # GUI
        pygame.Surface.fill(pygame.display.get_surface(), white)
        draw_board(active_cell, cells, game, area)

        reset_btn = draw_button(
            reset_x,
            reset_y,
            button_width,
            button_height,
            button_border,
            inactive_btn,
            black,
            'Reset'
        )
        solve_btn = draw_button(
            solve_x,
            solve_y,
            button_width,
            button_height,
            button_border,
            inactive_btn,
            black,
            'Visual Solve'
        )

        if reset_btn.collidepoint(pygame.mouse.get_pos()):
            reset_btn = draw_button(
                reset_x,
                reset_y,
                button_width,
                button_height,
                button_border,
                active_btn,
                black,
                'Reset'
            )
        if solve_btn.collidepoint(pygame.mouse.get_pos()):
            solve_btn = draw_button(
                solve_x,
                solve_y,
                button_width,
                button_height,
                button_border,
                active_btn,
                black,
                'Visual Solve'
            )

        hint_btn = draw_button(
            hint_x,
            hint_y,
            button_width,
            button_height,
            button_border,
            inactive_btn,
            black,
            'Hint'
        )
        if hint_btn.collidepoint(pygame.mouse.get_pos()):
            hint_btn = draw_button(
                hint_x,
                hint_y,
                button_width,
                button_height,
                button_border,
                active_btn,
                black,
                'Hint'
            )

        back_btn = draw_button(
            back_x,
            back_y,
            button_width,
            button_height,
            button_border,
            inactive_btn,
            black,
            'Back'
        )
        if back_btn.collidepoint(pygame.mouse.get_pos()):
            back_btn = draw_button(
                back_x,
                back_y,
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
                pygame.Surface.blit(
                    pygame.display.get_surface(), text, textbox)

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
                if credit_btn.collidepoint(mouse_pos):
                    screen = "credit"
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

        credit_btn = draw_button(
            300 / 2 - (button_width + button_border) / 2,
            height / 2 + (button_height + button_border),
            button_width,
            button_height,
            button_border,
            inactive_btn,
            black,
            'Credit'
        )
        if credit_btn.collidepoint(pygame.mouse.get_pos()):
            credit_btn = draw_button(
                300 / 2 - (button_width + button_border) / 2,
                height / 2 + (button_height + button_border),
                button_width,
                button_height,
                button_border,
                active_btn,
                black,
                'Credit'
            )

        pygame.display.flip()


def display_text(text, pos, font, color):
    collection = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]
    x, y = pos
    for lines in collection:
        for words in lines:
            word_surface = font.render(words, True, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= 800:
                x = pos[0]
                y += word_height
            pygame.Surface.blit(
                pygame.display.get_surface(), word_surface, (x, y))
            x += word_width + space
        x = pos[0]
        y += word_height


def credit():
    global screen, run
    pygame.display.set_mode((width+100, height))
    while True:

        # Controller
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()

                if back_btn.collidepoint(mouse_pos):
                    screen = "menu"
                    return
        # GUI
        pygame.Surface.fill(pygame.display.get_surface(), white)

        back_btn = draw_button(
            (width+100) / 2 - (button_width + button_border) / 2,
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
                (width+100) / 2 - (button_width + button_border) / 2,
                height - (button_height + button_border) * 3,
                button_width,
                button_height,
                button_border,
                active_btn,
                black,
                'Back'
            )
        font = pygame.font.SysFont('Comic Sans', 25)
        text = "                          Contributors:\n\nMoh Rosy Haqqy Aminy : 5025211012 : hqlco\n\n  M. Hafidh Rosyadi : 5025211013 : Hfdrsyd\n\n   Hammuda Arsyad : 5025211146 : H-mD"
        display_text(text, (35, 40), font, black)

        pygame.display.flip()


def run():
    global screen, run
    while run:
        if screen == "menu":
            menu()
        elif screen == "credit":
            credit()
        elif screen == "level":
            level()
        elif screen == "play":
            play()
        else:
            raise Exception("Error: No Matching Surface")


if __name__ == '__main__':
    run()
