import numpy as np
import matplotlib.pyplot as plt

x1 = 0.3
x2 = 0.9

Xs = []
errors = []


for _ in range(100):
    X = (x1+x2)/2
    error = 4*X**3-3*X
    Xs.append(X)
    errors.append(error)
    if error < 0:
        x1 = X
    else:
        x2 = X

errors = np.log(abs(np.array(errors)))
plt.title('Bisection method')
plt.plot(np.arange(1, 101), errors)
plt.xlabel('number of times to run')
plt.ylabel('error for logscale')
plt.show()
