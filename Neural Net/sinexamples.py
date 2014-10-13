#!/usr/bin/python3

from BPNN import *
from math import cos, radians, degrees
from random import choice

examples = [Example( [i/31],[cos( i/10 ) ]) for i in range( 63 )]

nn = Neural_Net( alpha = 0.10, ip = 1, h = 100, op = 1)
nn.initialize_weights( )
nn.backward_connect_nodes( )

for i in range( 1000 ) :
	for example in [choice( examples) for x in range( len( examples ) )]:
		nn.assign_input( example.ip) 
		nn.calculate( )
		nn.train( example)
	if i%10: nn.alpha -= 0.0001
	print(nn.alpha)
	with open('sin%04i.dat' % i,'w') as f:
		for example in examples:
				nn.assign_input( example.ip) 
				nn.calculate( )
				print( example.ip[0], nn.opl.nodes[0].value, file=f)
		
