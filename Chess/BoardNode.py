# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 19:19:23 2014

@author: owner
"""

class BoardNode():
	#Active board state at this point
        #       Stored in FEN chess notation     
        BoardState = ""

        NumberOfTimesReached  = 0
        NumberOfTimesWhiteWon = 0
        NumberOfTimesDraw     = 0
        GameHistory           = 0

        #List of known reachable nodes
        #   Move stored in a pair of bytes
        #               Ending Location, Piece
        #   And a pointer to resulting Node
        #KnownMovesTaken = []

                      
                      
        def __init__(self):
            return
            
            
            
                
            