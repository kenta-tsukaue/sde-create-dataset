import pickle
import numpy as np
import os
import random

folder_path = "/public/yasudak/tsukaue/sde-create-dataset/dataset"
new_path = "/public/tsukaue/graduation/sde-datas/data-yasudak-1"
#folder_path = "../datas/yasudak_0.1/airplane2.pickle" (テスト用)
file_list = os.listdir(folder_path)


for file in file_list:
  print("項目名:", file)
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
    new_tensor = standard_tensor
    
    for i in range(32):
      for j in range(32):
        for k in range(32):
          sum = pre_tensor[2*i][2*j][2*k] + pre_tensor[2*i][2*j][2*k+1] + pre_tensor[2*i][2*j+1][2*k] + pre_tensor[2*i][2*j+1][2*k+1]  \
              + pre_tensor[2*i+1][2*j][2*k] + pre_tensor[2*i+1][2*j][2*k+1] + pre_tensor[2*i+1][2*j+1][2*k] + pre_tensor[2*i+1][2*j+1][2*k+1]
          new_tensor[i][j][k] = sum/8


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


