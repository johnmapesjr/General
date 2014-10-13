#!/usr/bin/python3

from math import e, tanh
from random import random

#def g( x ): 
#	if x > 10: return 1
#	if x < -10: return 0
#	else: return 1.0 / ( 1.0 + e ** -x )
#def g_d( x ): return e ** -x / ( 1.0 + e ** -x ) ** 2
def g( x ): return tanh(x)
def g_d( x ): return 1 - tanh(x) * tanh(x)

class Node( ):
	def __init__( self ):
		self.value = 0.0
		self.bias = False
		self.summation = 0.0
		self.delta = 0.0
		self.i_connections = [ ]
		self.o_connections = [ ]
	def update( self ):
		if self.bias: 
			self.value = 1.0
			return
		self.summation = 0.0
		for connection in self.i_connections:
			self.summation += connection.weight * connection.i_node.value
		self.value = g( self.summation )
		
class Layer( ):
	def __init__( self, size, bias=True ):
		self.size = size
		if bias: self.size += 1
		self.nodes = [ Node( ) for i in range( self.size ) ]
		if bias: self.nodes[0].bias = True
	def __str__( self ):
		return "Layer has %s nodes." % ( self.size )

class Connection( ):
	def __init__( self, node ):
		self.weight = 0.0
		self.i_node = node

def FullyConnectNodes( Input_Nodes, Output_Nodes ):
	for o_node in Output_Nodes:
		for i_node in Input_Nodes:
			o_node.i_connections.append( Connection( i_node ))

class Neural_Net( ):
	def __init__( self, alpha=0.1, ip=5, h=5, op=5, Lambda_opl = 0.0001, Lambda_hil = 0.00001 ):
		self.Lambda_opl = Lambda_opl
		self.Lambda_hil = Lambda_hil
		self.error = 0
		self.avgerror = 0
		self.avgerrorqueuelen = op * 100
		self.avgerrorqueue = [0] * self.avgerrorqueuelen
		self.alpha = alpha
		self.ipl = Layer( ip )
		self.hil = Layer( h )
		self.opl = Layer( op, bias=False )
		FullyConnectNodes( self.ipl.nodes, self.hil.nodes )
		FullyConnectNodes( self.hil.nodes, self.opl.nodes )

	def initialize_weights( self ):
		for node in self.hil.nodes:
			for connection in node.i_connections:
				connection.weight = random( ) / 10
		for node in self.opl.nodes:
			for connection in node.i_connections:
				connection.weight = random( ) / 10

	def backward_connect_nodes( self ):
		for node in self.opl.nodes:
			for connection in node.i_connections:
				connection.o_node = node
				connection.i_node.o_connections.append( connection )
		for node in self.hil.nodes:
			for connection in node.i_connections:
				connection.o_node = node
				connection.i_node.o_connections.append( connection )

	def assign_input( self, ip ):
		for ( index, node ) in	enumerate( self.ipl.nodes ):
			if node.bias: node.value = 1.0; continue
			node.value = ip[ index - 1 ]

	def calculate( self ):
		#print( "Calculating..." )
		for node in self.hil.nodes:
			node.update( )
		for node in self.opl.nodes:
			node.update( )

	def train( self, example, batch=False ):
		#print( "Training..." )
		for ( index, node ) in enumerate( self.opl.nodes ):
			self.error = example.op[ index ] - node.value + sum([connection.weight for connection in node.i_connections]) * self.Lambda_opl / len(self.opl.nodes)
			self.avgerrorqueue.append(self.error)
			self.avgerror = sum(self.avgerrorqueue) / self.avgerrorqueuelen
			del self.avgerrorqueue[0]
			node.delta = self.error * g_d( node.summation ) 
			for connection in node.i_connections:
				connection.weight = connection.weight + self.alpha * connection.i_node.value * node.delta
		for node in self.hil.nodes:
			output_summation = 0.0
			for connection in node.o_connections:
				output_summation += connection.weight * connection.o_node.delta
			node.delta = g_d( node.summation ) * output_summation + sum([connection.weight for connection in node.i_connections]) * self.Lambda_hil / len(self.hil.nodes)
			for connection in node.i_connections:
				connection.weight = connection.weight + self.alpha * connection.i_node.value * node.delta
	def display_net( self, verbose = False):
		print ( "input" )
		print([node.value for node in self.ipl.nodes])
		if verbose:
			print ( "hidden" )
			print([node.value for node in self.hil.nodes])
		print ( "output" )
		print([node.value for node in self.opl.nodes])
		if verbose:
			print ( "weights-h-i" )
			for node in self.hil.nodes:
				print([ connection.weight for connection in node.i_connections ])
			print ( "weights-o-h" )
			for node in self.opl.nodes:
				print([ connection.weight for connection in node.i_connections ])

class Example( ):
 def __init__( self, ip, op ):
		self.ip = ip
		self.op = op


def Test( ):
	nn = Neural_Net( h = 2)
	nn.initialize_weights( )
	nn.backward_connect_nodes( )
	nn.display_net( )
	example = Example( [ 1.0, 0.2, 0.2, 0.2, 0.0 ], [ 0.8, 0.2, 0.2, 0.2, 0.8 ] )
	nn.assign_input( example.ip )
	for i in range(100):
		nn.calculate( )
		nn.train( example )
	nn.calculate( )
	nn.display_net( verbose=True)

#Test()
