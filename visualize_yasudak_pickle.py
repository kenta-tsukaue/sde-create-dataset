import pickle
import numpy as np
import os
import random
import pyvista as pv
from pyvista import examples
from pymeshfix import MeshFix

file_path = "/Users/tsukauekenta/Downloads/bottle.pickle"

#リストの最大値を返す関数
def return_max(list):
    max = 0
    for i in list:
        if i > max:
            max=i
    if max > 0:
        max = 1
    return max

with open(file_path,'rb') as f1:
    tensordict = pickle.load(f1)

for key,tensor in tensordict.items():
    print(key,tensor[0].shape, tensor[1].shape)
    standard_vector = []
    for i in range(32):
        standard_vector.append(0)
    standard_matrix = []
    for i in range(32):
        standard_matrix.append(standard_vector)
    standard_tensor = []
    for i in range(32):
        standard_tensor.append(standard_matrix)
    pre_tensor = tensor[0]
    standard_tensor = np.array(standard_tensor)
    new_tensor = standard_tensor

    for i in range(32):
        for j in range(32):
            for k in range(32):
                list = [pre_tensor[2*i][2*j][2*k], pre_tensor[2*i][2*j][2*k+1], pre_tensor[2*i][2*j+1][2*k], pre_tensor[2*i][2*j+1][2*k+1],  \
                    pre_tensor[2*i+1][2*j][2*k], pre_tensor[2*i+1][2*j][2*k+1], pre_tensor[2*i+1][2*j+1][2*k], pre_tensor[2*i+1][2*j+1][2*k+1]]
                print(list)
                new_tensor[i][j][k] = return_max(list)

    #print(tensor.shape)
    points = []; val = []
    tmax = new_tensor.max(); tmin = new_tensor.min()
    print(tmax,tmin)
    for ix in range(new_tensor.shape[0]):
        for iy in range(new_tensor.shape[1]):
            for iz in range(new_tensor.shape[2]):
                points.append((ix,iy,iz))
                val.append((new_tensor[ix,iy,iz]-tmin)/(tmax-tmin) * 0.5)
    point_cloud = pv.PolyData(points)
    point_cloud.plot(opacity=val, render_points_as_spheres=False, point_size=15) # , rgba=True)