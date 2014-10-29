#!/usr/bin/python3

from AI import *
import chess
import Minimax
import sys

def Human_Move():
	global board
	if board.is_check():
		print('Check!')
	print('''Please enter your move in UCI format e.g. e2e3, a1a3, etc.''')
	move_is_valid = False
	while not move_is_valid: 
			move = chess.Move.from_uci( input() )
			if move in board.legal_moves:
				board.push( move )
				move_is_valid = True
			else:
				print('Not a valid move, try again')
	a = board.is_game_over()
	if board.is_game_over():
		print("You have won.")
		winner = "human"
		ai.learn(winner) 
		sys.exit("You have won.")

def AI_Move():
	global board
	move = ai.Move( board )
	if move in board.legal_moves:
		board.push(move)
	else:
		print("MALFUNCTION HAL 2000\n Board is %s HAL Wanted %s" % (board.fen(), move)) 
		exit(0)
	#END OF HALS TURN
	print('The computer has moved %s' % (move))
	print("Board is %s " % (board.fen()))
	if board.is_game_over():
		print("Computers has won.")
		winner = "computer"
		ai.learn(winner)
		sys.exit("AI Computer has won.")

def Minimax_Move(color):
	global board
	move = Minimax.Minimax( board, color )
	if move in board.legal_moves:
		board.push(move)
	else:
		print("Minimax Error\n Board is %s Minimax attempted %s" % (board.fen(), move)) 
		exit(0)
	#END OF HALS TURN
	print('The computer has moved %s' % (move))
	print("Board is %s " % (board.fen()))
	if board.is_game_over():
		print("Computers has won.")
		ai.learn("human") #uncommented for ai vs. computer testing.
		sys.exit("Minimax Computer has won.")

def Computer_vs_Computer():
	while True:
		Minimax_Move('w')
		Minimax_Move('b')
	exit(0)

def AI_vs_Computer():
    while True:
        Minimax_Move('w')
        AI_Move()

#Initialize AI
ai = AI()
#Initialize board and player chooses Black or White
board = chess.Bitboard()
Computer_vs_Computer() #uncomment for computer vs. computer testing
player_color = ''
while player_color != 'w' and player_color != 'b' and player_color !='self':
	print('''Choose a start color, valid input is w or b''')
	player_color = input()
#Player is White and moves first.
if player_color == 'w':	
	while True:
		Human_Move()
		AI_Move()
#Player is Black and computer moves first.
elif player_color == 'self':
	AI_vs_Computer()
else:
	while True:
		AI_Move()
		Human_Move()






