#!/usr/bin/python3

from math import e

alpha = 0.1

def g(x): 
	if x > 0:
		return 1
	else: return 0

#def g(x): return 1.0 / (1.0 + e ** -x)

mul = lambda x, y: x * y

add = lambda x, y: x + y

innerproduct = lambda X, Y: sum( map ( mul, X, Y ))

scalar_vector_product = lambda x, Y: [x * y for y in Y]

vector_vector_sum = lambda X, Y: [x for x in map( add, X, Y )]

class Example():
	def __init__(self, inputs, output):
		self.inputs = inputs
		self.output = output

class Perceptron():
	def __init__(self, weights):
		self.weights = weights
	def hypothesis(self):
		self.output = g( innerproduct( self.weights, self.inputs ) )
		return self.output
	def train(self, example):
			p.inputs = example.inputs
			error = example.output - p.hypothesis()
			self.weights = vector_vector_sum( self.weights, scalar_vector_product( (alpha * error), self.inputs ))

def Stats():
	correct = 0
	for example in examples:
		p.inputs = example.inputs
		print( "Given %s, I guess %s, the correct answer is %s." % ( p.inputs, p.hypothesis(), example.output ))
		if p.output ==	example.output: correct+=1
	print( "I got %s out of %s correct or %s percent." % ( correct, len( examples ), correct / len( examples ) * 100 ))
	print( "My weights are %s." % ( p.weights ) )

examples = []

#SEE CHART
examples.append( Example([1,1,4], 0) )
examples.append( Example([1,2,2], 0) )
examples.append( Example([1,2,7], 0) )
examples.append( Example([1,3,1], 0) )
examples.append( Example([1,7,2], 0) )
#CENTER OF CHART UNCLASSIFIABLE
#examples.append( Example([1,5,5], 0) )
examples.append( Example([1,5,8], 1) )
examples.append( Example([1,6,9], 1) )
examples.append( Example([1,5,5], 1) )
examples.append( Example([1,8,5], 1) )
examples.append( Example([1,8,7], 1) )
examples.append( Example([1,8,9], 1) )

p = Perceptron( [0.1,0.1,0.1] )
epochs = 100
for epoch in range(epochs):
	for example in examples:
		p.train(example)
print("I trained for %s epochs." % epoch)
Stats()

