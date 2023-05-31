import random as rnd

BLOCK_CHAR = '[]'
BLANK = "  "

shapes = {
    'I' : 3 * (BLOCK_CHAR + '\n') + BLOCK_CHAR,
    
    'T' : 3 * BLOCK_CHAR + '\n' + BLANK + BLOCK_CHAR,
    
    'Z' : 2 * BLOCK_CHAR + '\n' + BLANK + 2 * BLOCK_CHAR,
    
    'S' : BLANK + 2 * BLOCK_CHAR + '\n' + 2 * BLOCK_CHAR,
    
    'L' : 2 * (BLOCK_CHAR + '\n') + 2 * BLOCK_CHAR,
    
    'J' : 2 * (BLANK + BLOCK_CHAR + '\n') + 2 * BLOCK_CHAR,
    
    'O' : 2 * BLOCK_CHAR + '\n' + 2 * BLOCK_CHAR
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
    def __init__(self) -> None:
        self.falling = True
        self.rotated_right_amount = 0
        self.rotated_left_amount = 0
        self.name = rnd.choice(list(shapes))
        self.shape = shapes[self.name]
        
    def rotate_right(self):
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
    
    def rotate_left(self):
        pass
    
    def move_down(self):
        pass
    
    def fall(self):
        pass
    
    def move_left(self):
        pass

    def move_right(self):
        pass

for item in shapes.values():
        print(item + '\n')
