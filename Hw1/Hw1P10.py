import numpy as np
from sklearn.datasets import load_svmlight_file
import random
import matplotlib.pyplot as plt

X,y = load_svmlight_file("rcv1_train.binary")

X = X.toarray()
X = np.insert(X, 0, values=[1], axis=1)

xlength, ylength = X.shape

update = []
norm_w_i = []
for i in range(1000):
    N = 0
    w = np.zeros(ylength)
    updatetimes = 0
    norm_w = []
    while N < 1000:
        n = random.randrange(0, 199)
        x = np.array(X[n,:])
        h = w.T.dot(x)
        if np.sign(h) == 0:
            sig = -1
        else:
            sig = np.sign(h)
        if sig != y[n]:
            w += y[n]*x
            norm_w.append(np.linalg.norm(w))
            updatetimes += 1
            N = 0
        else:
            N += 1
    print(i)
    update.append(updatetimes)
    norm_w_i.append(norm_w)
print(norm_w_i)

print(update)

plt.figure(1)
T = min(update)
for i in range(1000):
    plt.plot(norm_w_i[i][0:T-1])
plt.xlabel("t")
plt.ylabel("Norm of w_t")

plt.figure(2)
plt.hist(update, bins=4)
plt.xlabel("Update times")
plt.ylabel("The numbers of the update times occurs")
plt.show()

