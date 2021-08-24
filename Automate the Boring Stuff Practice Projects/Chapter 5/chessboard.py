# This function checks whether a chess board is valid according to criteria specified in the project prompt
# Example board: {'h2': 'bking', 'h1': 'bpawn', 'c2': 'wqueen', 'g2': 'bbishop', 'h5': 'bqueen', 'e2': 'wking', 'e3': 'wbishop', 'c4': 'bbishop'}
# The algebraic notation in the project prompt is reversed (e.g. '5a'). This program uses regular notation (e.g. 'a5')
#TODO: Rewrite after studying regex. There's likely an easier way to do this
#TODO: Include checking whether 2 pieces are in the same spot

POSSIBLE_X = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
POSSIBLE_Y = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
POSSIBLE_PIECES = ['wpawn', 'wknight', 'wbishop', 'wrook', 'wqueen', 'wking',
                    'bpawn', 'bknight', 'bbishop', 'brook', 'bqueen', 'bking']
MAX_PIECES = 16
MAX_PAWNS = 8

def is_valid_chessboard(board):
    for key in board:
        if len(key) != 2: 
            return False
        if key[0] not in POSSIBLE_X:
            return False
        if key[1] not in POSSIBLE_Y:
            return False
    
    wkings = bkings = wpawns = bpawns = wpieces = bpieces = 0
    for value in board.values():
        if value not in POSSIBLE_PIECES:
            return False
        if value == 'wking':
            wkings += 1
        if value == 'bking':
            bkings += 1
        if value == 'wpawn':
            wpawns += 1
        if value == 'bpawn':
            bpawns += 1
        if value.startswith('w'):
            wpieces += 1
        if value.startswith('b'):
            bpieces += 1
    if wkings != 1 or bkings != 1:
        return False
    if wpawns > MAX_PAWNS or bpawns > MAX_PAWNS:
        return False
    if wpieces > MAX_PIECES or bpieces > MAX_PIECES:
        return False

    return True
