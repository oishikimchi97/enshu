import numpy as np
import matplotlib.pyplot as plt

#%%

N = np.arange(4, 10+1)
K = np.array(list(map(np.arange, N)))
ans = []

for k, n in zip(K, N):
    a = np.cos((2*k+1)*np.pi/(2*n))
    ans.append(a)

text = ["a{} = {}".format(j, ak) for j, ak in enumerate(ans[0])]
print(", ".join(text))

for i, an in enumerate(ans):
    print("T{}".format(i))
    print(an)
