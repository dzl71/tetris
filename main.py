import blocks as blk
import time
import keyboard as kb  # it resolves the problem of the input

BOARD_WIDTH = 10
BOARD_HEIGHT = 20
STARTING_POSITION_PTR = 4

def create_board() -> list[list]:
    board = []
    for _ in range(BOARD_HEIGHT):
        row = []
        for tile in range(BOARD_HEIGHT):
            row.append(None)
        board.append(row)
    return board

def print_board(board: list[list]):
    for row in board:
        for tile in row:
            if tile == None:
                print("  ", end='')
            else:
                print(tile, end='')
        print()

def insert_block_to_board(board: list[list], block: blk.block, position_ptr: int):
    pass

def is_row_full(board: list[list], row: int) -> bool:
    for tile in board[row]:
        if tile == None:
            return False
    return True

def delete_row(board: list[list], row_num: int):
    for item in board[row_num]:
        item = None

def board_full(board: list[list]) -> bool:
    return False

def main():
    board = create_board()
    while not board_full(board):
        block = blk.block()
        position_ptr = STARTING_POSITION_PTR
        insert_block_to_board(board, block, position_ptr)
        
        while block.falling:
            
            #insert the checker if able to fall and change the block state
            
            if kb.is_pressed('d'):
                block.move_right()
                insert_block_to_board(board, block, position_ptr)
                
            if kb.is_pressed('a'):
                block.move_left()
                insert_block_to_board(board, block, position_ptr)
                
            if kb.is_pressed('s'):
                block.fall()
                insert_block_to_board(board, block, position_ptr)
               
            if kb.is_pressed('k'):
                block.rotate_left()
                insert_block_to_board(board, block, position_ptr)
               
            if kb.is_pressed('l'):
                block.rotate_right()
                insert_block_to_board(board, block, position_ptr)
                
            time.sleep(1)
            block.move_down()
            position_ptr += 1
            


main()
