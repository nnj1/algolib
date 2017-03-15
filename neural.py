from random import *
import math

# each neuron
class Neuron:
    def __init__(self):
        self.value = 0
        self.synpases = []
    def activate(self):
        # use sigmoid activation function
        return 1.0/(1.0+math.e**(-1.0*self.value))

class Brain:
  def __init__(self, density, layers):
    # Save parameters
    self.density = density
    self.layers = layers
    
    # Create neurons
    self.neurons = [[Neuron() for j in range(0, density)] for i in range(0, layers)]
    
    # Create synpases for each neuron
    for layer in self.neurons:
      for neuron in layer:
        for i in range(0, density):
          neuron.synpases.append(random())
    
  def train(self, inputs, output):
    # load up first layer with input
    for i,input in enumerate(inputs):
      self.neurons[0][i].value = input
    
    # fwd propagate
    prediction = self.fwd()
    
    # adjust weights
    while abs(prediction - output) > 0.000001:
      prediction = self.fwd()  
    
  def fwd(self):
    # begin propagation
    for i, layer in enumerate(self.neurons[:-1]):
      for j, neuron in enumerate(layer):
        for k in range(0, self.density):
          self.neurons[i + 1][k].value = neuron.activate() * neuron.synpases[k]
    
    # send back prediction
    prediction = 0
    for neuron in self.neurons[-1]:
      prediction = prediction + neuron.activate()*(sum(neuron.synpases)/len(neuron.synpases))
    return prediction
    
# test
brain = Brain(20,40)
brain.train([0,23,14,12,3], 4)
