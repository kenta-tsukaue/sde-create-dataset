import pickle
import numpy as np
import os
import random
import pyvista as pv
from pyvista import examples
from pymeshfix import MeshFix

file_path = "/Users/tsukauekenta/Downloads/タンパク質/6vms_R.pickle"

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
    tensor = pickle.load(f1)
    tensor = np.array(tensor[0])
    print(tensor.shape)

    new_tensor = tensor
    final_tensor = new_tensor
    print(tensor.shape)
    points = []; val = []
    tmax = new_tensor.max(); tmin = new_tensor.min()
    print(tmax,tmin)
    """正規化"""
    for ix in range(new_tensor.shape[0]):
        for iy in range(new_tensor.shape[1]):
            for iz in range(new_tensor.shape[2]):
                points.append((ix,iy,iz))
                val.append((new_tensor[ix,iy,iz]-tmin)/(tmax-tmin) * 0.5)
                #val.append(new_tensor[ix,iy,iz])
    print("ポイント", np.array(points).shape)
    print("val",np.array(val).shape)

    points = np.array(points)
    val = np.array(val)

    #マスク
    mask = np.any(val != [0,0,0], axis=1)
    filtered_points = points[mask]
    filtered_colors = val[mask]

    


    
    point_cloud = pv.PolyData(filtered_points)
    point_cloud["colors"]=filtered_colors

    p = pv.Plotter()
    p.add_mesh(point_cloud, point_size=20)
    p.show()