import random as rnd

BLOCK_CHAR = '[]'
BLANK = "  "

shapes = {
    'I' : [[BLOCK_CHAR, BLANK, BLANK],
            [BLOCK_CHAR, BLANK, BLANK],
            [BLOCK_CHAR, BLANK, BLANK],
            [BLOCK_CHAR, BLANK, BLANK]],
    
    'T' : [[BLOCK_CHAR, BLOCK_CHAR, BLOCK_CHAR],
            [BLOCK_CHAR, BLOCK_CHAR, BLANK],
            [BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK]],
    
    'Z' : [[BLOCK_CHAR, BLOCK_CHAR, BLANK],
            [BLANK, BLOCK_CHAR, BLOCK_CHAR],
            [BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK]],
    
    'S' : [[BLANK, BLOCK_CHAR, BLOCK_CHAR],
            [BLOCK_CHAR, BLOCK_CHAR, BLANK],
            [BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK]],
    
    'L' : [[BLOCK_CHAR, BLANK, BLANK],
            [BLOCK_CHAR, BLANK, BLANK],
            [BLOCK_CHAR, BLOCK_CHAR, BLANK],
            [BLANK, BLANK, BLANK]],
    
    'J' : [[BLANK, BLOCK_CHAR, BLANK],
            [BLANK, BLOCK_CHAR, BLANK],
            [BLOCK_CHAR, BLOCK_CHAR, BLANK],
            [BLANK, BLANK, BLANK]],
    
    'O' : [[BLOCK_CHAR, BLOCK_CHAR, BLANK],
            [BLOCK_CHAR, BLOCK_CHAR, BLANK],
            [BLANK, BLANK, BLANK],
            [BLANK, BLANK, BLANK]]
}

class block:
    def __init__(self) -> None:
        self.falling = True
        self.name = rnd.choice(list(shapes))
        self.shape = shapes[self.name]
        
    def rotate_right(self):
        pass
    
    def rotate_left(self):
        pass
    
    def move_down(self):
        pass
    
    def fall(self):
        pass
