# pylint: skip-file

class Cell:
    def __init__(self, area, papan ,row, col, value, editable):
        self.row = row
        self.col = col
        self.value = value
        self._editable = editable
        self.Rarea = area
        self.papan = papan

    @property
    def row(self):
        return self._row

    @row.setter
    def row(self, row):
        if row < 0 or row > 8:
            raise AttributeError('Row must be between 0 and 8.')
        else:
            self._row = row

    @property
    def col(self):
        return self._col

    @col.setter
    def col(self, col):
        if col < 0 or col > 8:
            raise AttributeError('Col must be between 0 and 8.')
        else:
            self._col = col

    @property
    def value(self):
        return self._value

    @property
    def editable(self):
        return self._editable

    def __repr__(self):
        return f'{self.__class__.__name__}({self.value})'

    @value.setter
    def value(self, value):
        if value is not None and (value < 1 or value > 9):
            raise AttributeError('Value must be between 1 and 9.')
        else:
            self._value = value


class Sudoku:
    def __init__(self, board,areaM):
        self.board = []
        self.area = []
        for papan in range(len(board)):
            self.board.append([])
            self.area.append(areaM[papan])
            for row in range(9):
                self.board[papan].append([])
                for col in range(9):
                    if board[papan][row][col] == 0:
                        val = None
                        editable = True
                    else:
                        val = board[papan][row][col]
                        editable = False
                    self.board[papan][row].append(Cell(self.find_region(self.area[papan],row,col),papan, row, col, val, editable))


    def find_region(self, region_dict, i, j):
        for v, d in region_dict.items():
            if (i, j) in d:
                return v


    def check_move(self, cell, num):
        for col in range(9):
            if self.board[cell.papan][cell.row][col].value == num and col != cell.col:
                return False
        for row in range(9):
            if self.board[cell.papan][row][cell.col].value == num and row != cell.row:
                return False
        for (i, j) in self.area[cell.papan][cell.Rarea]:
            if self.board[cell.papan][i][j].value == num and i != cell.row and j != cell.col:
                return False

        return True

    def get_possible_moves(self, cell):
        possible_moves = [num for num in range(1, 10)]

        for col in range(9):
            if self.board[cell.papan][cell.row][col].value in possible_moves:
                possible_moves.remove(self.board[cell.row][col].value)

        for row in range(9):
            if self.board[cell.papan][row][cell.col].value in possible_moves:
                possible_moves.remove(self.board[row][cell.col].value)
        # kasus apabila papan pertama area 9 diisi
        regional_point = self.find_region(self.area[cell.papan], cell.row, cell.col)
        if cell.papan == 0 and regional_point == 9 and len(self.area)==2:
            for col in range(9):
                if self.board[1][cell.row-6][col].value in possible_moves:
                    possible_moves.remove(self.board[2][cell.row-6][col].value)
            for row in range(9):
                if self.board[1][row][cell.col -6].value in possible_moves:
                    possible_moves.remove(self.board[2][row][cell.col -6].value)
        # kasus apabila papan kedua area 1 diisi
        # boleh pilih salah satu karena intesect
        elif cell.papan == 1 and regional_point == 1 and len(self.area)==2:
            for col in range(9):
                if self.board[0][cell.row+6][col].value in possible_moves:
                    possible_moves.remove(self.board[2][cell.row+6][col].value)
            for row in range(9):
                if self.board[0][row][cell.col + 6].value in possible_moves:
                    possible_moves.remove(self.board[2][row][cell.col + 6].value)
        
        for i, j in self.area[cell.papan][regional_point]:
            if self.board[cell.papan][i][j].value in possible_moves:
                possible_moves.remove(self.board[cell.papan][i][j].value)

        return possible_moves

    def get_empty_cell(self):
        for p in range(len(self.board)):
            for row in range(9):
                for col in range(9):
                    if self.board[p][row][col].value is None:
                        return self.board[p][row][col]
        return False

    def solve(self):
        cell = self.get_empty_cell()

        if not cell:
            return True

        for val in range(1, 10):
            if not (cell.papan == 0 and cell.Rarea == "region_9") or not (cell.papan == 1 and cell.Rarea == "region_1"):
                if not self.check_move(cell, val):
                    continue
            if (cell.papan == 0 and cell.Rarea == "region_9"):
                if not (self.check_move(cell, val) and self.check_move(self.board[1][cell.row-6][cell.col-6],val)):
                    continue
                self.board[1][cell.row-6][cell.col-6].value = val
            if (cell.papan == 1 and cell.Rarea == "region_1"):
                if not (self.check_move(cell, val) and self.check_move(self.board[0][cell.row+6][cell.col+6],val)):
                    continue
                self.board[1][cell.row+6][cell.col-+6] = val
            cell.value = val
            
            if self.solve():
                return True
            if (cell.papan == 0 and cell.Rarea == "region_9"):
                self.board[1][cell.row-6][cell.col-6].value = None
            if (cell.papan == 1 and cell.Rarea == "region_1"):
                self.board[0][cell.row+6][cell.col+6].value = None
            cell.value = None

        return False

    def get_board(self):
        return [[[self.board[p][row][col].value for col in range(9)] for row in range(9)]for p in range(len(self.board))]

    def test_solve(self):
        current_board = self.get_board()
        solvable = self.solve()

        for row in range(9):
            for col in range(9):
                self.board[row][col].value = current_board[row][col]

        return solvable

    def reset(self):
        for p in range(len(self.board)):
            for row in self.board[p]:
                for cell in row:
                    if cell.editable:
                        cell.value = None

    def __str__(self):
        board = ' -----------------------\n'
        for row, line in enumerate(self.board):
            board += '|'
            for col, cell in enumerate(line):
                if cell.value is None:
                    val = '-'
                else:
                    val = cell.value
                if col < 8:
                    board += f' {val}'
                    if (col + 1) % 3 == 0:
                        board += ' |'
                else:
                    board += f' {val} |\n'
            if row < 8 and (row + 1) % 3 == 0:
                board += '|-------|-------|-------|\n'
        board += ' -----------------------\n'
        return board