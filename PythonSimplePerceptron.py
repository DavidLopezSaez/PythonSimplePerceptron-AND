from Entry import Entry
from Threshold import Threshold
from Perceptron import Perceptron


perceptron = Perceptron()
print("Learned in: ", perceptron.get_iterations())
print("########################################")

while True:
    print("Enter first value: ", end = "")
    value1 = input()
    print("Enter second value: ", end = "")
    value2 = input()

    output = perceptron.get_output(value1, value2)
    print("Output: ", output)
    print("########################################")
