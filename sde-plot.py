import numpy as np
import matplotlib.pyplot as plt

def sde_solver(diffusion_coefficient, t_max, n_points):
    dt = t_max / n_points
    t = np.linspace(0, t_max, n_points + 1)
    X = np.zeros(n_points + 1)
    X[0] = 1
    for i in range(1, n_points + 1):
        X[i] = X[i - 1] + (0.5*(i-1))*dt + diffusion_coefficient * (i-1) * np.sqrt(dt) * np.random.normal() #W[i]
    return t, X

t_max = 1
n_points = 1000
diffusion_coefficient = 0.5
t, X = sde_solver(diffusion_coefficient, t_max, n_points)
for i in range(10):
    t, X_temp = sde_solver(diffusion_coefficient, t_max, n_points)
    plt.plot(t, X_temp)
t, X_no_diffusion = sde_solver(0, t_max, n_points)
plt.plot(t, X_no_diffusion, linewidth=4, label='No Diffusion')
plt.legend()
plt.show()