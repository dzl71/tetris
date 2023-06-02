import random as rnd
import os

BOARD_WIDTH = 10
BOARD_HEIGHT = 20
BLANK = "0"
BLOCK_CHAR = '1'

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
    'I' : 3 * (BLOCK_CHAR + '\n') + BLOCK_CHAR,
    
    'T' : 3 * BLOCK_CHAR + '\n' + BLANK + BLOCK_CHAR,
    
    'Z' : 2 * BLOCK_CHAR + '\n' + BLANK + 2 * BLOCK_CHAR,
    
    'S' : BLANK + 2 * BLOCK_CHAR + '\n' + 2 * BLOCK_CHAR,
    
    'L' : 2 * (BLOCK_CHAR + '\n') + 2 * BLOCK_CHAR,
    
    'J' : 2 * (BLANK + BLOCK_CHAR + '\n') + 2 * BLOCK_CHAR,
    
    'O' : 2 * BLOCK_CHAR + '\n' + 2 * BLOCK_CHAR
}

shapes_l = {
    'I' : 3 * (BLOCK_CHAR + '\n') + BLOCK_CHAR,
    
    'T' : 3 * BLOCK_CHAR + '\n' + BLANK + BLOCK_CHAR,
    
    'Z' : 2 * BLOCK_CHAR + '\n' + BLANK + 2 * BLOCK_CHAR,
    
    'S' : BLANK + 2 * BLOCK_CHAR + '\n' + 2 * BLOCK_CHAR,
    
    'L' : 2 * (BLOCK_CHAR + '\n') + 2 * BLOCK_CHAR,
    
    'J' : 2 * (BLANK + BLOCK_CHAR + '\n') + 2 * BLOCK_CHAR,
    
    'O' : 2 * BLOCK_CHAR + '\n' + 2 * BLOCK_CHAR
}

shapes_180 =  {
    'I' : 3 * (BLOCK_CHAR + '\n') + BLOCK_CHAR,
    
    'T' : 3 * BLOCK_CHAR + '\n' + BLANK + BLOCK_CHAR,
    
    'Z' : 2 * BLOCK_CHAR + '\n' + BLANK + 2 * BLOCK_CHAR,
    
    'S' : BLANK + 2 * BLOCK_CHAR + '\n' + 2 * BLOCK_CHAR,
    
    'L' : 2 * (BLOCK_CHAR + '\n') + 2 * BLOCK_CHAR,
    
    'J' : 2 * (BLANK + BLOCK_CHAR + '\n') + 2 * BLOCK_CHAR,
    
    'O' : 2 * BLOCK_CHAR + '\n' + 2 * BLOCK_CHAR
}

class block:
    def __init__(self, starting_ptr: tuple[int, int]) -> None:
        self.falling = True
        self.rotated_right_amount = 0
        self.rotated_left_amount = 0
        self.name = rnd.choice(list(shapes))
        self.shape = shapes[self.name][0]
        self.width = shapes[self.name][1][0]
        self.height = shapes[self.name][1][1]
        self.row_position_ptr = starting_ptr[0]
        self.column_position_ptr = starting_ptr[1]
    
    def insert_into_board(self, board: list[list]):
        row_num = self.row_position_ptr
        col_num = self.column_position_ptr
        for blk in self.shape:
            if blk == '\n':
                row_num += 1
                col_num = self.column_position_ptr
            else:
                if blk == BLOCK_CHAR:
                    board[row_num][col_num] = BLOCK_CHAR
                col_num += 1
                 
            
    def remove_from_board(self, board: list[list]):
        os.system('clear')
        row_num = self.row_position_ptr
        col_num = self.column_position_ptr
        for blk in self.shape:
            if blk == '\n':
                row_num += 1
                col_num = self.column_position_ptr
                board[row_num][col_num] = BLANK
            else:
                board[row_num][col_num] = BLANK
                col_num += 1
        
    def rotate_right(self, board: list[list]):
        self.remove_from_board(board)
        match self.rotated_right_amount:
            case 0:
                self.shape = shapes_r[self.name]
                self.rotated_right_amount = 1,
            case 1: 
                self.shape = shapes_180[self.name],
                self.rotated_right_amount = 2
            case 2:
                self.shape = shapes_l[self.name],
                self.rotated_right_amount = 3,
            case 3:
                self.shape = shapes[self.name],
                self.rotated_right_amount = 0
        self.insert_into_board(board)
    
    def rotate_left(self, board: list[list]):
        self.remove_from_board(board)
        match self.rotated_left_amount:
            case 0:
                self.shape = shapes_l[self.name]
                self.rotated_left_amount = 1,
            case 1: 
                self.shape = shapes_180[self.name],
                self.rotated_left_amount = 2
            case 2:
                self.shape = shapes_r[self.name],
                self.rotated_left_amount = 3,
            case 3:
                self.shape = shapes[self.name],
                self.rotated_left_amount = 0
        self.insert_into_board(board)
    
    def move_down(self, board: list[list]):
        self.remove_from_board(board)
        if self.row_position_ptr + self.height < BOARD_HEIGHT:
            self.row_position_ptr += 1
        else:
            self.falling = False
        self.insert_into_board(board)
    
    def move_left(self, board: list[list]):
        self.remove_from_board(board)
        if self.column_position_ptr > 0:
            self.column_position_ptr -= 1
        self.insert_into_board(board)

    def move_right(self, board: list[list]):
        self.remove_from_board(board)
        if self.width + self.column_position_ptr < BOARD_WIDTH:
            self.column_position_ptr += 1
        self.insert_into_board(board)
    
    def is_able_to_fall(self, board: list[list]):
        pass