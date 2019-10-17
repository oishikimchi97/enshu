import numpy as np
import matplotlib.pyplot as plt

t = 60
g = np.array([1, 0, 0, 0, 0, 0, 0])
data = [g]

s = 0.03
p = 0.485
q = 0.485

S = np.array([[s + p, p, 0, 0, 0, 0, 0],
              [q, s, p, 0, 0, 0, 0],
              [0, q, s, p, 0, 0, 0],
              [0, 0, q, s, p, 0, 0],
              [0, 0, 0, q, s, p, 0],
              [0, 0, 0, 0, q, s, p],
              [0, 0, 0, 0, 0, q, s + q]])
print(S)  # Sの値を確認

for _ in range(t):
    g = np.dot(S, g)
    data.append(g)

print(np.array(data))
data = zip(*data)

for i, g in enumerate(data):
    plt.plot(range(t + 1), g, label="place{}".format(i))

plt.title("The butterfly stochastic process")
plt.legend(loc="upper right")
plt.xlabel("Time")
plt.ylabel("Probability")
plt.grid()
plt.show()
