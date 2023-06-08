import blocks as blk
import time
import keyboard as kb

BOARD_WIDTH = 10
BOARD_HEIGHT = 20
STARTING_POSITION_PTR = tuple([0, 4])
BLOCK = '[]'
EMPTY = "  "

TETRIS = 800
TRIPLE_LINE = 500
DOUBLE_LINE = 300
ONE_LINE = 100

STARTING_BLOCK_SPEED = 1 # in seconds

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
    #         row.append((blk.BLANK, 0))
    #     board.append(row)
    board = [[(blk.BLANK, 0)] * 10 for _ in range(20)]

    return board


def row_is_full(board: list[list], row: int) -> bool:
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
    for tile in board[row]:
        if tile[1] == 0:
            return False
    return True

def row_not_empty(board: list[list[tuple[str, int]]], row_num) -> bool:
    for tile in board[row_num]:
        if tile[1] != 0:
            return True
    return False

def delete_row(board: list[list], row_num: int):
    # `board[row_num] = board[0]` is replacing the row at index `row_num` with the first row of the
    # board. This is because when a row is deleted, the rows above it need to be shifted down, and the
    # top row needs to be replaced with a new empty row.
    board[row_num] = board[0]
    while row_num > 1 and row_not_empty(board, row_num - 1):
        board[row_num] = board[row_num - 1]
        row_num -= 1


def board_full(board: list[list], current_block_serial_num: int) -> bool:
    """
    The function checks if the board is full by iterating through the tiles of the current block and
    returning True if any of them have a non-zero value less than the current block's serial number.
    
    :param board: A 2D list representing the game board. Each element in the list is a list representing
    a row on the board. Each element in the row list is a tuple representing a tile on the board. The
    first element of the tuple is the value of the tile (0 if empty, 1
    :type board: list[list]
    :param current_block_serial_num: The current_block_serial_num parameter is an integer representing
    the serial number of the current block being played on the board
    :type current_block_serial_num: int
    :return: a boolean value indicating whether the game board is full or not. If there is any tile in
    the second row of the board that has a non-zero value in the second element of its tuple and that
    value is less than the current block serial number, the function returns True. Otherwise, it returns
    False.
    """
    for tile in board[1]:
        if 0 < tile[1] < current_block_serial_num:
            return True
    return False

def drop_block(board: list[list], block: blk.block):
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
    :type block: blk.block
    """
    while block.is_able_to_fall(board):
        block.move_down(board)

def main():
    """
    This function runs a Tetris game, where the player controls falling blocks using keyboard inputs and
    earns points for completing lines.
    """
    board = create_board()
    block_num = 1
    fall_delay = STARTING_BLOCK_SPEED
    while True:
        block = blk.block(STARTING_POSITION_PTR, block_num)
        if board_full(board, block_num):
            print("Game Over")
            break
        block.insert_into_board(board, 0)
        
        while block.is_able_to_fall(board):
            start_time = time.perf_counter()
            while True:
                if kb.is_pressed('d'):
                    block.move_right(board)
                    
                if kb.is_pressed('a'):
                    block.move_left(board)
                    
                if kb.is_pressed(' '):
                    drop_block(board, block)
                
                if kb.is_pressed('s'):
                    block.rotate_left(board)
                
                if kb.is_pressed('w'):
                    block.rotate_right(board)
                
                end_time = time.perf_counter()
                if end_time - start_time >= fall_delay:
                    break
            if block.is_able_to_fall(board): 
                block.move_down(board)

        deleted_lines_num = 0
        for row in range(block.row_position_ptr, BOARD_HEIGHT):
            if row_is_full(board, row):
                delete_row(board, row)
                deleted_lines_num += 1
        block_num += 1
        match deleted_lines_num:
            case 1:
                blk.score += ONE_LINE
            case 2:
                blk.score += DOUBLE_LINE
            case 3:
                blk.score += TRIPLE_LINE
            case 4:
                blk.score += TETRIS
            case _: 
                blk.score += 0
        if blk.score > 10_000:
            fall_delay *= 0.7
        elif blk.score > 80_000:
            fall_delay *= 0.5
        elif blk.score > 175_000:
            fall_delay *= 0.5
        elif blk.score > 500_000:
            fall_delay *= 0.5
        elif blk.score > 1_500_000:
            fall_delay *= 0.01

print("ours game refresh rate is very high.\nSo if you have epilepsy, or you are sensetive to bright colors and blinking colors,\nplease don't play")
play = input("continue (insert Y to continue)?\n...> ")

if play == 'Y':
    main()
