import glob, pickle
import numpy as np
import pyvista as pv
from pyvista import examples
from pymeshfix import MeshFix

#folder_path = "/Users/tsukauekenta/Downloads/voxel5/bottle/bottle9f50b2ddbcc2141cfa20324e30e0bf4040.ply"
folder_path ="/Users/tsukauekenta/Desktop/iter_50/sample1.np"

with open(folder_path,'rb') as f1:
  tensor = np.load(f1)
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
point_cloud.plot(opacity=val, render_points_as_spheres=True, point_size=40) # , rgba=True)
raise RuntimeError
