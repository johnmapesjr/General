



class TreeNode():
	#Active board state at this point
        #       Stored in FEN chess notation
        BoardState = ""

        NumberOfTimesReached  = 0
        NumberOfTimesWon      = 0
        NumberOfTimesDraw     = 0
        GameHistory           = 0

        #List of known reachable nodes
        #   Move stored in a pair of bytes
        #               Ending Location, Piece
        #   And a pointer to resulting Node
        KnownMovesTaken = []

                      
                      
        def __init__(self, board):
            self.board = board 


