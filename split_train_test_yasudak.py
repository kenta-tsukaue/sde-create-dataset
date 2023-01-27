import pickle
import numpy as np
import os
import random
import pyvista as pv
from pyvista import examples
from pymeshfix import MeshFix

folder_path = "/public/yasudak/tsukaue/sde-create-dataset/dataset"
new_path = "/public/tsukaue/graduation/sde-datas/data-yasudak-2"
#folder_path = "../datas/yasudak_0.1/airplane2.pickle" (テスト用)
#folder_path = "/Users/tsukauekenta/Downloads/yasudak-data"
#save_path = "/Users/tsukauekenta/Downloads/voxel10/car"
file_list = os.listdir(folder_path)

#リストの最大値を返す関数
def return_max(list):
  max = 0
  for i in list:
    if i > max:
      max=i
  if max > 0:
    max = 1
  return max

for file in file_list:
  print("項目名:", file)
  if file == ".DS_Store":
    continue
  file_path = os.path.join(folder_path, file)
  with open(file_path,'rb') as f1:
    tensordict = pickle.load(f1)

  for key,tensor in tensordict.items():
    #print(key,tensor[0].shape, tensor[1].shape)

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
          new_tensor[i][j][k] = return_max(list)

    """===================保存==================
    with open(new_path + "/" + file[:-7] + key + ".ply","wb")as f:
        pickle.dump(new_tensor, f)
    """
    """[表示]
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
    """

    """[保存]"""
    random_num = random.random()
    #ファイル名
    channel_file_path_train = "train/" +file[:-7]+ key +".npy"
    channel_file_path_test = "test/" +file[:-7]+ key +".npy"

    if random_num <= 0.8:
        channel_file_path = os.path.join(new_path, channel_file_path_train)
    else:
        channel_file_path = os.path.join(new_path, channel_file_path_test)
    with open(channel_file_path,"wb") as f:
        pickle.dump(new_tensor,f)
    

