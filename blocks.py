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
    """
    The function prints a game board represented by a list of lists with a specified delay between each
    print.
    
    :param board: A 2D list representing the game board, where each element is a tuple containing
    information about a tile on the board
    :type board: list[list]
    :param delay: The delay parameter is a number that represents the amount of time (in seconds) that
    the program should pause before printing the board. This can be useful for creating animations or
    for slowing down the output so that it is easier to follow
    """
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

# The `shapes` dictionary contains the shapes of the different types of blocks that can appear in the
# game. Each key in the dictionary represents a different block shape, and the value associated with
# each key is a tuple containing two elements: the first element is a string representing the shape of
# the block, and the second element is a tuple containing the dimensions of the block (width and
# height).
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
        # This is the constructor method for the `block` class. It initializes the attributes of a
        # block object, including its direction, name, shape, serial number, falling status, row and
        # column position pointers, height, and width. The `self.direction` attribute is set to `'up'`
        # by default, indicating that the block is initially facing upwards. The `self.name` attribute
        # is randomly chosen from the keys of the `shapes` dictionary, which contains the different
        # block shapes. The `self.shape` attribute is set to the shape of the block corresponding to
        # its name. The `self.serial_num` attribute is set to the serial number of the block, which is
        # used to distinguish it from other blocks on the board. The `self.falling` attribute is set
        # to `True` by default, indicating that the block is initially falling. The
        # `self.row_position_ptr` and `self.column_position_ptr` attributes are set to the starting
        # row and column positions of the block, respectively. The `self.height` and `self.width`
        # attributes are set to the dimensions of the block's shape.
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
        """
        This function changes the shape, width, and height of an object based on a new shape dictionary.
        
        :param new_shape: The parameter `new_shape` is a dictionary that maps a string key to a tuple
        value. The string key represents the name of a shape, and the tuple value contains two elements:
        a string representing the shape itself, and a tuple of two integers representing the width and
        height of the shape. The
        :type new_shape: dict[str, tuple[str, tuple[int, int]]]
        """
        self.shape = new_shape[self.name][0]
        self.width = new_shape[self.name][1][0]
        self.height = new_shape[self.name][1][1]
    
    def insert_into_board(self, board: list[list], delay):
        """
        This function inserts a shape into a board and prints the updated board with a delay.
        
        :param board: a 2D list representing the game board where each element is a tuple containing a
        character (either a block or empty space) and a serial number (unique identifier for each block)
        :type board: list[list]
        :param delay: The delay parameter is a variable that determines the time delay between each step
        of the game. It is used to control the speed of the game and make it more playable for the user
        """
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
        """
        This function removes a shape from a game board by setting the corresponding cells to blank.
        
        :param board: a 2D list representing the game board, where each element is a tuple containing a
        character representing the block type and an integer representing the block's color
        :type board: list[list]
        """
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
        """
        This function rotates a shape to the right on a game board.
        
        :param board: a 2D list representing the game board where the tetromino will be placed and moved
        on
        :type board: list[list]
        """
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
        """
        This function rotates a Tetris piece to the left and updates its position on the game board.
        
        :param board: A 2D list representing the game board where the tetromino will be placed
        :type board: list[list]
        """
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
        """
        This function moves a block down on a game board if it is able to fall.
        
        :param board: A 2D list representing the game board where the tetromino is currently placed.
        Each element in the list represents a cell on the board and can have a value of 0 or 1, where 0
        represents an empty cell and 1 represents a filled cell
        :type board: list[list]
        """
        self.remove_from_board(board)
        if self.row_position_ptr + self.height < BOARD_HEIGHT:
            self.falling = self.is_able_to_fall(board)
        if self.falling:
            self.row_position_ptr += 1
        self.insert_into_board(board, NO_DELAY)
    
    def move_left(self, board: list[list]):
        """
        This function moves an object to the left on a board if it is able to, and updates the board
        accordingly.
        
        :param board: A 2D list representing the game board, where each element is a tuple containing
        information about a block on the board (e.g. its color and serial number)
        :type board: list[list]
        """
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
        """
        This function moves a block to the right on a board if it is able to move without colliding with
        other blocks.
        
        :param board: A 2D list representing the game board, where each element is a tuple containing
        information about the cell (e.g. whether it is occupied by a block and which block it belongs
        to)
        :type board: list[list]
        """
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
        """
        This function checks if a block can fall down on a given board without colliding with any other
        blocks.
        
        :param board: A 2D list representing the game board, where each element is a tuple containing
        information about the block at that position. The first element of the tuple represents the type
        of block (e.g. "I", "J", "L", etc.), and the second element represents the height of the
        :type board: list[list]
        :return: The function `is_able_to_fall` returns a boolean value indicating whether or not the
        current piece can fall further down the board without colliding with any other pieces.
        """
        if self.row_position_ptr + self.height + 1 > BOARD_HEIGHT:
            return False
        for row_idx in range(self.row_position_ptr, self.row_position_ptr + self.height):
            for col_idx in range(self.column_position_ptr, self.column_position_ptr + self.width):
                if board[row_idx][col_idx][1] > board[row_idx + 1][col_idx][1] and board[row_idx + 1][col_idx][1] != 0:
                    return False
        return True
