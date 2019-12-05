import numpy as np
import matplotlib.pyplot as plt

N = 10  # set of nodes of the network
# np.random.seed(0)
x1 = np.random.randint(10, 90, size=N)
y1 = np.random.randint(10, 90, size=N)
ind = [i for i, v in enumerate(x1) if v < 40 or v > 60]
x, y = x1[ind], y1[ind]
N = len(x)
print(N)

x[0], x[-1] = 0, 100
y[0], y[-1] = 0, 100
fig = plt.figure(1, figsize=(16, 16))
plt.plot(x, y, 'ko', ms=16)
plt.plot(x[0], y[0], 'bs', ms=18)
plt.plot(x[-1], y[-1],'bs', ms=18)
fs = 16

for i in range(N):
    if i == 0:
        plt.text(x[i], y[i]+2, 'S', fontsize=fs)
    elif i == N-1:
        plt.text(x[i], y[i]+2, 'D', fontsize=fs)
    else:
        plt.text(x[i], y[i]+2, str(i), fontsize=fs)

source = [0]
dest = [N for N in range(1, N)]
w = [np.Infinity]*N
w[0] = 0
path = [-1]*N
path[0] = 0
loop = 0
# hop = 40
for hop in [40, 50, 60, 70, 80]:
    while True:
        for i in range(len(dest)):
            j = dest[i]
            d = []
            for k in range(len(source)):
                l = source[k]
                dist = np.sqrt((x[j] - x[l]) ** 2 + (y[j] - y[l]) ** 2)
                if dist > hop:
                    dist = np.Infinity
                    d.append(dist+w[l])
                    # print(d)
                    # print(source)
                    # print(w)
                    # print(path)
                    print('---------------------', [loop])
                    loop += 1
                if loop >= N-1:
                    break

        fig.savefig('hop = {}' .format(hop), dpi=300)