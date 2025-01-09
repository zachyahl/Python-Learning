import sys
# Declare initial dictionary
chessBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

def isValidChessBoard(board):
    # chessBoardList = list(chessBoard.keys())
    if len(board) > 32:
        print('Invalid list. Too many pieces')
    
    else:
        validPositions = {'1a': 0, '1b': 0, '1c': 0, '1d': 0, '1e': 0, '1f': 0, '1g': 0, '1h': 0, \
                            '2a': 0, '2b': 0, '2c': 0, '2d': 0, '2e': 0, '2f': 0, '2g': 0, '2h': 0,\
                            '3a': 0, '3b': 0, '3c': 0, '3d': 0, '3e': 0, '3f': 0, '3g': 0, '3h': 0, \
                            '4a': 0, '4b': 0, '4c': 0, '4d': 0, '4e': 0, '4f': 0, '4g': 0, '4h': 0, \
                            '5a': 0, '5b': 0, '5c': 0, '5d': 0, '5e': 0, '5f': 0, '5g': 0, '5h': 0, \
                            '6a': 0, '6b': 0, '6c': 0, '6d': 0, '6e': 0, '6f': 0, '6g': 0, '6h': 0, \
                            '7a': 0, '7b': 0, '7c': 0, '7d': 0, '7e': 0, '7f': 0, '7g': 0, '7h': 0, \
                            '8a': 0, '8b': 0, '8c': 0, '8d': 0, '8e': 0, '8f': 0, '8g': 0, '8h': 0,}

        validPieces = ['bking', 'bqueen', 'brook', 'bknight', 'bbishop', 'bpawn', 'wking', 'wqueen', 'wrook', 'wknight', 'wbishop', 'wpawn']
        while len(board) < 32:
            for x in board:
                if x in validPositions:
                    continue

                else:
                    print('Board is not valid.')
                    sys.exit()
            
            for y in board.values():
                if y in validPieces:
                    continue
                else:
                    print('Board is not valid')
                    sys.exit()
        else:
            sys.exit()
            
        print('skr skr')

isValidChessBoard(chessBoard)


# Potential Steps
# check to see if it has more than unique 32 keys
# 1 - check to see if dictionary has more than 16 pcs that start with 'w'
# 2 - check to see if dictionary has more than 16 pcs that start with 'b'
# 3 - build a grid
    # use for loop in for loop to build 8 rows and 8 columns

# Exercise Directions
# each board will have exactly one white king and one black king
# each player has 16 pcs max and 8 pawns max
# all pieces must be on a valid space from '1a' to '8h'
# all piece names begin with 'w' or 'b' to represent white or black
    # followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'
# Return True or False based on whether it is a valid board
