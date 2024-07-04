"""
This class is responsible for storing all information about the current state of the game. It will also be responsible
for determining the valid moves at the current state and keeping a move log.
"""

class GameState():
    def __init__(self):
        # board is an 8*8 2D list, each element has 2 characters.
        # first character represents color ('b' or 'w').
        # second character represents the piece ('K','Q','B','N','p').
        # Squares with no pieces are represented by --
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
        ]
        self.moveFunctions = {'p': self.getPawnMoves, 'R': self.getRookMoves,
                              'N': self.getKnightMoves, 'B': self.getBishopMoves,
                              'K': self.getKingMoves, 'Q': self.getQueenMoves}
        self.whiteToMove = True
        self.moveLog = []
        self.whiteKingLocation = (7, 4)
        self.blackKingLocation = (0, 4)
        self.inCheck = False
        self.pins = []
        self.checks = []
        self.enpassantPossible = ()  # square where the enpassant capture is possible
        self.enpassantPossibleLog = [self.enpassantPossible]
        self.currentCastlingRight = CastleRights(True, True, True, True)
        self.castleRightsLog = [CastleRights(self.currentCastlingRight.wks, self.currentCastlingRight.bks,
                                             self.currentCastlingRight.wqs, self.currentCastlingRight.bqs)]
        self.checkmate = False
        self.stalemate = False

    def makeMove(self, move):
        """
        Takes a move as parameter and executes it, except for castling, en-passant, pawn promotion
        """
        self.board[move.start_row][move.start_col] = "--"
        self.board[move.end_row][move.end_col] = move.pieceMoved
        self.moveLog.append(move)  # log move for undo/history
        self.whiteToMove = not self.whiteToMove  # swap players

        # update the king's location

        if move.pieceMoved == "wK":
            self.whiteKingLocation = (move.end_row, move.end_col)
        elif move.pieceMoved == "bK":
            self.blackKingLocation = (move.end_row, move.end_col)

        # pawn promotion
        if move.isPawnPromotion:
            self.board[move.end_row][move.end_col] = move.pieceMoved[0] + 'Q'

        # enpassant move
        if move.isEnpassantMove:
            self.board[move.start_row][move.end_col] = "--"  # capturing the pawn

        # update  enpassantPossible square
        if move.pieceMoved[1] == 'p' and abs(move.start_row - move.end_row) == 2:  # only on 2 square pawn advances
            self.enpassantPossible = ((move.start_row + move.end_row)//2, move.start_col)
        else:
            self.enpassantPossible = ()

        # castle move
        if move.isCastleMove:
            if move.end_col - move.start_col == 2:  # king side castle
                self.board[move.end_row][move.end_col - 1] = self.board[move.end_row][move.end_col + 1]
                self.board[move.end_row][move.end_col + 1] = "--"
            else:  # queen side castle
                self.board[move.end_row][move.end_col + 1] = self.board[move.end_row][move.end_col - 2]
                self.board[move.end_row][move.end_col - 2] = "--"

        self.enpassantPossibleLog.append(self.enpassantPossible)

        # update the castling rights whenever the rook or king has to move
        self.updateCastleRights(move)
        self.castleRightsLog.append(CastleRights(self.currentCastlingRight.wks, self.currentCastlingRight.bks,
                                                 self.currentCastlingRight.wqs, self.currentCastlingRight.bqs))

    def undoMove(self):
        """
        Undo the last move made
        """
        if len(self.moveLog) != 0:  # If there is move to undo
            prevMove = self.moveLog.pop()
            self.board[prevMove.start_row][prevMove.start_col] = prevMove.pieceMoved
            self.board[prevMove.end_row][prevMove.end_col] = prevMove.pieceCaptured
            self.whiteToMove = not self.whiteToMove
            # update the king's location if needed
            if prevMove.pieceMoved == "wK":
                self.whiteKingLocation = (prevMove.start_row, prevMove.start_col)
            elif prevMove.pieceMoved == "bK":
                self.blackKingLocation = (prevMove.start_row, prevMove.start_col)

            # undo enpassant move
            if prevMove.isEnpassantMove:
                self.board[prevMove.end_row][prevMove.end_col] = '--'  # leave landing square blank
                self.board[prevMove.start_row][prevMove.end_col] = prevMove.pieceCaptured

            self.enpassantPossibleLog.pop()
            self.enpassantPossible = self.enpassantPossibleLog[-1]

            # undoing the castling rights
            self.castleRightsLog.pop()
            self.currentCastlingRight = self.castleRightsLog[-1]

            # undo the castle move
            if prevMove.isCastleMove:
                if prevMove.end_col - prevMove.start_col == 2:  # King-side castle
                    # Move the rook back
                    self.board[prevMove.end_row][prevMove.end_col + 1] = self.board[prevMove.end_row][
                        prevMove.end_col - 1]
                    self.board[prevMove.end_row][prevMove.end_col - 1] = "--"  # Empty the rook's original position
                    # Move the king back
                    self.board[prevMove.end_row][prevMove.end_col - 1] = self.board[prevMove.end_row][prevMove.end_col]
                    self.board[prevMove.end_row][prevMove.end_col] = "--"  # Empty the king's original position

                else:  # Queen-side castle
                    # Move the rook back
                    self.board[prevMove.end_row][prevMove.end_col - 2] = self.board[prevMove.end_row][
                        prevMove.end_col + 1]
                    self.board[prevMove.end_row][prevMove.end_col + 1] = "--"  # Empty the rook's original position
                    # Move the king back
                    self.board[prevMove.end_row][prevMove.end_col + 1] = self.board[prevMove.end_row][prevMove.end_col]
                    self.board[prevMove.end_row][prevMove.end_col] = "--"  # Empty the king's original position
            self.checkmate = False
            self.stalemate = False

    def updateCastleRights(self, move):
        """
        Update the castle rights given the move
        :param move:
        :return:
        """
        if move.pieceMoved == "wK":
            self.currentCastlingRight.wks = False
            self.currentCastlingRight.wqs = False
        elif move.pieceMoved == "bK":
            self.currentCastlingRight.bks = False
            self.currentCastlingRight.bqs = False
        elif move.pieceMoved == "wR":
            if move.start_row == 7:
                if move.start_col == 0:  # left white rook
                    self.currentCastlingRight.wqs = False
                elif move.start_col == 7:  # right white rook
                    self.currentCastlingRight.wks = False
        elif move.pieceMoved == "bR":
            if move.start_row == 0:
                if move.start_col == 0:  # left rook
                    self.currentCastlingRight.bqs = False
                elif move.start_col == 7:  # right rook
                    self.currentCastlingRight.bks = False

        # if a rook is captured
        if move.pieceCaptured == "wR":
            if move.end_row == 7:
                if move.end_col == 0:
                    self.currentCastlingRight.wqs = False
                elif move.end_col == 7:
                    self.currentCastlingRight.wks = False
        elif move.pieceCaptured == "bR":
            if move.end_row == 0:
                if move.end_col == 0:
                    self.currentCastlingRight.bqs = False
                elif move.end_col == 7:
                    self.currentCastlingRight.bks = False


    def getValidMoves(self):
        """
        All moves considering checks
        """
        '''
        # Naive Algorithm:
        # 1.) generate all the possible moves
        moves = self.getAllPossibleMoves()

        # 2.) for each move, make the move
        for i in range(len(moves)-1, -1, -1):  # when removing from a list, traverse backwards.
            self.makeMove(moves[i])
            # 3.) generate all opponent's move
            # 4.) for each of your opponent's move, see if your king is being attacked
            # steps 3, 4 done in inCheck function.
            self.whiteToMove = not self.whiteToMove
            if self.inCheck():
                moves.remove(moves[i])
            self.whiteToMove = not self.whiteToMove
            self.undoMove()
        # 5.) If it is being attacked, then the move we made is not a valid move

        if len(moves) == 0:  # either checkmate or stalemate
            if self.inCheck():
                self.checkMate = True
            else:
                self.staleMate = True
        else:  # when we undo the checkmate or stalemate, it should work.
            self.checkMate = False
            self.staleMate = False
        return moves
        '''

        # More advanced algorithm
        moves = []
        self.inCheck, self.pins, self.checks = self.checkForPinsAndChecks()
        if self.whiteToMove:
            kingRow = self.whiteKingLocation[0]
            kingCol = self.whiteKingLocation[1]
        else:
            kingRow = self.blackKingLocation[0]
            kingCol = self.blackKingLocation[1]
        if self.inCheck:
            if len(self.checks) == 1:  # only one check, block check or more king
                moves = self.getAllPossibleMoves()
                # to block a check, you must move a piece into one of the squares between king and the attacking piece.
                check = self.checks[0]
                checkRow = check[0]
                checkCol = check[1]
                pieceChecking = self.board[checkRow][checkCol]  # enemy piece causing the check
                validSquares = []  # squares where pieces can move to
                # if knight, then either capture the knight or move the king, pieces can't block the check.
                if pieceChecking[1] == 'N':
                    validSquares = [(checkRow, checkCol)]
                else:
                    for i in range(1, len(self.board)):
                        validSquare = (kingRow + check[2]*i, kingCol + check[3]*i)
                        validSquares.append(validSquare)
                        if validSquare[0] == checkRow and validSquare[1] == checkCol:  # once you get to piece end check
                            break
                # get rid of any moves that don't block the check or move the king
                for i in range(len(moves)-1, -1, -1):
                    if moves[i].pieceMoved[1] != 'K':  # if you don't move the king, block or capture
                        if not (moves[i].end_row, moves[i].end_col) in validSquares:  # move which doesn't block or capture
                            moves.remove(moves[i])
            else:  # double check, king has to move
                self.getKingMoves(kingRow, kingCol, moves)
            if len(moves) == 0:
                self.checkmate = True
            else:
                self.checkmate = False
        else:  # not in check so all the moves are fine
            moves = self.getAllPossibleMoves()
            if len(moves) == 0:
                self.stalemate = True
            else:
                self.stalemate = False

        if self.whiteToMove:
            self.getCastleMoves(self.whiteKingLocation[0], self.whiteKingLocation[1], moves, "w")
        else:
            self.getCastleMoves(self.blackKingLocation[0], self.blackKingLocation[1], moves, "b")
        return moves

    '''
    def inCheck(self):
        """
        Determine if the current player is in check
        """
        if self.whiteToMove:
            return self.squareUnderAttack(self.whiteKingLocation[0], self.whiteKingLocation[1])
        else:
            return self.squareUnderAttack(self.blackKingLocation[0], self.blackKingLocation[1])
    
    '''

    def squareUnderAttack(self, r, c):
        """
        Determine if the enemy can attack the square (r, c).
        """
        self.whiteToMove = not self.whiteToMove  # switch to opponent's turn and check if the king is being attacked.
        oppMoves = self.getAllPossibleMoves()
        self.whiteToMove = not self.whiteToMove
        for move in oppMoves:
            if move.end_row == r and move.end_col == c:
                return True
        return False

    def getAllPossibleMoves(self):
        """
        All moves without considering checks
        """
        moves = []
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0]
                if (turn == 'w' and self.whiteToMove) or (turn == 'b' and not self.whiteToMove):
                    piece = self.board[r][c][1]
                    self.moveFunctions[piece](r, c, moves)
        return moves

    def checkForPinsAndChecks(self):
        """
        Returns if the player is in check, a list of pins and a list of checks
        """
        pins = []
        checks = []
        inCheck = False
        if self.whiteToMove:
            enemyColor = "b"
            allyColor = "w"
            startRow = self.whiteKingLocation[0]
            startCol = self.whiteKingLocation[1]
        else:
            enemyColor = "w"
            allyColor = "b"
            startRow = self.blackKingLocation[0]
            startCol = self.blackKingLocation[1]

        # check outward from king, for pins and check and keep track of pins

        directions = ((-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))
        for j in range(len(directions)):
            d = directions[j]
            possiblePin = ()
            for i in range(1,len(self.board)):
                endRow = startRow + d[0] * i
                endCol = startCol + d[1] * i
                if 0 <= endRow < len(self.board) and 0 <= endCol < len(self.board[0]):
                    endPiece = self.board[endRow][endCol]
                    if endPiece[0] == allyColor and endPiece[1] != 'K':
                        if possiblePin == ():
                            possiblePin = (endRow, endCol, d[0], d[1])
                        else:  # second allied piece so no pin or check possible in this direction
                            break
                    elif endPiece[0] == enemyColor:
                        type = endPiece[1]
                        # 5 conditions arise:
                        # 1.) orthogonally away from the king and the piece is a rook
                        # 2.) diagonally away from the king and the piece is a bishop
                        # 3.) 1 square away diagonally from the king and the piece is a pawn
                        # 4.) any direction and the piece is a queen
                        # 5.) any direction, 1 square away and the piece is a king (king controls that square)
                        if (0 <= j <= 3 and type == 'R') or \
                                (4 <= j <= 7 and type == 'B') or \
                                (i == 1 and type == 'p' and ((enemyColor == 'w' and 6 <= j <= 7) or enemyColor == 'b' and 4 <= j <= 5)) or \
                                (type == 'Q') or (type == 'K' and i == 1):
                            if possiblePin == ():  # no piece is blocking, so check
                                inCheck = True
                                checks.append((endRow, endCol, d[0], d[1]))
                                break
                            else:  # piece is blocking so pin
                                pins.append(possiblePin)
                                break
                        else:  # enemy piece but not check
                            break
                else:  # off board
                    break
        # check for knight checks
        knightMoves = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
        for m in knightMoves:
            endRow = startRow + m[0]
            endCol = startCol + m[1]
            if 0 <= endRow < len(self.board) and 0 <= endCol < len(self.board[0]):
                endPiece = self.board[endRow][endCol]
                if endPiece[0] == enemyColor and endPiece[1] == 'N': # enemy knight piece
                    inCheck = True
                    checks.append((endRow, endCol, m[0], m[1]))
        return inCheck, pins, checks

    def getPawnMoves(self, r, c, moves):
        """
        Get all the pawn moves for the pawn located at row, col and these moves to the list
        """
        piecePinned = False
        pinDirection = ()
        for i in range(len(self.pins)-1, -1, -1):
            if self.pins[i][0] == r and self.pins[i][1] == c:
                piecePinned = True
                pinDirection = (self.pins[i][2], self.pins[i][3])
                self.pins.remove(self.pins[i])
                break

        if self.whiteToMove:  # white pawn move
            kingRow, kingCol = self.whiteKingLocation
            if self.board[r-1][c] == "--":  # 1 sq pawn advance
                if not piecePinned or pinDirection == (-1, 0):
                    moves.append(Move((r, c), (r-1, c), self.board))
                    if r == 6 and self.board[r-2][c] == "--":  # 2 sq pawn advance
                        moves.append(Move((r, c), (r-2, c), self.board))

            # capture left side piece
            if c-1 >= 0:
                if self.board[r-1][c-1] != "--" and self.board[r-1][c-1][0] == "b":  # enemy piece to capture
                    if not piecePinned or pinDirection == (-1, -1):  # capture left
                        moves.append(Move((r, c), (r-1, c-1), self.board))
                elif (r-1, c-1) == self.enpassantPossible:
                    if not piecePinned or pinDirection == (-1, -1):  # capture left
                        attackingPiece = blockingPiece = False
                        if kingRow == r:
                            if kingCol < c:  # king is left of pawn
                                # insideRange: attacking piece bw king and pawn, outside range: bw pawn and border
                                insideRange = range(kingCol + 1, c - 1)
                                outsideRange = range(c + 1, len(self.board[0]))
                            else:  # king is in right of the pawn
                                insideRange = range(kingCol - 1, c, -1)
                                outsideRange = range(c - 2, -1, -1)
                            for i in insideRange:
                                if self.board[r][i] != "--":  # some piece blocking other than enpassant pawns
                                    blockingPiece = True
                            for i in outsideRange:
                                square = self.board[r][i]
                                if square[0] == "b" and (square[1] == "R" or square[1] == "Q"):  # attacking piece
                                    attackingPiece = True
                                elif square != "--":
                                    blockingPiece = True
                        if not attackingPiece or blockingPiece:
                            moves.append(Move((r, c), (r-1, c-1), self.board, isEnpassantMove=True))

            # capture right side piece
            if c+1 < len(self.board[r]):
                if self.board[r-1][c+1] != "--" and self.board[r-1][c+1][0] == "b":  # enemy piece to capture
                    if not piecePinned or pinDirection == (1, -1):  # capture right
                        moves.append(Move((r, c), (r-1, c+1), self.board))
                elif (r-1, c+1) == self.enpassantPossible:
                    if not piecePinned or pinDirection == (1, -1):  # capture left
                        attackingPiece = blockingPiece = False
                        if kingRow == r:
                            if kingCol < c:  # king is left of pawn
                                # insideRange: attacking piece bw king and pawn, outside range: bw pawn and border
                                insideRange = range(kingCol + 1, c)
                                outsideRange = range(c + 2, len(self.board[0]))
                            else:  # king is in right of the pawn
                                insideRange = range(kingCol - 1, c + 1, -1)
                                outsideRange = range(c - 1, -1, -1)
                            for i in insideRange:
                                if self.board[r][i] != "--":  # some piece blocking other than enpassant pawns
                                    blockingPiece = True
                            for i in outsideRange:
                                square = self.board[r][i]
                                if square[0] == "b" and (square[1] == "R" or square[1] == "Q"):  # attacking piece
                                    attackingPiece = True
                                elif square != "--":
                                    blockingPiece = True
                        if not attackingPiece or blockingPiece:
                            moves.append(Move((r, c), (r-1, c+1), self.board, isEnpassantMove=True))

        else:  # black pawn move
            kingRow, kingCol = self.blackKingLocation
            if self.board[r + 1][c] == "--":  # 1 sq pawn advance
                if not piecePinned or pinDirection == (1, 0):
                    moves.append(Move((r, c), (r + 1, c), self.board))
                    if r == 1 and self.board[r + 2][c] == "--":  # 2 sq pawn advance
                        moves.append(Move((r, c), (r + 2, c), self.board))

            # capture left side piece
            if c - 1 >= 0:
                if self.board[r + 1][c - 1] != "--" and self.board[r + 1][c - 1][0] == "w":  # enemy piece to capture
                    if not piecePinned or pinDirection == (-1, 1):
                        moves.append(Move((r, c), (r + 1, c - 1), self.board))
                elif (r+1, c-1) == self.enpassantPossible:
                    if not piecePinned or pinDirection == (-1, 1):
                        attackingPiece = blockingPiece = False
                        if kingRow == r:
                            if kingCol < c:  # king is left of pawn
                                # insideRange: attacking piece bw king and pawn, outside range: bw pawn and border
                                insideRange = range(kingCol + 1, c - 1)
                                outsideRange = range(c + 1, len(self.board[0]))
                            else:  # king is in right of the pawn
                                insideRange = range(kingCol - 1, c, -1)
                                outsideRange = range(c - 2, -1, -1)
                            for i in insideRange:
                                if self.board[r][i] != "--":  # some piece blocking other than enpassant pawns
                                    blockingPiece = True
                            for i in outsideRange:
                                square = self.board[r][i]
                                if square[0] == "w" and (square[1] == "R" or square[1] == "Q"):  # attacking piece
                                    attackingPiece = True
                                elif square != "--":
                                    blockingPiece = True
                        if not attackingPiece or blockingPiece:
                            moves.append(Move((r, c), (r + 1, c - 1), self.board, isEnpassantMove=True))

            # capture right side piece
            if c + 1 < len(self.board[r]):
                if self.board[r + 1][c + 1] != "--" and self.board[r + 1][c + 1][0] == "w":  # enemy piece to capture
                    if not piecePinned or pinDirection == (1, 1):
                        moves.append(Move((r, c), (r + 1, c + 1), self.board))
                elif (r+1, c+1) == self.enpassantPossible:
                    if not piecePinned or pinDirection == (1, 1):
                        attackingPiece = blockingPiece = False
                        if kingRow == r:
                            if kingCol < c:  # king is left of pawn
                                # insideRange: attacking piece bw king and pawn, outside range: bw pawn and border
                                insideRange = range(kingCol + 1, c)
                                outsideRange = range(c + 2, len(self.board[0]))
                            else:  # king is in right of the pawn
                                insideRange = range(kingCol - 1, c + 1, -1)
                                outsideRange = range(c - 1, -1, -1)
                            for i in insideRange:
                                if self.board[r][i] != "--":  # some piece blocking other than enpassant pawns
                                    blockingPiece = True
                            for i in outsideRange:
                                square = self.board[r][i]
                                if square[0] == "w" and (square[1] == "R" or square[1] == "Q"):  # attacking piece
                                    attackingPiece = True
                                elif square != "--":
                                    blockingPiece = True
                        if not attackingPiece or blockingPiece:
                            moves.append(Move((r, c), (r + 1, c + 1), self.board, isEnpassantMove=True))

    def getRookMoves(self, r, c, moves):
        """
        Get all the rook moves for the pawn located at row, col and these moves to the list
        """
        piecePinned = False
        pinDirection = ()
        for i in range(len(self.pins)-1, -1, -1):
            if self.pins[i][0] == r and self.pins[i][1] == c:
                piecePinned = True
                pinDirection = (self.pins[i][2], self.pins[i][3])
                if self.board[r][c][1] != 'Q':  # can't remove queen from pin on rook moves, only remove on bishop moves
                    self.pins.remove(self.pins[i])
                break

        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        enemyColor = "b" if self.whiteToMove else "w"
        for d in directions:
            for i in range(1, len(self.board)):
                endRow = r + d[0]*i
                endCol = c + d[1]*i
                if 0 <= endRow < len(self.board) and 0 <= endCol < len(self.board):  # on board
                    if not piecePinned or pinDirection == d or pinDirection == (-d[0], -d[1]):
                        endPiece = self.board[endRow][endCol]
                        if endPiece == "--":
                            moves.append(Move((r, c), (endRow, endCol), self.board))
                        elif endPiece[0] == enemyColor:
                            moves.append(Move((r, c), (endRow, endCol), self.board))
                            break
                        else:
                            break
                else:  # off board
                    break

    def getKnightMoves(self, r, c, moves):
        """
        Get all the knight moves for the pawn located at row, col and these moves to the list
        """
        piecePinned = False
        for i in range(len(self.pins)-1, -1, -1):
            if self.pins[i][0] == r and self.pins[i][1] == c:
                piecePinned = True
                self.pins.remove(self.pins[i])
                break

        knightMoves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        allyColor = "w" if self.whiteToMove else "b"
        for m in knightMoves:
            endRow = r + m[0]
            endCol = c + m[1]
            if 0 <= endRow < len(self.board) and 0 <= endCol < len(self.board[0]):
                if not piecePinned:
                    if self.board[endRow][endCol][0] != allyColor:
                        moves.append(Move((r, c), (endRow, endCol), self.board))


    def getBishopMoves(self, r, c, moves):
        """
        Get all the bishop moves for the pawn located at row, col and these moves to the list
        """
        piecePinned = False
        pinDirection = ()
        for i in range(len(self.pins)-1, -1, -1):
            if self.pins[i][0] == r and self.pins[i][1] == c:
                piecePinned = True
                pinDirection = (self.pins[i][2], self.pins[i][3])
                self.pins.remove(self.pins[i])
                break

        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        enemyColor = "b" if self.whiteToMove else "w"
        for d in directions:
            for i in range(1, 8):
                endRow = r + d[0]*i
                endCol = c + d[1]*i
                if 0 <= endRow < len(self.board) and 0 <= endCol < len(self.board[0]):
                    if not piecePinned or pinDirection == d or pinDirection == (-d[0], -d[1]):
                        if self.board[endRow][endCol] == "--":
                            moves.append(Move((r, c), (endRow, endCol), self.board))
                        elif self.board[endRow][endCol][0] == enemyColor:
                            moves.append(Move((r, c), (endRow, endCol), self.board))
                            break
                        else:
                            break
                else:
                    break

    def getQueenMoves(self, r, c, moves):
        """
        Get all the queen moves for the pawn located at row, col and these moves to the list
        """
        self.getRookMoves(r, c, moves)
        self.getBishopMoves(r, c, moves)

    def getKingMoves(self, r, c, moves):
        """
        Get all the king moves for the pawn located at row, col and these moves to the list
        """
        kingMoves = [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 0), (-1, 1), (-1, -1)]
        allyColor = "w" if self.whiteToMove else "b"
        for i in range(len(kingMoves)):
            endRow = r + kingMoves[i][0]
            endCol = c + kingMoves[i][1]
            if 0 <= endRow < len(self.board) and 0 <= endCol < len(self.board[0]):
                if self.board[endRow][endCol][0] != allyColor:  # not an ally, means enemy piece or empty
                    # place the king on end square and check for checks
                    if allyColor == 'w':
                        self.whiteKingLocation = (endRow, endCol)
                    else:
                        self.blackKingLocation = (endRow, endCol)

                    inCheck, pins, checks = self.checkForPinsAndChecks()
                    if not inCheck:
                        moves.append(Move((r, c), (endRow, endCol), self.board))
                    # place the king back on the original square
                    if allyColor == 'w':
                        self.whiteKingLocation = (r, c)
                    else:
                        self.blackKingLocation = (r, c)

    def getCastleMoves(self, r, c, moves, allyColor):
        """
        Geenerate all valid castle moves for the king and them to the list of moves
        :param r:
        :param c:
        :param moves:
        :param allyColor:
        :return:
        """
        inCheck, _, __ = self.checkForPinsAndChecks()
        if inCheck:
            return  # can't castle when we are in check
        if (self.whiteToMove and self.currentCastlingRight.wks) or (not self.whiteToMove and self.currentCastlingRight.bks):
            self.getKingsideCastleMoves(r, c, moves, allyColor)
        if (self.whiteToMove and self.currentCastlingRight.wqs) or (not self.whiteToMove and self.currentCastlingRight.bqs):
            self.getQueensideCastleMoves(r, c, moves, allyColor)

    def getKingsideCastleMoves(self, r, c, moves, allyColor):
        if self.board[r][c+1] == "--" and self.board[r][c+2] == "--":
            if not self.squareUnderAttack(r, c+1) and not self.squareUnderAttack(r, c+2):
                moves.append(Move((r, c), (r, c+2), self.board, isCastleMove=True))

    def getQueensideCastleMoves(self, r, c, moves, allyColor):
        if self.board[r][c-1] == "--" and self.board[r][c-2] == "--" and self.board[r][c-3] == "--":
            if not self.squareUnderAttack(r, c-1) and not self.squareUnderAttack(r, c-2):
                moves.append(Move((r, c), (r, c-2), self.board, isCastleMove=True))


class CastleRights():
    def __init__(self, wks, bks, wqs, bqs):
        self.wks = wks
        self.bks = bks
        self.wqs = wqs
        self.bqs = bqs


class Move():
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}

    def __init__(self, start_sq, end_sq, board, isEnpassantMove = False, isCastleMove = False):
        self.start_row = start_sq[0]
        self.start_col = start_sq[1]
        self.end_row = end_sq[0]
        self.end_col = end_sq[1]
        self.pieceMoved = board[self.start_row][self.start_col]
        self.pieceCaptured = board[self.end_row][self.end_col]
        # Pawn promotion
        self.isPawnPromotion = False
        self.isPawnPromotion = (self.pieceMoved == 'wp' and self.end_row == 0) or (self.pieceMoved == 'bp' and self.end_row == 7)
        # Enpassant
        self.isEnpassantMove = isEnpassantMove
        if self.isEnpassantMove:
            self.pieceCaptured = 'wp' if self.pieceMoved == 'bp' else 'bp'

        # castle move
        self.isCastleMove = isCastleMove

        self.isCaptureMove = self.pieceCaptured != "--"
        self.moveId = self.start_row * 1000 + self.start_col * 100 + self.end_row * 10 + self.end_col

    '''
    Overriding the equals method
    '''
    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveId == other.moveId
        return False

    def getChessNotation(self):
        return self.getRankFile(self.start_row, self.start_col) + self.getRankFile(self.end_row, self.end_col)

    def getRankFile(self, r, c):
        return self.colsToFiles[c] + self.rowsToRanks[r]

    # overriding the str() function
    def __str__(self):
        # castle move
        if self.isCastleMove:
            return "O-O" if self.end_col == 6 else "O-O-O"

        endSquare = self.getRankFile(self.end_row, self.end_col)
        # pawn moves
        if self.pieceMoved[1] == "p":
            if self.isCaptureMove:
                return self.colsToFiles[self.start_col] + "x" + endSquare
            else:
                return endSquare


        # piece moves
        moveString = self.pieceMoved[1]
        if self.isCaptureMove:
            moveString += "x"
        return moveString+endSquare