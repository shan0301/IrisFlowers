#######################################
######### Irises Classification #######
# Version: 0.1
#
# Author: Chet Mancini
# Email: cam479 at cornell dot edu
# Web: chetmancini.com
# Warranty: None at all
#
# CS4700, Fall 2011
# Cornell University
#
#######################################


############# Imports #################
from __future__ import division
from Iris import *
from MatrixOperations import *
from HelperFunctions import *
import math
import random

class Example:

	def __init__(self):
		inputX = []
		outputY = []


class Network:

	'''
	Nodes [INPUT, HIDDEN, OUTPUT]
	'''
	def __init__(self, nodeCounts):

		#nodes[0] = INPUT node list
		#nodes[1] = HIDDEN node list
		#nodes[2] = OUTPUT node list

		self.nodes = []
		for i in range(3):
			initVect = [1.0]*nodeCounts[i]
			self.nodes.append(initVect)

		hiddenInputs = [0.0] * nodeCounts[1]
		outputInputs = [0.0] * nodeCounts[2]

		self.inputWeights = zeroMatrix(len(nodes[0]), len(nodes[1]))
		self.outputWeights = zeroMatrix(len(nodes[1]), len(nodes[2]))

		for row in self.inputWeights:
			for col in row:
				col = random.uniform(-0.2, 0.2)
		for row in self.outputWeights:
			for col in row:
				col = random.uniform(-0.2, 0.2)

		activationfunction = None
		activationderivative = None


	def numLayers(self):
		return len(self.nodes)
	
	# Layer counts
	def numInput(self):
		return len(self.nodes[0])
	def numHidden(self):
		return len(self.nodes[1])
	def numOutput(self):
		return len(self.nodes[2])


	def backPropLearn(self, examples):
		delta = copy.deepcopy(self.nodes)
		iterations = 0

		while True:
			for example in examples:
				# Assign inputs
				for i in range(len(example.inputX)):
					nodes[0][i] = example.inputX[i]
				# Propogate to Hidden Layer
				for j in range(self.numHidden()):
					hiddenInputs[j] = 0.0
					for i in range(self.numInput()):
						hiddenInputs[j] += inputWeights[i][j] * self.nodes[0][i]
					self.nodes[1] = activationfunction(hiddenInputs[j])

				# Propogate to Output Layer
				for j in range(self.numOutput()):
					outputInputs[j] = 0.0
					for i in range(self.numHidden()):
						outputInputs[j] += outputWeights[i][j] * self.nodes[1][i]
					self.nodes[2] = activationfunction(outputInputs[j])


				for j in range(self.numOutput()):
					delta[2][j] = activationderivative(outputInputs[j]) * (example.outputY[j] - self.nodes[2][j])

				#propgate back through hidden
				for i in range(self.numHidden()):
					summation = 0.0
					for j in range(len(self.outputWeights)):
						summation += self.outputWeights[j] * delta[2][j]
					delta[1][i] = activationderivative(hiddenInputs[i]) * summation

				#propgate back through input
				for j in range(self.numInput()):
					summation = 0.0
					for j in range(len(self.inputWeights)):
						summation += self.inputWeights[j] * delta[1][j]
					delta[0][i] = activationderivative(example.inputX[i]) * summation

				# Update weights.
				for i in range(len(self.inputWeights)):
					for j in range(numHidden()):
						self.inputWeights[i][j] += alpha * nodes[0][i] * delta[1][j]
				for i in range(len(self.outputWeights)):
					for j in range(numOutput()):
						self.outputWeights[i][j] += alpha * nodes[1][i] * delta[2][j]

			iterations += 1

			if iterations > 50:
				break

############################################
############# Training Program #############
'''
Train
'''
def train():
	pass

'''
Load data
'''
def loaddata():
	pass

'''
Feed forward
'''
def feedForward(inputsMatrix, weightsMatrix, biasMatrix=None):
	if not biasMatrix:
		toMul = inputsMatrix
	else:
		toMul = concatenate(inputsMatrix, biasMatrix)

	net = matrix.multiply(weightsMatrix, toMul)
	output = activate(net)
	return output

'''
Eval network
'''
def evalnetwork():
	pass

'''
Back propogation
'''
def backpropagation():
	pass

'''

'''
def backPropLearning(examples, network):
	delta = []

	while True:
		for example in examples:
			for i in range(len(example.inputX)):
				a[i] = example.inputX[i]
			for l in range(2, network.layers):
				for nodeJ in l:
					inj = 0
					inj = summation of is network.w[i][j]*a[i]
					a[j] = network.activationfunction(inj)
			for node j in output layer:
				delta[i] = activationderivative(inj) * (yj - aj)
			for l in range(network.layers-1, 0, -1)
				for node i in l:
					delta[i] = activationderivative(ini) * summation j network.w[i][j] * delta[j]
			for i in range(len(network.w)):
				for j in range(len(network.w[i])):
					network.w[i][j] = network.w[i][j] + (alpha * a[i] * delta[j])

		if stopCondition:
			break
	return network

'''
Output to class
'''
def outputToClass(outputMatrix):
	toReturn = []
	for row in outputMatrix:
		for i in range(len(row)):
			if row[i] == 1:
				toReturn.append(i+1)
	return toReturn


'''
Class to output
'''
def classOutput(classVector):
	toReturn = [[0 for col in range(3)] for row in range(len(classVector))]
	for i in range(len(classVector)):
		toReturn[i][classVector[i]-1] = 1
	return toReturn


'''
Activation function f(x)
Use hyperbolic tangent
'''
def activation(x):
	return (math.tanh(x) + 1)/2

'''
Derivative of activation function: f'(x)
(d/dx hyperbolic tangent)
'''
def dActivation(x):
	return (1 - (math.tanh(x)**2))/2

'''
apply activation function to a matrix
'''
def activate(matrixIn):
	toReturn = copy.deepcopy(matrixIn)
	return [[activation(col) for col in row] for row in toReturn]



#############################################
############### Application Program #########
class Application:
	def feedForward(self):
		pass

	def outputVectorToClass(self):
		pass


##############  RUN  ###############
'''
Run Neural Nets
'''
def Run():
	pass


'''
Boostrap
'''
if __name__ == "__main__":
	Run()
