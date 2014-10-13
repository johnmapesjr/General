#!/usr/bin/python3

def g( x ): return x

class Node( ):
	def __init__( self ):
		self.value = 0.0
		self.i_connections = [ ]
		self.o_connections = [ ]
	def update( self ):
		summation = 0.0
		for connection in self.i_connections:
			summation += connection.weight * connection.node.value
		self.value = g( summation )

class Layer( ):
	def __init__( self, size ):
		self.size = size
		self.nodes = [ Node( ) for i in range( size ) ]
	def __str__( self ):
		return "Layer has %s nodes." % ( self.size )

class Connection( ):
	def __init__( self, node ):
		self.weight = 0.0
		self.node = node

def FullyConnectNodes( Input_Nodes, Output_Nodes ):
	for i_node in Input_Nodes:
		for o_node in Output_Nodes:
			o_node.i_connections.append( Connection( i_node ))

class Neural_Net( ):
	def __init__( self ):
		self.ipl = Layer( 5 )
		self.opl = Layer( 5 )
		FullyConnectNodes( self.ipl.nodes, self.opl.nodes )
	def calculate( self ):
		print( "Calculating..." )
		for node in self.opl.nodes:
			node.update( )
		
nn = Neural_Net( )


print ( "input" )
for node in nn.ipl.nodes:
 print( node.value )
print ( "output" )
for node in nn.opl.nodes:
 print( node.value )
print ( "weights" )
for node in nn.opl.nodes:
	print( "-" )
	for connection in node.i_connections:
		print( connection.weight )

nn.ipl.nodes[0].value = 0.5
nn.ipl.nodes[1].value = 0.5
nn.ipl.nodes[2].value = 0.5
nn.opl.nodes[0].i_connections[0].weight = 0.5
nn.opl.nodes[0].i_connections[1].weight = 0.5
nn.opl.nodes[0].i_connections[2].weight = 0.5
nn.opl.nodes[0].i_connections[3].weight = 0.5

nn.calculate( )


print ( "input" )
for node in nn.ipl.nodes:
 print( node.value )
print ( "output" )
for node in nn.opl.nodes:
 print( node.value )
print ( "weights" )
for node in nn.opl.nodes:
	print( "-" )
	for connection in node.i_connections:
		print( connection.weight )
