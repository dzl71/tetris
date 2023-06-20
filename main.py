import blocks as blk
import time
import keyboard as kb

BOARD_WIDTH = 10
BOARD_HEIGHT = 20
STARTING_POSITION_PTR = tuple([0, 4])
BLOCK = '[]'
EMPTY = "  "
CLEAR_TERMINAL = "clear"

TETRIS = 800
TRIPLE_LINE = 500
DOUBLE_LINE = 300
ONE_LINE = 100

EMPTY_ROW = [(blk.BLANK, 0)] * BOARD_WIDTH

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

def delete_row(board: list[list], row_num: int):
    # `board[row_num] = board[0]` is replacing the row at index `row_num` with the first row of the
    # board. This is because when a row is deleted, the rows above it need to be shifted down, and the
    # top row needs to be replaced with a new empty row.
    board[row_num] = EMPTY_ROW
    while row_num > 0 :
        board[row_num] = board[row_num - 1]
        board[row_num - 1] = EMPTY_ROW
        row_num -= 1

def movement(block: blk.block, board: list[list], fall_delay: float):
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

def movement_logic(block: blk.block, board: list[list], fall_delay: float):
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
    block = blk.block(STARTING_POSITION_PTR, block_num)
    while board[block.row_position_ptr + block.height] == EMPTY_ROW:
        block.insert_into_board(board, 0, True)
    
        movement_logic(block, board, fall_delay)

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
        block = blk.block(STARTING_POSITION_PTR, block_num)

print("ours game refresh rate is very high.\nSo if you have epilepsy, or you are sensetive to bright colors and blinking colors,\nplease don't play")
play = input("continue (insert Y to continue)?\n...> ")

if play == 'Y':
    main()

print('\x1b[31m' + "UNABLE TO CREATE A NEW BLOCK\nGame Over" + blk.colors.WHITE)
