import numpy as np
import matplotlib.pyplot as plt



E_in_final = []
E_out_final = []
E_diff = []
p = 0.15

for i in range(1000):

    # Generate data
    X = np.random.uniform(-1,1,12)
    y = np.sign(X)
    for i in range(12):
        c = np.random.uniform(0,1,1)
        if c <= p:
            y *= -1

    # (1) Sort data
    newX = np.sort(X)
    E_in = 0

    # (2) Generate theta, s and Calculate E_in
    theta = np.random.uniform(-1, 1, 1)
    s = np.random.choice([-1, 1])

    # Calculate E_in
    for k in range(12):
        h1 = np.sign(newX[k] - theta) * s
        if h1 != y[k]:
            E_in += 1
    E_in = E_in / 12
    E_out = (0.5 - s * (0.5 - p)) + s * (0.5 - p) * abs(theta)
    E_in_final.append(E_in)
    E_out_final.append(E_out)
    E_diff.append(E_out - E_in)

print ("The median of E_out - E_in is ", np.median(E_diff))

plt.scatter(E_in_final, E_out_final)
plt.xlabel("E_in(g)")
plt.ylabel("E_out(g)")
plt.show()

