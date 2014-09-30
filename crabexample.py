#!/usr/bin/python3

from BPNN import *
from random import choice, randint

#CREATE 100 EXAMPLES
train=[]
test=[]

with open('crabs.csv') as f:
	header = f.readline()
	for i in range(100):
		line = f.readline()
		ip = [line.split(',')[2]]
		if ip[0] == '"M"': ip[0] = 0
		if ip[0] == '"F"': ip[0] = 1
		op = [float(line.split(',')[-4]), float(line.split(',')[-2])]
		train.append( Example( ip, op ))

with open('crabs.csv') as f:
	header = f.readline()
	for i in range(100):
		line = f.readline()
		ip = [line.split(',')[2]]
		if ip[0] == '"M"': ip[0] = 0
		if ip[0] == '"F"': ip[0] = 1
		op = [float(line.split(',')[-4]), float(line.split(',')[-2])]
		test.append( Example( ip, op ))

nn = Neural_Net( alpha = 0.1, ip = 1, h = 5, op = 1)
nn.initialize_weights( )
nn.backward_connect_nodes( )

for i in range( 1000 ) :
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
			print(actual, 'Actual')
			print(hypothesis, 'Hypothesis \n\n')
print('%2f%% correct. ' % (correct / len(examples) * 100), correct, ' correct out of ', len(examples))
		
