import glob, pickle
import numpy as np
import pyvista as pv
from pyvista import examples
from pymeshfix import MeshFix

#folder_path = "/Users/tsukauekenta/Downloads/voxel5/bowl/bowl4967063fc3673caa47fe6b02985fbd02747.ply"
#folder_path ="/Users/tsukauekenta/Library/Mobile Documents/com~apple~CloudDocs/研究/SDE結果/32x32x32_voxel5_3dConv_2/iter_15000/sample6.np"
folder_path = "/Users/tsukauekenta/Desktop/sofad851b8a016cf114c742f75bc7df727ae.npy"

with open(folder_path,'rb') as f1:
  tensor = pickle.load(f1)
print(tensor.shape)
points = []; val = []
tmax = tensor.max(); tmin = tensor.min()
print(tmax,tmin)
for ix in range(tensor.shape[0]):
  for iy in range(tensor.shape[1]):
    for iz in range(tensor.shape[2]):
      points.append((ix,iy,iz))
      val.append((tensor[ix,iy,iz]-tmin)/(tmax-tmin) * 0.5)
point_cloud = pv.PolyData(points)
point_cloud.plot(opacity=val, render_points_as_spheres=False, point_size=20) # , rgba=True)
raise RuntimeError
