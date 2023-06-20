import time
import keyboard as kb
import random as rnd
import os
import time

BOARD_WIDTH = 10
BOARD_HEIGHT = 20
BLANK = "0"
BLOCK_CHAR = '1'

EMPTY = "  "
CLEAR_TERMINAL = 'cls'

STANDART_INPUT_DELAY = 0.0875
NO_DELAY = 0

EMPTY_TILE_SERIAL_NUM = 0

class colors:
    RED = '\x1b[41m'
    BLUE = '\x1b[44m'
    GREEN = '\x1b[42m'
    PURPLE = '\x1b[45m'
    YELLOW = '\x1b[43m'
    WHITE = '\033[0m'


green_blocks: set[int] = set()
red_blocks: set[int] = set()
blue_blocks: set[int] = set()
purple_blocks: set[int] = set()
yellow_blocks: set[int] = set()

def print_board(board: list[list]):
    """
    This function prints the game board with colored blocks and the current score.
    
    :param board: a 2D list representing the game board
    :type board: list[list]
    :param delay: The delay parameter is the amount of time (in seconds) that the program should wait
    before printing the board
    :param score: The current score of the game
    """
    board_str = ""
    board_str += (BOARD_WIDTH  + 1 ) * '--' + '\n'
    for row in board:
        board_str += '|'
        for tile in row:
            if tile == (BLANK, EMPTY_TILE_SERIAL_NUM):
                board_str += EMPTY
            else:
                if (tile[1] not in green_blocks) and (tile[1] not in red_blocks) and (tile[1] not in blue_blocks):
                  tile_color = tile[1] % 5
                  match tile_color:
                        case 1:
                            green_blocks.add(tile[1])
                        case 2:
                            red_blocks.add(tile[1])
                        case 0:
                            blue_blocks.add(tile[1])
                        case 3:
                            purple_blocks.add(tile[1])
                        case 4:
                            yellow_blocks.add(tile[1])
                if tile[1] in green_blocks:
                    board_str += colors.GREEN + EMPTY + colors.WHITE
                elif tile[1] in blue_blocks:
                    board_str += colors.BLUE + EMPTY + colors.WHITE
                elif tile[1] in yellow_blocks:
                    board_str += colors.YELLOW + EMPTY + colors.WHITE
                elif tile[1] in purple_blocks:
                    board_str += colors.PURPLE + EMPTY + colors.WHITE
                else:
                    board_str += colors.RED + EMPTY + colors.WHITE
        board_str += '|\n'
    board_str += (BOARD_WIDTH  + 1 ) * '--' + '\n'
    print(board_str)

# The `shapes_up` dictionary contains the shapes_up of the different types of blocks that can appear in the
# game. Each key in the dictionary represents a different block shape, and the value associated with
# each key is a tuple containing two elements: the first element is a string representing the shape of
# the block, and the second element is a tuple containing the dimensions of the block (width and
# height).
shapes_up = {
    'I' : (3 * (BLOCK_CHAR + '\n') + BLOCK_CHAR, (1, 4)),
    
    'T' : (3 * BLOCK_CHAR + '\n' + BLANK + BLOCK_CHAR, (3, 2)),
    
    'Z' : (2 * BLOCK_CHAR + '\n' + BLANK + 2 * BLOCK_CHAR, (3, 2)),
    
    'S' : (BLANK + 2 * BLOCK_CHAR + '\n' + 2 * BLOCK_CHAR, (3, 2)),
    
    'L' : (2 * (BLOCK_CHAR + '\n') + 2 * BLOCK_CHAR, (2, 3)),
    
    'J' : (2 * (BLANK + BLOCK_CHAR + '\n') + 2 * BLOCK_CHAR, (2, 3)),
    
    'O' : (2 * BLOCK_CHAR + '\n' + 2 * BLOCK_CHAR, (2, 2))
}

shapes_right = {
    'I' : (4 * BLOCK_CHAR, (4, 1)),
    
    'T' : (BLANK + BLOCK_CHAR + '\n' + 2 * BLOCK_CHAR + '\n' + BLANK + BLOCK_CHAR, (2, 3)),
    
    'Z' : (BLANK + BLOCK_CHAR + '\n' + 2 * BLOCK_CHAR + '\n' + BLOCK_CHAR, (2, 3)),
    
    'S' : (BLOCK_CHAR + BLANK +  '\n' + 2 * BLOCK_CHAR + '\n' + BLANK + BLOCK_CHAR, (2, 3)),
    
    'L' : (3 * BLOCK_CHAR + '\n' + BLOCK_CHAR, (3, 2)),
    
    'J' : (BLOCK_CHAR + '\n' + 3 * BLOCK_CHAR, (3, 2)),
    
    'O' : (2 * BLOCK_CHAR + '\n' + 2 * BLOCK_CHAR, (2, 2))
}

shapes_left = {
    'I' : (4 * BLOCK_CHAR, (4, 1)),
    
    'T' : (BLOCK_CHAR + BLANK + '\n' + 2 * BLOCK_CHAR + '\n' + BLOCK_CHAR + BLANK, (2, 3)),
    
    'Z' : (BLANK + BLOCK_CHAR + '\n' + 2 * BLOCK_CHAR + '\n' + BLOCK_CHAR, (2, 3)),
    
    'S' : (BLOCK_CHAR + BLANK +  '\n' + 2 * BLOCK_CHAR + '\n' + BLANK + BLOCK_CHAR, (2, 3)),
    
    'L' : (2 * BLANK + BLOCK_CHAR + '\n' + 3 * BLOCK_CHAR, (3, 2)),
    
    'J' : (3 * BLOCK_CHAR + '\n' + 2 * BLANK + BLOCK_CHAR, (3, 2)),
    
    'O' : (2 * BLOCK_CHAR + '\n' + 2 * BLOCK_CHAR, (2, 2))
}

shapes_down =  {
    'I' : (3 * (BLOCK_CHAR + '\n') + BLOCK_CHAR, (1, 4)),
    
    'T' : (BLANK + BLOCK_CHAR + '\n' + 3 * BLOCK_CHAR, (3, 2)),
    
    'Z' : (2 * BLOCK_CHAR + '\n' + BLANK + 2 * BLOCK_CHAR, (3, 2)),
    
    'S' : (BLANK + 2 * BLOCK_CHAR + '\n' + 2 * BLOCK_CHAR, (3, 2)),
    
    'L' : (2 * BLOCK_CHAR + '\n' + 2 * (BLANK + BLOCK_CHAR + '\n'), (2, 3)),
    
    'J' : (2 * BLOCK_CHAR + '\n' + 2 * (BLOCK_CHAR + '\n'), (2, 3)),
    
    'O' : (2 * BLOCK_CHAR + '\n' + 2 * BLOCK_CHAR, (2, 2))
}

class Block:
    def __init__(self, starting_ptr: tuple[int, int], serial_num: int) -> None:
        # This is the constructor method for the `block` class. It initializes the attributes of a
        # block object, including its direction, name, shape, serial number, falling status, row and
        # column position pointers, height, and width. The `self.direction` attribute is set to `'up'`
        # by default, indicating that the block is initially facing upwards. The `self.name` attribute
        # is randomly chosen from the keys of the `shapes_up` dictionary, which contains the different
        # block shapes_up. The `self.shape` attribute is set to the shape of the block corresponding to
        # its name. The `self.serial_num` attribute is set to the serial number of the block, which is
        # used to distinguish it from other blocks on the board. The `self.falling` attribute is set
        # to `True` by default, indicating that the block is initially falling. The
        # `self.row_position_ptr` and `self.column_position_ptr` attributes are set to the starting
        # row and column positions of the block, respectively. The `self.height` and `self.width`
        # attributes are set to the dimensions of the block's shape.
        self.direction: str = 'up'
        
        self.name = rnd.choice(list(shapes_up))
        self.shape = shapes_up[self.name][0]
        self.serial_num = serial_num
                
        self.row_position_ptr = starting_ptr[0]
        self.height = shapes_up[self.name][1][1]
        
        self.column_position_ptr = starting_ptr[1]
        self.width = shapes_up[self.name][1][0]
    
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
    
    def insert_into_board(self, board: list[list], delay, to_print: bool):
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

        row_seperated = self.shape.split("\n")
        for row in row_seperated:
            for tile in row:
                if tile == BLOCK_CHAR:
                    board[row_num][col_num] = (BLOCK_CHAR, self.serial_num)
                col_num += 1
            col_num = self.column_position_ptr
            row_num += 1
        if to_print:
            os.system(CLEAR_TERMINAL)
            print_board(board)
            time.sleep(delay)


            
    def remove_from_board(self, board: list[list]):
        """
        This function removes a shape from a game board by setting the corresponding cells to blank.
        
        :param board: a 2D list representing the game board, where each element is a tuple containing a
        character representing the block type and an integer representing the block's color
        :type board: list[list]
        """
        for row_num in range(BOARD_HEIGHT):
            for tile_num in range(BOARD_WIDTH):
                if board[row_num][tile_num][1] == self.serial_num:
                    board[row_num][tile_num] = (BLANK, EMPTY_TILE_SERIAL_NUM)

    def rotate_right(self, board: list[list]):
        """
        This function rotates the current shape to the right and updates its direction accordingly.
        
        :param board: The board parameter is a 2D list that represents the game board. Each element in
        the list represents a cell on the board, and can contain either a block or an empty space. The
        rotate_right method is used to rotate the current shape to the right on the board
        :type board: list[list]
        """
        self.remove_from_board(board)
        match self.direction:
            case 'up':
                self.change_shape(shapes_right)
                if self.is_able_to_go_right(board):
                    self.direction = 'right'
                else:
                    self.change_shape(shapes_up)
            case 'right': 
                self.change_shape(shapes_down)
                if self.is_able_to_go_right(board) and self.is_able_to_fall(board):
                    self.direction = 'down'
                else:
                    self.change_shape(shapes_right)
            case 'down':
                self.change_shape(shapes_left)
                if self.is_able_to_go_right(board):
                    self.direction = 'left'
                else:
                    self.change_shape(shapes_down)
            case 'left':
                self.change_shape(shapes_up)
                if self.is_able_to_go_right(board) and self.is_able_to_fall(board):
                    self.direction = 'up'
                else:
                    self.change_shape(shapes_left)
        self.insert_into_board(board, STANDART_INPUT_DELAY, True)
    
    def rotate_left(self, board: list[list]):
        """
        This function rotates the current shape left and updates its direction accordingly.
        
        :param board: The "board" parameter is a 2D list that represents the game board. Each element in
        the list represents a cell on the board, and can contain a value indicating the presence of a
        game piece or be empty. The "rotate_left" method is a function that rotates the current game
        piece
        :type board: list[list]
        """
        self.remove_from_board(board)
        match self.direction:
            case 'up':
                self.change_shape(shapes_left)
                if self.is_able_to_go_right(board):
                    self.direction = 'left'
                else:
                    self.change_shape(shapes_up)
            case 'left': 
                self.change_shape(shapes_down)
                if self.is_able_to_go_right(board) and self.is_able_to_fall(board):
                    self.direction = 'down'
                else:
                    self.change_shape(shapes_left)
            case 'down':
                self.change_shape(shapes_right)
                if self.is_able_to_go_right(board):
                    self.direction = 'right'
                else:
                    self.change_shape(shapes_down)
            case 'right':
                self.change_shape(shapes_up)
                if self.is_able_to_go_right(board) and self.is_able_to_fall(board):
                    self.direction = 'up'
                else:
                    self.change_shape(shapes_right)
        self.insert_into_board(board, STANDART_INPUT_DELAY, True)
    
    def move_down(self, board: list[list], to_print: bool):
        """
        This function moves a block down on a game board if it is able to fall.
        
        :param board: A 2D list representing the game board where the tetromino is currently placed.
        Each element in the list represents a cell on the board and can have a value of 0 or 1, where 0
        represents an empty cell and 1 represents a filled cell
        :type board: list[list]
        """
        self.remove_from_board(board)
        if self.is_able_to_fall(board):
            self.row_position_ptr += 1
        self.insert_into_board(board, NO_DELAY, to_print)
    
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
                if EMPTY_TILE_SERIAL_NUM < board[row_idx][self.column_position_ptr - 1][1] < self.serial_num:
                    able_to_go_left = False
        else:
            able_to_go_left = False
        if able_to_go_left:
            self.column_position_ptr -= 1
        self.insert_into_board(board, STANDART_INPUT_DELAY, True)

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
                if EMPTY_TILE_SERIAL_NUM < board[row_idx][self.column_position_ptr + self.width][1] < self.serial_num:
                    able_to_move = False
        else:
            able_to_move = False
        if able_to_move:
            self.column_position_ptr += 1
        self.insert_into_board(board, STANDART_INPUT_DELAY, True)
    
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
        if self.row_position_ptr + self.height >= BOARD_HEIGHT:
            return False
        for row_idx in range(self.row_position_ptr, self.row_position_ptr + self.height):
            for col_idx in range(self.column_position_ptr, self.column_position_ptr + self.width):
                if EMPTY_TILE_SERIAL_NUM < board[row_idx + 1][col_idx][1] < board[row_idx][col_idx][1]:
                    return False
        return True
    
    def is_able_to_go_right(self, board) -> bool:
        """
        This function checks if a game piece can move to the right on a game board without colliding
        with other pieces.
        
        :param board: a 2D list representing the game board, where each element is a tuple containing
        two values: the first value represents the type of block (e.g. empty, filled, etc.), and the
        second value represents the serial number of the block (if it is filled)
        :return: a boolean value, either True or False.
        """
        if self.width + self.column_position_ptr > BOARD_WIDTH:
            return False
        for row_idx in range(self.row_position_ptr, self.row_position_ptr + self.height):
            for col_idx in range(self.column_position_ptr, self.column_position_ptr + self.width):
                if EMPTY_TILE_SERIAL_NUM < board[row_idx][col_idx][1] < self.serial_num:
                    return False
        return True
    
    def drop_block(self, board: list[list]):
        """
        The function drops a block down on a board until it can no longer fall.
        
        :param board: A 2D list representing the game board where the block will be dropped. Each element in
        the list represents a cell on the board and can contain a value indicating the state of the cell
        (e.g. empty, filled with a block, etc.)
        :type board: list[list]
        :param block: The "block" parameter is an instance of a custom-defined class called "block". This
        class likely represents a block or shape in a game or puzzle, and has methods for moving and
        checking its position on a game board. The "drop_block" function takes in a game board represented
        as a
        :type block: block
        """
        while self.is_able_to_fall(board):
            self.move_down(board, False)
        self.insert_into_board(board, STANDART_INPUT_DELAY, True)
        

STARTING_POSITION_PTR = tuple([0, 4])

TETRIS = 800
TRIPLE_LINE = 500
DOUBLE_LINE = 300
ONE_LINE = 100

EMPTY_ROW = [(BLANK, 0)] * BOARD_WIDTH

STARTING_BLOCK_SPEED = 1.5 # in seconds

def create_board() -> list[list]:
    """
    The function creates a two-dimensional list representing a game board with blank tiles and zero
    values.
    :return: The function `create_board()` returns a 2D list (list of lists) representing the game
    board. Each element of the list is a tuple containing a string representing the color of the block
    and an integer representing the block's rotation. The size of the board is determined by the
    constants `BOARD_HEIGHT` and `BOARD_WIDTH`.
    """
    # board = []
    # for _ in range(BOARD_HEIGHT):
    #     row = []
    #     for _ in range(BOARD_WIDTH):
    #         row.append((BLANK, 0))
    #     board.append(row)
    board = [[(BLANK, 0)] * 10 for _ in range(20)]

    return board


def row_is_full(row: list) -> bool:
    """
    The function checks if a given row in a board is completely filled with non-zero tiles.
    
    :param board: A 2D list representing the game board, where each element is a tuple representing a
    tile on the board. The first element of the tuple represents the color of the tile (an integer), and
    the second element represents whether the tile is empty (0) or occupied (1)
    :type board: list[list]
    :param row: The row parameter is an integer representing the index of the row in the board list that
    we want to check if it is full or not
    :type row: int
    :return: a boolean value indicating whether the specified row in the given board is full or not. If
    all the tiles in the row have a non-zero value in their second element, the function returns True,
    otherwise it returns False.
    """
    for tile in row:
        if tile[1] == EMPTY_TILE_SERIAL_NUM:
            return False
    return True

def delete_row(board: list[list], row_num: int) -> None:
    # `board[row_num] = board[0]` is replacing the row at index `row_num` with the first row of the
    # board. This is because when a row is deleted, the rows above it need to be shifted down, and the
    # top row needs to be replaced with a new empty row.
    board[0:row_num + 1] = board[0:row_num]
    board.insert(0, EMPTY_ROW)

def movement(block: Block, board: list[list], fall_delay: float):
    start_time = time.perf_counter()
    while True:
        if kb.is_pressed('d'):
            block.move_right(board)
            
        if kb.is_pressed('a'):
            block.move_left(board)
            
        if kb.is_pressed(' '):
            block.drop_block(board)
        
        if kb.is_pressed('s'):
            block.rotate_left(board)
        
        if kb.is_pressed('w'):
            block.rotate_right(board)
        
        end_time = time.perf_counter()
        if end_time - start_time >= fall_delay:
            break

def movement_logic(block: Block, board: list[list], fall_delay: float):
    while True:
        movement(block, board, fall_delay)
        if not block.is_able_to_fall(board):
            break
        block.move_down(board, True)
    movement(block, board, fall_delay)
    if block.is_able_to_fall(board):
        movement_logic(block, board, fall_delay)

def main():
    """
    This function runs a Tetris game, where the player controls falling blocks using keyboard inputs and
    earns points for completing lines.
    """
    board = create_board()
    block_num = 1
    fall_delay = STARTING_BLOCK_SPEED
    while True:
        block = Block(STARTING_POSITION_PTR, block_num)
        block.insert_into_board(board, 0, True)
    
        movement_logic(block, board, fall_delay)

        for row_idx, row in enumerate(board):
            if row_is_full(row):
                delete_row(board, row_idx) 
                os.system(CLEAR_TERMINAL) 
                print_board(board)
                time.sleep(1)
        if board[block.height] != EMPTY_ROW:
            break
        block_num += 1
        

print("ours game refresh rate is very high.\nSo if you have epilepsy, or you are sensetive to bright colors and blinking colors,\nplease don't play")
play = input("continue (insert Y to continue)?\n...> ")

if play == 'Y':
    main()

print('\x1b[31m' + "UNABLE TO CREATE A NEW BLOCK\nGame Over" + colors.WHITE)
