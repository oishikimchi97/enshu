import numpy as np
import matplotlib.pyplot as plt

x = 0.6

Xs = []
errors = []


for _ in range(100):
    x = x - (4*x**3 - 3*x)/(12*x**2-3)
    error = 4*x**3 - 3*x
    Xs.append(x)
    errors.append(error)


errors = np.log(abs(np.array(errors)))
plt.plot(np.arange(1, 101), errors)
plt.title('Newton\'s method')
plt.xlabel('number of times to run')
plt.ylabel('error for logscale')
plt.show()
