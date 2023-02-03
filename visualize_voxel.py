import glob, pickle
import numpy as np
import pyvista as pv
from pyvista import examples
from pymeshfix import MeshFix
import os

folder_path = "/Users/tsukauekenta/Library/Mobile Documents/com~apple~CloudDocs/研究/datas/voxel10-3-pot"
file_list = os.listdir(folder_path)

def pottochg(pot):
  maxpixel = pot.shape[0]
  assert pot.shape[1]==maxpixel
  assert pot.shape[2]==maxpixel
  potk = np.fft.fftn(pot)
  freq = np.fft.fftfreq(maxpixel)
  for kx in range(maxpixel):
    for ky in range(maxpixel):
      for kz in range(maxpixel):
        k2 = freq[kx]**2 + freq[ky]**2 + freq[kz]**2
        if abs(k2)<1e-5: continue
        potk[kx,ky,kz] *= k2  
  chg = np.fft.ifftn(potk).real
  return chg

for file in file_list:
  if file == ".DS_Store":
    continue

  file_path = os.path.join(folder_path, file)
  with open(file_path,'rb') as f1:
    tensor = np.load(f1, allow_pickle=True)
  
  #print(tensor)

  tensor = pottochg(tensor)
  #tensor = np.clip(np.array(tensor) * 255, 0, 255)

  for i in range(32):
    print("=====================[", i+1, "チャネル]====================")
    for j in range(32):
      print(tensor[i][j])

  #print(tensor.shape)
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
  
