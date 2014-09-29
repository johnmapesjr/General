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
		op = [float(line.split(',')[-4]), float(line.split(',')[-2])]
		print(ip, op)
		exit()
		train.append( Example( ip, op ))

nn = Neural_Net( alpha = 0.1, ip = 12, h = 20, op = 12)
nn.initialize_weights( )
nn.backward_connect_nodes( )

for i in range( 1000 ) :
	for example in [choice( examples) for x in range( len( examples ) )]:
		nn.assign_input( example.ip) 
		nn.calculate( )
		nn.train( example)

#CREATE 1000 EXAMPLES
examples=[]

for i in range(1000):
	value = i
	ip = [float(s) for s in '{:012b}'.format(value)]
	op = [float(s) for s in '{:012b}'.format(value + 1)]
	examples.append( Example( ip, op ))

correct = 0
for example in examples:
		nn.assign_input( example.ip) 
		nn.calculate( )
		actual = example.op
		hypothesis = [abs(round(node.value,0)) for node in nn.opl.nodes]
		if hypothesis == actual: 
			correct += 1	
		else:
			print(actual, 'Actual')
			print(hypothesis, 'Hypothesis \n\n')
print('%2f%% correct. ' % (correct / len(examples) * 100), correct, ' correct out of ', len(examples))
		

print('Watch me count to one thousand now...')
nn.assign_input( [float(s) for s in '{:012b}'.format(0)] )
for i in range(1000):
	nn.calculate()
	hypothesis_in_list = [abs(round(node.value,0)) for node in nn.opl.nodes]
	hypothesis_in_decimal = int(''.join([str(int(f)) for f in hypothesis_in_list]),2)
	print(hypothesis_in_decimal)
	nn.assign_input(hypothesis_in_list)

