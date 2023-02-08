import numpy as np
import matplotlib.pyplot as plt
import random

# 初期位置
x, y = [0], [0]
plt.scatter(0, 0, color="blue")
for i in range(50):
    x_start = random.random() * 10000
    y_start = random.random() * 10000
    plt.scatter(x_start, y_start, color="blue")

# 時間移動量のシミュレーション
delta_t = 0.01
for k in range (1000):
    x, y = [0], [0]
    for i in range(4000):
        dx = (0.5*(i-1))*delta_t + 0.5 * (i-1) * np.sqrt(delta_t) * np.random.normal()
        dy = (0.5*(i-1))*delta_t + 0.5 * (i-1) * np.sqrt(delta_t) * np.random.normal()
        x.append(x[-1] + dx)
        y.append(y[-1] + dy)
    # 点の位置の可視化
    plt.scatter(x[-1], y[-1], color="red")

plt.show()
