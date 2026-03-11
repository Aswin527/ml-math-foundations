import random

'''
Linear Layer are core building block of neural network.
y = Wx + b

x = input vector
W = weight matrix
b = bias vector
y = output vector

'''

class LinearLayer:
    def __init__(self, input_size, output_size):
        # Initialize weights
        self.W = [[random.random() for _ in range(input_size)] 
                  for _ in range(output_size)]
        
        # Initialize bias
        self.b = [random.random() for _ in range(output_size)]

    def forward(self, x):
        output = []

        for i in range(len(self.W)):
            weighted_sum = 0
            
            for j in range(len(x)):
                weighted_sum += self.W[i][j] * x[j]

            weighted_sum += self.b[i]
            output.append(weighted_sum)

        return output


# Example
layer = LinearLayer(3, 2)

x = [1, 2, 3]  # input vector

y = layer.forward(x)

print("Output:", y)