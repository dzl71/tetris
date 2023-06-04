import blocks as blk
import time
import keyboard as kb  # it resolves the problem of the input

BOARD_WIDTH = 10
BOARD_HEIGHT = 20
STARTING_POSITION_PTR = tuple([0, 4])
BLOCK = '[]'
EMPTY = "  "
STANDART_DELAY = 1

def create_board() -> list[list]:
    board = []
    for _ in range(BOARD_HEIGHT):
        row = []
        for tile in range(BOARD_WIDTH):
            row.append((blk.BLANK, 0))
        board.append(row)
    return board



def is_row_full(board: list[list], row: int) -> bool:
    for tile in board[row]:
        if tile == 0:
            return False
    return True

def delete_row(board: list[list], row_num: int):
    for item in board[row_num]:
        item = None

def board_full(board: list[list], current_block_serial_num: int) -> bool:
    for tile in board[0]:
        if 0 < tile[1] < current_block_serial_num:
            return True
    return False

def drop_block(board: list[list], block: blk.block):
    while block.is_able_to_fall(board):
        block.move_down(board)

def main():
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
                
                if kb.is_pressed('w'):
                    block.rotate_left(board)
                
                if kb.is_pressed('s'):
                    block.rotate_right(board)
                
                end_time = time.perf_counter()
                if end_time - start_time >= STANDART_DELAY:
                    break
            if block.is_able_to_fall(board): 
                block.move_down(board)
        block_num += 1      

main()
