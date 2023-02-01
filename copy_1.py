import pickle
import numpy as np
import os
import random

folder_path = "/public/tsukaue/graduation/sde-datas/voxel10-2/can"

file_list = os.listdir(folder_path)

for file in file_list:
    file_path = os.path.join(folder_path, file)
    with open(file_path,'rb') as f1:
        tensor = pickle.load(f1)
    
    with open(folder_path + "/" + file[:-4] + "c" + ".ply","wb")as f:
        pickle.dump(tensor, f)