#!/usr/bin/python3

from BPNN import *
from random import choice

#CREATE 100 TRAINING EXAMPLES & 100 TESTING EXAMPLES
train=[]
test=[]

with open('crabs.csv') as f:
	header = f.readline()
	for i in range(100):
		line = f.readline()
		op = [line.split(',')[2]]
		if op[0] == '"M"': op[0] = 0
		if op[0] == '"F"': op[0] = 1
		ip = [float(line.split(',')[-4]), float(line.split(',')[-2])]
		train.append( Example( ip, op ))
	for i in range(100):
		line = f.readline()
		op = [line.split(',')[2]]
		if op[0] == '"M"': op[0] = 0
		if op[0] == '"F"': op[0] = 1
		ip = [float(line.split(',')[-4]), float(line.split(',')[-2])]
		test.append( Example( ip, op ))

nn = Neural_Net( alpha = 0.10, ip = 2, h = 10, op = 1)
nn.initialize_weights( )
nn.backward_connect_nodes( )

Epochs = 1000
for i in range( Epochs ) :
	for example in [choice( train) for x in range( len( train ) )]:
		nn.assign_input( example.ip) 
		nn.calculate( )
		nn.train( example)

correct = 0
for example in test:
		nn.assign_input( example.ip) 
		nn.calculate( )
		actual = example.op
		hypothesis = [abs(round(node.value,0)) for node in nn.opl.nodes]
		if hypothesis == actual: 
			correct += 1	
			print('correct')
		else:
			print('whoops...')
			print(actual, 'Actual')
			print(hypothesis, 'Hypothesis \n\n')
print('%2f%% correct. ' % (correct / len(test) * 100), correct, ' correct out of ', len(test))
		
