import blocks as blk
import time
import keyboard as kb

BOARD_WIDTH = 10
BOARD_HEIGHT = 20
STARTING_POSITION_PTR = tuple([0, 4])
BLOCK = '[]'
EMPTY = "  "
STANDART_DELAY = 1

def create_board() -> list[list]:
    """
    The function creates a two-dimensional list representing a game board with blank tiles and zero
    values.
    :return: The function `create_board()` returns a 2D list (list of lists) representing the game
    board. Each element of the list is a tuple containing a string representing the color of the block
    and an integer representing the block's rotation. The size of the board is determined by the
    constants `BOARD_HEIGHT` and `BOARD_WIDTH`.
    """
    board = []
    for _ in range(BOARD_HEIGHT):
        row = []
        for tile in range(BOARD_WIDTH):
            row.append((blk.BLANK, 0))
        board.append(row)
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
    """
    The function deletes a row from a board and then drops the remaining rows down.
    
    :param board: A 2D list representing the game board, where each element is a tuple containing a
    block type and its color
    :type board: list[list]
    :param row_num: The row number of the board that needs to be deleted
    :type row_num: int
    """
    for tile_idx in range(BOARD_WIDTH):
        board[row_num][tile_idx] = (blk.BLANK, 0)
    drop_rows(board, row_num)

def drop_rows(board: list[list], drop_to_row: int):
    """
    The function drops rows in a board by shifting the rows above the specified row downwards.
    
    :param board: The board parameter is a 2-dimensional list that represents the game board. Each
    element in the list represents a row on the board, and each row is itself a list of elements
    representing the tiles in that row
    :type board: list[list]
    :param drop_to_row: The parameter `drop_to_row` is an integer that represents the row number to
    which the rows of the board will be dropped. The function will move all the rows above this row down
    by one position and replace the contents of the row at `drop_to_row` with the contents of the row
    above
    :type drop_to_row: int
    """
    while drop_to_row > 0:
        for tile_idx in range(BOARD_WIDTH):
            board[drop_to_row][tile_idx] = board[drop_to_row - 1][tile_idx]
        drop_to_row -= 1

def board_full(board: list[list], current_block_serial_num: int) -> bool:
    """
    The function checks if the board is full by iterating through the first row of the board and
    checking if any tile has a non-zero value in the second index and a value less than the current
    block serial number.
    
    :param board: A 2D list representing the game board. Each element in the list is a tuple
    representing a tile on the board. The first element of the tuple is the value of the tile (0 if it
    is empty, otherwise the serial number of the block occupying the tile), and the second element is
    :type board: list[list]
    :param current_block_serial_num: The current_block_serial_num parameter is an integer representing
    the serial number of the current block being played on the board
    :type current_block_serial_num: int
    :return: a boolean value indicating whether the board is full or not. If there is any tile in the
    first row of the board that has a non-zero value in the second index and is less than the current
    block serial number, the function returns True, indicating that the board is full. Otherwise, it
    returns False, indicating that the board is not full.
    """
    for tile in board[0]:
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
    This function runs a game loop where it creates a board, generates blocks, and allows the player to
    move and rotate the blocks until they reach the bottom or fill up the board.
    """
    board = create_board()
    block_num = 1
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
                if end_time - start_time >= STANDART_DELAY:
                    break
            if block.is_able_to_fall(board): 
                block.move_down(board)
        for row in range(block.row_position_ptr, BOARD_HEIGHT):
            if row_is_full(board, row):
                delete_row(board, row)
        block_num += 1

main()
