#!/usr/bin/python3
import queue
import TreeNode
import chess
from pickle import *
import Minimax

#Tree = Tree()

#Does all the actual work!
class AI():
        #The AI's knowledge of current board, used for move checking
        chessboard = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
                      ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'], 
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                      [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                      ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'], 
                      ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]
        
        #Total game count and
        #   Number of current game
        totalgamecount = 1
        currentgame    = 1
        BoardDictionary = {}  #data file dictionary
        BoardPath = [] #list of fens taken during game
        testcount = 0
        
        #Move will be a string of the following formate
        #   a lowercase character and number representing board location
        #   a space seperating another set of characters same as above
        #       First set is starting location second is end location
        #   It will return a move of the similiar formate, or 
        #           invalid if the given move isn't valid
        #   Move will be None if AI makes first move
        def Move(self, board):
            '''calculate and return move'''
            '''if self.testcount == 3:#temporarily add to dictionary every third move
                self.learn()
                self.testcount = 0
            self.testcount +=1'''
            
            BestMove = "" #calculated bestmove returned at end
            MoveWeights = {} #dictionary of all legal moves and calculated weights
            NumberOfLegalMoves = 0 #add up legal moves
            NumberOfMovesInDictionary = 0 #add up found moves
            
            '''cycle through legal moves and assign weights'''
            for move in board.legal_moves:
                NumberOfLegalMoves +=1 #add up legal moves
                WinPercentage = 0 #initialize win% to 0, board may not be in dictionary
                
                KillWeightBefore = 0
                KillWeightAfter = 0
                
                
                KillWeightBefore = Minimax.Evaluator(board, 'b')
                
                board.push(move)
                fen = board.fen() #i need the fen notation for BoardDictionary
                MoveWeights[fen] = 0 #initialize each moves weight to 0                        
                KillWeightAfter = Minimax.Evaluator(board, 'b')
                MoveWeights[fen] = KillWeightAfter - KillWeightBefore#get weighted score >0 back if kills a piece
                board.pop()
                
                '''add weight to move if found in dictionary'''
                if fen in self.BoardDictionary:#get info from board if found in dictionary
                    NumberOfMovesInDictionary +=1 #add up found moves
                    boardData = self.BoardDictionary.get(fen)
                    NumberOfTimesReached = boardData[0]
                    NumberOfTimesWon = boardData[1]
                    #NumberOfTimesDraw = boardData[2]
                    WinPercentage = NumberOfTimesWon/NumberOfTimesReached
                    #MoveWeights[fen] = WinPercentage #assign weight to move
                
                    
                '''add kill weight to move'''
                MoveWeights[fen] += WinPercentage
                
                if BestMove == "":
                    BestMove = move
                    HighestWeight = MoveWeights[fen]
                
                '''do something random here'''            
                if MoveWeights[fen] > HighestWeight:
                    BestMove = move
                    HighestWeight = MoveWeights[fen]
                
            for move in board.legal_moves: #loop through again to find best move fen
                if move == BestMove:
                    board.push(move)
                    fen = board.fen()
                    board.pop()
                    if fen in self.BoardDictionary:
                        print("move found in dictionary")
                    else:
                        print("add move to dictionary")
                        self.BoardDictionary[fen]=[0,0,0,0]
                    
                    
            
            print("Number of legal moves:", NumberOfLegalMoves)
            print("Number of moves found in dictionary:", NumberOfMovesInDictionary)
            self.BoardPath.append(fen)    
            '''Return move in four characters, start and end square'''
            return BestMove

        #Interage through board and convert it into FEN format
        #   Return said string
        def BoardToFEN(self):
            FEN = ""
            for row in self.chessboard:
                spacecount = 0
                for square in row:
                    if (square == ' '):
                        spacecount += 1
                    else:
                        if (spacecount > 0):
                            FEN += str(spacecount)
                            spacecount = 0
                        FEN += str(square)
                if (spacecount > 0):
                    FEN += str(spacecount)
                    spacecount = 0
                if (row != self.chessboard[-1]):
                    FEN += '/'
            return FEN

        #Returns a list of valid moves based on chessboard
        #   Moves defined as four single didget numbers
        def ValidMoves(self):
            cb = chessboard
            validmoves = []
            for r in range(7):
                for c in range(7):
                    piece = cb[r][c]
                    if (cb == 'r' or cb == 'R'):
                        R = r
                        while (R >= 0):
                            if (cb[R][c] == ' '): 
                                validmoves += ("%i%i%i%i", r,c,R,c)
                                R -= 1
                                continue    
                            elif (cb[R][c].isLower() - cb[r][c].isLower() == 0):
                                validmoves += ("%i%i%i%i", r,c,R,c)
                            break
                        R = r
                        while (R <= 7):
                            if (cb[R][c] == ' '): 
                                validmoves += ("%i%i%i%i", r,c,R,c)
                                R += 1
                                continue    
                            elif (cb[R][c].isLower() - cb[r][c].isLower() == 0):
                                validmoves += ("%i%i%i%i", r,c,R,c)
                            break
                    
        def __init__(self):
            self.loadfile()
            return    

        def loadfile(self):
            #f = open('chess.dat', 'rb')
            #self.BoardDictionary = load(f)
            #f.close()
            print("loadfile")
            self.BoardDictionary = {};
            try:
               with open('chess.dat', "rb") as file:
                   unpickler = Unpickler(file);
                   self.BoardDictionary = unpickler.load();
                   if not isinstance(self.BoardDictionary, dict):
                      self.BoardDictionary = {};
            except EOFError:
               return {}
        
        def learn(self, winner):
            print("learn")
            for fen in self.BoardPath:
                boardData = self.BoardDictionary.get(fen, None)
                if boardData != None:
                    a = boardData[0]
                    boardData[0] += 1 #of times reached
                    if winner == "computer":
                        boardData[1] += 1 #of times won
                    #NumberOfTimesDraw = boardData[2]
            try:
               with open('chess.dat', "wb") as file:
                   #pickle = pickler(file);
                   #BoardDictionary = unpickler.load();
                   dump(self.BoardDictionary, file)
            except EOFError:
               return {}
                     
            
            
            
            
            










