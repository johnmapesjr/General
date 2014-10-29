from re import compile as pattern, findall

p = pattern('p')
r = pattern('r')
n = pattern('n')
b = pattern('b')
q = pattern('q')
k = pattern('k')
P = pattern('P')
R = pattern('R')
N = pattern('N')
B = pattern('B')
Q = pattern('Q')
K = pattern('K')

def pieces(piece, fen):
	return len(findall(piece, fen.split()[0]))

def Evaluator( board, color ):
	fen = board.fen()
	mobility = len(board.legal_moves) * 0.1
	score = 0
	score += pieces(p, fen) * 1
	score += pieces(r, fen) * 5.1
	score += pieces(n, fen) * 3.2
	score += pieces(b, fen) * 3.3
	score += pieces(q, fen) * 8.8
	score += pieces(k, fen) * 3
	score -= pieces(P, fen) * 1
	score -= pieces(R, fen) * 5.1
	score -= pieces(N, fen) * 3.2
	score -= pieces(B, fen) * 3.3
	score -= pieces(Q, fen) * 8.8
	score -= pieces(K, fen) * 3
	if color == 'w': return score * -1 + mobility
	if color == 'b': return score + mobility

def Loss( board ):
	if board.is_stalemate(): 
		print('stalemate')
		return True
	elif board.is_insufficient_material(): 
		print('IM')
		return True
	elif board.is_fivefold_repitition():
		print('fivefold rep')
		return True
	elif board.is_seventyfive_moves():
		print('75 moves')
		return True
	elif board.can_claim_threefold_repitition():
		print('3fold')
		return True
	elif board.can_claim_fifty_moves():
		print('fifty_moves')
		return True
	else: False

def Win( board ):
	if board.is_checkmate():
		print('checkmate!')
		return True
	else: False

def Minimax( board, color, ply = 1 ):
	maximum_min_move = 0
	max_moves = {move:-1000 for move in board.legal_moves}
	for max_move in max_moves:
		min_score = 10000
		board.push( max_move )
		if Loss( board ): 
			print('LOSS IMMINENT')
			board.pop()
			continue
		if Win( board ):
			print('WIN IMMINENT')
			board.pop()
			return max_move
		for min_move in board.legal_moves:
			board.push( min_move )
##PLY 2
			if Loss( board ): 
				print('LOSS IMMINENT')
				board.pop()
				continue
			if Win( board ):
				print('WIN IMMINENT')
				board.pop()
				return max_move
			for max_move2 in board.legal_moves:
				board.push( max_move )
				if Loss( board ): 
					print('LOSS IMMINENT')
					board.pop()
					continue
				if Win( board ):
					print('WIN IMMINENT')
					board.pop()
					return max_move
				for min_move2 in board.legal_moves:
					board.push( min_move )
					if Evaluator( board, color ) < min_score: 
						min_score = Evaluator( board, color )
						max_moves[max_move] = min_score
					board.pop()
				board.pop()
			board.pop()
		board.pop()
	maximum_min_move = max(max_moves, key=max_moves.get)
	return maximum_min_move
##PLY 2
#			if Evaluator( board, color ) < min_score: 
#				min_score = Evaluator( board, color )
#				max_moves[max_move] = min_score
#			board.pop()
#		board.pop()
#	maximum_min_move = max(max_moves, key=max_moves.get)
#	return maximum_min_move
