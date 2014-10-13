#!/usr/bin/python3

from BPNN import *
from random import choice, randint, sample
from time import sleep
from collections import Counter
from multiprocessing import process
from copy import deepcopy

#CREATE 100 In Sample EXAMPLES
examples=[]

for i in range(100):
	value = randint(1,1000)
	ip = [float(s) for s in '{:012b}'.format(value)]
	op = [float(s) for s in '{:012b}'.format(value + 1)]
	examples.append( Example( ip, op ))

nets = []
for i in range(5):
	nn = Neural_Net( alpha = 0.10, ip = 12, h = 12, op = 12)
	nn.initialize_weights( )
	nn.backward_connect_nodes( )
	nets.append(nn)

hardest = set()

for nn in nets:
	for i in range( 1000 ) :
		correct = 0
		incorrect = []
		for example in [choice( examples) for x in range( len( examples ) )]:
			nn.assign_input( example.ip) 
			nn.calculate( )
			nn.train( example)
			actual = example.op
			hypothesis = [abs(round(node.value,0)) for node in nn.opl.nodes]
			if hypothesis == actual: 
				correct += 1	
			else: incorrect.append(example)
		if i % 10 == 0:
			nn.alpha -= 0.001
	#		print('avg error: ', nn.avgerror)
			print('%2f%% correct. ' % (correct / len(examples) * 100), correct, ' correct out of ', len(examples), ' alpha ', nn.alpha)
		if correct >= len(examples) - 3: 
			#for ex in [(x.ip, x.op) for x in incorrect]:
			#	print(ex[0])
			#	print(ex[1])
			for item in incorrect: hardest.add( item )
			break

#Train a new neural net to recognize the hardest to classify examples...
non_hardest_example_set = set(examples) - hardest
hardest_org = deepcopy(hardest)
for ex in non_hardest_example_set: ex.op = [-1.0]
for ex in hardest: ex.op = [1.0]
trainset = non_hardest_example_set.union(hardest)
hard_nn = Neural_Net(alpha = 0.1, ip=12, h=12, op=1)
hard_nn.initialize_weights( )
hard_nn.backward_connect_nodes( )
#print([(ex.op,ex.ip) for ex in trainset])
for i in range(1000):
	for ex in [sample(trainset,1)[0] for x in range(len(trainset))]:
		hard_nn.assign_input(ex.ip)
		hard_nn.calculate()
		hard_nn.train(ex)
	if i % 10 == 0:
		hard_nn.alpha -= 0.001
		

#Train a new neural net to solve the hardest to solve examples...
hard_solve_nn = Neural_Net(alpha = 0.1, ip =12, h =12, op=12)	
hard_solve_nn.initialize_weights( )
hard_solve_nn.backward_connect_nodes( )
for i in range(1000):
	for ex in [sample(hardest_org,1)[0] for x in range(len(hardest_org))]:
		hard_solve_nn.assign_input(ex.ip)
		hard_solve_nn.calculate()
		hard_solve_nn.train(ex)
	if i % 10 == 0:
		hard_solve_nn.alpha -= 0.001


#Out of Sample 1000 EXAMPLES
examples=[]

for i in range(1000):
	value = i
	ip = [float(s) for s in '{:012b}'.format(value)]
	op = [float(s) for s in '{:012b}'.format(value + 1)]
	examples.append( Example( ip, op ))

for nn in nets:
	correct = 0
	for i, example in enumerate(examples):
			###TEST
			hard_nn.assign_input(example.ip)
			hard_nn.calculate()
			if hard_nn.opl.nodes[0].value > -0.0:
				#print('Hard...')
				del examples[i]
				continue
				#hard_solve_nn.assign_input(example.ip)
				#hard_solve_nn.calculate()
				#print([abs(round(node.value,0)) for node in nn.opl.nodes])
			#else: print('Easy...')

			###TEST
			nn.assign_input( example.ip) 
			nn.calculate( )
			actual = example.op
			hypothesis = [abs(round(node.value,0)) for node in nn.opl.nodes]
			if hypothesis == actual: 
				correct += 1	
			#else:
				#pass
				#print(actual, 'Actual')
				#print(hypothesis, 'Hypothesis \n\n')
	print('%2f%% correct. ' % (correct / len(examples) * 100), correct, ' correct out of ', len(examples))
		
sleep(3)
for nn in nets:
	print('Watch me count to one thousand now...')
	nn.assign_input( [float(s) for s in '{:012b}'.format(0)] )

for i in range(100):
	hypothesi = []
	for nn in nets:
		nn.calculate()
		hypothesis_in_list = [abs(round(node.value,0)) for node in nn.opl.nodes]
		hypothesis_in_decimal = int(''.join([str(int(f)) for f in hypothesis_in_list]),2)
		hypothesi.append(hypothesis_in_decimal)
	winning_hypothesis = Counter(hypothesi).most_common()[0][0]
	print(winning_hypothesis)
	winning_hypothesis_in_list = [float(s) for s in '{:012b}'.format(winning_hypothesis)]
	for nn in nets:
		nn.assign_input(winning_hypothesis_in_list)

