from math import e
x = [
    [12,23],
    [21,34],
    [32,12],
    [18,42]
]
y = [
    [1],
    [0],
    [1],
    [0]
]

def sigmoid(x):
    return 1/(1 + e**(-x) )

w1,w2 = 0.1,0.01
b = 1
epochs = 10
for i in range(len(x)):
    z = (x[i][0] * w1 + x[i][1] * w2) + b

    res = sigmoid(z)

    loss = y[i][0] - res

    print(loss)

