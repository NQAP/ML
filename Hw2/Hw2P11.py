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
    E_in = 1000
    final_s = 0
    final_theta = 0

    # (2) Generate theta and Calculate E_in
    for j in range(12):
        E_in_theta = 0
        E_in_theta1 = 0
        E_in_theta0 = 0
        s = 0
        if j == 0:
            theta = -1
        else:
            theta = (newX[j-1] + newX[j]) / 2

        # Calculate E_in
        for k in range(12):
            h1 = np.sign(newX[k] - theta) * 1
            h2 = h1 * (-1)
            if h1 != y[k]:
                E_in_theta1 += 1
            if h2 != y[k]:
                E_in_theta0 += 1
        if E_in_theta0 < E_in_theta1:
            E_in_theta = E_in_theta0
            s = -1
        else:
            E_in_theta = E_in_theta1
            s = 1
        if E_in > E_in_theta:
            E_in = E_in_theta
            final_theta = theta
            final_s = s
    E_in = E_in / 12
    E_out = (0.5 - final_s * (0.5 - p)) + final_s * (0.5 - p) * abs(final_theta)
    E_in_final.append(E_in)
    E_out_final.append(E_out)
    E_diff.append(E_out - E_in)

print ("The median of E_out - E_in is ", np.median(E_diff))

plt.scatter(E_in_final, E_out_final)
plt.xlabel("E_in(g)")
plt.ylabel("E_out(g)")
plt.show()

