import blocks as blk
import time
import keyboard as kb  # it resolves the problem of the input

BOARD_WIDTH = 10
BOARD_HEIGHT = 20
STARTING_POSITION_PTR = tuple([0, 4])
BLOCK = '[]'
EMPTY = "  "

def create_board() -> list[list]:
    board = []
    for _ in range(BOARD_HEIGHT):
        row = []
        for tile in range(BOARD_WIDTH):
            row.append(blk.BLANK)
        board.append(row)
    return board

def print_board(board: list[list]):
    print((BOARD_WIDTH  + 1 ) * '--')
    for row in board:
        print('|', end='')
        for tile in row:
            if tile == blk.BLANK:
                print(EMPTY, end='')
            else:
                print(BLOCK, end='')
        print('|')
    print((BOARD_WIDTH  + 1 ) * '--')
    time.sleep(0.01)

def is_row_full(board: list[list], row: int) -> bool:
    for tile in board[row]:
        if tile == 0:
            return False
    return True

def delete_row(board: list[list], row_num: int):
    for item in board[row_num]:
        item = None

def board_full(board: list[list]) -> bool:
    return False

def drop_block(board: list[list], block: blk.block):
    pass

def main():
    board = create_board()
    while not board_full(board):
        block = blk.block(STARTING_POSITION_PTR)
        block.insert_into_board(board)
        print_board(board)
        
        while block.falling:
            
            #insert the checker if able to fall and change the block state
            
            start_time = time.perf_counter()
            
            while True:
                if kb.is_pressed('d'):
                    block.move_right(board)
                    print_board(board)
                    
                if kb.is_pressed('a'):
                    block.move_left(board)
                    print_board(board)
                    
                if kb.is_pressed('s'):
                    drop_block(board, block)
                    print_board(board)
                
                if kb.is_pressed('k'):
                    block.rotate_left(board)
                    print_board(board)
                
                if kb.is_pressed('l'):
                    block.rotate_right(board)
                    print_board(board)
                
                end_time = time.perf_counter()
                if end_time - start_time >= 1:
                    break
                
            block.move_down(board)
            print_board(board)
            


main()
