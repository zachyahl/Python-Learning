import sys

chessBoard = {'1h': 'bking', '6c': 'wqueen', '2g': \
            'bbishop', '5h': 'bqueen', '3e': 'wking'}

validPositions = {'1a': 0, '1b': 0, '1c': 0, '1d': 0, '1e': 0, '1f': 0, '1g': 0, '1h': 0, \
                            '2a': 0, '2b': 0, '2c': 0, '2d': 0, '2e': 0, '2f': 0, '2g': 0, '2h': 0,\
                            '3a': 0, '3b': 0, '3c': 0, '3d': 0, '3e': 0, '3f': 0, '3g': 0, '3h': 0, \
                            '4a': 0, '4b': 0, '4c': 0, '4d': 0, '4e': 0, '4f': 0, '4g': 0, '4h': 0, \
                            '5a': 0, '5b': 0, '5c': 0, '5d': 0, '5e': 0, '5f': 0, '5g': 0, '5h': 0, \
                            '6a': 0, '6b': 0, '6c': 0, '6d': 0, '6e': 0, '6f': 0, '6g': 0, '6h': 0, \
                            '7a': 0, '7b': 0, '7c': 0, '7d': 0, '7e': 0, '7f': 0, '7g': 0, '7h': 0, \
                            '8a': 0, '8b': 0, '8c': 0, '8d': 0, '8e': 0, '8f': 0, '8g': 0, '8h': 0,}

validPieces = ['bking', 'bqueen', 'brook', 'bknight', 'bbishop', 'bpawn', 'wking', 'wqueen', 'wrook', 'wknight', 'wbishop', 'wpawn']

def isValidChessBoard(board):
    chessList = list(board.values())
    listCount = 0
    listCount2 = 0
    if len(board) <= 32:
        for x in board:
            listCount = (listCount + 1)
            if listCount <= len(board):
                if x in validPositions:
                    continue
                else:
                    print('Board is not valid')
                    sys.exit()
                
                break
            else:
                break

        for y in board.values():
            listCount2 = (listCount2 + 1)
            if listCount <= len(board):
                if y in validPieces:
                    if chessList.count('bking') > 1:
                        print('Too many Black Kings')
                        sys.exit()

                    elif chessList.count('wking') > 1:
                        print('Too many White Kings')
                        sys.exit()
                    
                    elif chessList.count('bqueen') > 1:
                        print('Too many Black Queens')
                        sys.exit()
                    
                    elif chessList.count('wqueen') > 1:
                        print('Too many White Queens')
                        sys.exit()

                    elif chessList.count('bbishop') > 2:
                        print('Too many Black Bishops')
                        sys.exit()

                    elif chessList.count('wbishop') > 2:
                        print('Too many White Bishops')
                        sys.exit()

                    elif chessList.count('brook') > 2:
                        print('Too many Black Rooks')
                        sys.exit()

                    elif chessList.count('wrook') > 2:
                        print('Too many White Rooks')
                        sys.exit()

                    elif chessList.count('bknight') > 2:
                        print('Too many Black Knights')
                        sys.exit()

                    elif chessList.count('wknight') > 2:
                        print('Too many White Knights')
                        sys.exit()

                    elif chessList.count('bpawn') > 8:
                        print('Too many Black Pawns')
                        sys.exit()         

                    elif chessList.count('wpawn') > 8:
                        print('Too many Black Pawns')
                        sys.exit()

                    continue
                else:
                    print('Board is not valid.')
                    sys.exit()
                break
            else:
                break
        print('Board is valid')
        sys.exit()
    else:
        print('Board is not valid. Too many pieces.')

isValidChessBoard(chessBoard)