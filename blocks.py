import random as rnd
import os
import time

BOARD_WIDTH = 10
BOARD_HEIGHT = 20
BLANK = "0"
BLOCK_CHAR = '1'

BLOCK = '[]'
EMPTY = "  "

CLEAR_TERMINAL = 'clear'

STANDART_INPUT_DELAY = 0.0875
NO_DELAY = 0

def print_board(board: list[list], delay):
    print((BOARD_WIDTH  + 1 ) * '--')
    for row in board:
        print('|', end='')
        for tile in row:
            if tile[0] == BLANK:
                print(EMPTY, end='')
            else:
                print(BLOCK, end='')
        print('|')
    print((BOARD_WIDTH  + 1 ) * '--')
    time.sleep(delay)

shapes = {
    'I' : (3 * (BLOCK_CHAR + '\n') + BLOCK_CHAR, (1, 4)),
    
    'T' : (3 * BLOCK_CHAR + '\n' + BLANK + BLOCK_CHAR, (3, 2)),
    
    'Z' : (2 * BLOCK_CHAR + '\n' + BLANK + 2 * BLOCK_CHAR, (3, 2)),
    
    'S' : (BLANK + 2 * BLOCK_CHAR + '\n' + 2 * BLOCK_CHAR, (3, 2)),
    
    'L' : (2 * (BLOCK_CHAR + '\n') + 2 * BLOCK_CHAR, (2, 3)),
    
    'J' : (2 * (BLANK + BLOCK_CHAR + '\n') + 2 * BLOCK_CHAR, (2, 3)),
    
    'O' : (2 * BLOCK_CHAR + '\n' + 2 * BLOCK_CHAR, (2, 2))
}

shapes_r = {
    'I' : (4 * BLOCK_CHAR, (4, 1)),
    
    'T' : (BLANK + BLOCK_CHAR + '\n' + 2 * BLOCK_CHAR + '\n' + BLANK + BLOCK_CHAR, (2, 3)),
    
    'Z' : (BLANK + BLOCK_CHAR + '\n' + 2 * BLOCK_CHAR + '\n' + BLOCK_CHAR + BLANK, (2, 3)),
    
    'S' : (BLOCK_CHAR + BLANK +  '\n' + 2 * BLOCK_CHAR + '\n' + BLANK + BLOCK_CHAR, (2, 3)),
    
    'L' : (3 * BLOCK_CHAR + '\n' + BLOCK_CHAR, (3, 2)),
    
    'J' : (BLOCK_CHAR + '\n' + 3 * BLOCK_CHAR, (3, 2)),
    
    'O' : (2 * BLOCK_CHAR + '\n' + 2 * BLOCK_CHAR, (2, 2))
}

shapes_l = {
    'I' : (3 * (BLOCK_CHAR + '\n') + BLOCK_CHAR, (1, 4)),
    
    'T' : (3 * BLOCK_CHAR + '\n' + BLANK + BLOCK_CHAR, (3, 2)),
    
    'Z' : (2 * BLOCK_CHAR + '\n' + BLANK + 2 * BLOCK_CHAR, (3, 2)),
    
    'S' : (BLANK + 2 * BLOCK_CHAR + '\n' + 2 * BLOCK_CHAR, (3, 2)),
    
    'L' : (2 * (BLOCK_CHAR + '\n') + 2 * BLOCK_CHAR, (2, 3)),
    
    'J' : (2 * (BLANK + BLOCK_CHAR + '\n') + 2 * BLOCK_CHAR, (2, 3)),
    
    'O' : (2 * BLOCK_CHAR + '\n' + 2 * BLOCK_CHAR, (2, 2))
}

shapes_180 =  {
    'I' : (3 * (BLOCK_CHAR + '\n') + BLOCK_CHAR, (1, 4)),
    
    'T' : (3 * BLOCK_CHAR + '\n' + BLANK + BLOCK_CHAR, (3, 2)),
    
    'Z' : (2 * BLOCK_CHAR + '\n' + BLANK + 2 * BLOCK_CHAR, (3, 2)),
    
    'S' : (BLANK + 2 * BLOCK_CHAR + '\n' + 2 * BLOCK_CHAR, (3, 2)),
    
    'L' : (2 * (BLOCK_CHAR + '\n') + 2 * BLOCK_CHAR, (2, 3)),
    
    'J' : (2 * (BLANK + BLOCK_CHAR + '\n') + 2 * BLOCK_CHAR, (2, 3)),
    
    'O' : (2 * BLOCK_CHAR + '\n' + 2 * BLOCK_CHAR, (2, 2))
}

class block:
    def __init__(self, starting_ptr: tuple[int, int], serial_num: int) -> None:
        self.direction: str = 'up'
        
        self.name = rnd.choice(list(shapes))
        self.shape = shapes[self.name][0]
        self.serial_num = serial_num
        self.falling = True
                
        self.row_position_ptr = starting_ptr[0]
        self.height = shapes[self.name][1][1]
        
        self.column_position_ptr = starting_ptr[1]
        self.width = shapes[self.name][1][0]
        
    def change_shape(self, new_shape: dict[str, tuple[str, tuple[int, int]]]):
        self.shape = new_shape[self.name][0]
        self.width = new_shape[self.name][1][0]
        self.height = new_shape[self.name][1][1]
    
    def insert_into_board(self, board: list[list], delay):
        row_num = self.row_position_ptr
        col_num = self.column_position_ptr
        for blk in self.shape:
            if blk == '\n':
                row_num += 1
                col_num = self.column_position_ptr
            else:
                if blk == BLOCK_CHAR:
                    board[row_num][col_num] = (BLOCK_CHAR, self.serial_num)
                col_num += 1
        print_board(board, delay)
                 
            
    def remove_from_board(self, board: list[list]):
        os.system(CLEAR_TERMINAL)
        row_num = self.row_position_ptr
        col_num = self.column_position_ptr
        for blk in self.shape:
            if blk == '\n':
                row_num += 1
                col_num = self.column_position_ptr
                board[row_num][col_num] = (BLANK, 0)
            else:
                board[row_num][col_num] = (BLANK, 0)
                col_num += 1
        
    def rotate_right(self, board: list[list]):
        self.remove_from_board(board)
        match self.direction:
            case 'up':
                self.change_shape(shapes_r)
                self.direction = 'right'
            case 'right': 
                self.change_shape(shapes_180)
                self.direction = 'down'
            case 'down':
                self.change_shape(shapes_l)
                self.direction = 'left'
            case 'left':
                self.change_shape(shapes)
                self.direction = 'up'
        self.insert_into_board(board, STANDART_INPUT_DELAY)
    
    def rotate_left(self, board: list[list]):
        self.remove_from_board(board)
        match self.direction:
            case 'up':
                self.change_shape(shapes_r)
                self.direction = 'left'
            case 'right': 
                self.change_shape(shapes_180)
                self.direction = 'up'
            case 'down':
                self.change_shape(shapes_l)
                self.direction = 'right'
            case 'left':
                self.change_shape(shapes)
                self.direction = 'down'
        self.insert_into_board(board, STANDART_INPUT_DELAY)
    
    def move_down(self, board: list[list]):
        self.remove_from_board(board)
        if self.row_position_ptr + self.height < BOARD_HEIGHT:
            self.falling = self.is_able_to_fall(board)
        if self.falling:
            self.row_position_ptr += 1
        self.insert_into_board(board, NO_DELAY)
    
    def move_left(self, board: list[list]):
        able_to_go_left: bool = True
        self.remove_from_board(board)
        if self.column_position_ptr > 0:
            for row_idx in range(self.row_position_ptr, self.row_position_ptr + self.height):
                if 0 < board[row_idx][self.column_position_ptr - 1][1] < self.serial_num:
                    able_to_go_left = False
        else:
            able_to_go_left = False
        if able_to_go_left:
            self.column_position_ptr -= 1
        self.insert_into_board(board, STANDART_INPUT_DELAY)

    def move_right(self, board: list[list]):
        able_to_move = True
        self.remove_from_board(board)
        if self.width + self.column_position_ptr < BOARD_WIDTH:
            for row_idx in range(self.row_position_ptr, self.row_position_ptr + self.height):
                if 0 < board[row_idx][self.column_position_ptr + self.width][1] < self.serial_num:
                    able_to_move = False
        else:
            able_to_move = False
        if able_to_move:
            self.column_position_ptr += 1
        self.insert_into_board(board, STANDART_INPUT_DELAY)
    
    def is_able_to_fall(self, board: list[list]) -> bool:
        if self.row_position_ptr + self.height + 1 > BOARD_HEIGHT:
            return False
        for row_idx in range(self.row_position_ptr, self.row_position_ptr + self.height):
            for col_idx in range(self.column_position_ptr, self.column_position_ptr + self.width):
                if board[row_idx][col_idx][1] > board[row_idx + 1][col_idx][1] and board[row_idx + 1][col_idx][1] != 0:
                    return False
        return True
