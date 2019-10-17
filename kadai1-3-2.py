import numpy as np
import matplotlib.pyplot as plt


g = np.array([0,0,0,1,0,0,0])

s=0.03
p=0.485
q=0.485

S = np.array([[s+p, p, 0, 0, 0, 0, 0],
              [q,   s, p, 0, 0, 0, 0],
              [0,   q, s, p, 0, 0, 0],
              [0,   0, q, s, p, 0, 0],
              [0,   0, 0, q, s, p, 0],
              [0,   0, 0, 0, q, s, p],
              [0,   0, 0, 0, 0, q, s+q]])

for t in range(1, 60+1):
    g = np.dot(S, g)
    print('{}second\n'.format(t), g)
