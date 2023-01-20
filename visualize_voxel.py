import glob, pickle
import numpy as np
import pyvista as pv
from pyvista import examples
from pymeshfix import MeshFix

#folder_path = "/Users/tsukauekenta/Downloads/voxel5/bowl/bowl4967063fc3673caa47fe6b02985fbd02747.ply"
folder_path ="/Users/tsukauekenta/Library/Mobile Documents/com~apple~CloudDocs/研究/SDE結果/32x32x32_voxel5_3dConv_2/iter_775000/sample1.np"
#folder_path = "/Users/tsukauekenta/Desktop/washingMachine360e2cb74c9c4d38df3a1b0d597ce76e.npy"
#folder_path = "/Users/tsukauekenta/Library/Mobile Documents/com~apple~CloudDocs/研究/datas/point-cloud/box1eb3abf47be2022381faebbdea6bd9be4042.ply"

with open(folder_path,'rb') as f1:
  tensor = np.load(f1)
tensor = np.clip(np.array(tensor) * 255, 0, 255)
#print(tensor)

for i in range(32):
  print("=====================[", i+1, "チャネル]====================")
  for j in range(32):
    print(tensor[i][j])

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
point_cloud.plot(opacity=val, render_points_as_spheres=False, point_size=15) # , rgba=True)
raise RuntimeError
