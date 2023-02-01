import pickle
import numpy as np
import os
import random

folder_path = "/public/tsukaue/graduation/sde-datas/voxel10-2/can"

file_list = os.listdir(folder_path)
print(len(file_list))
for file in file_list:
    print(file)
    """
    file_path = os.path.join(folder_path, file)
    with open(file_path,'rb') as f1:
        tensor = pickle.load(f1)
    
    with open(folder_path + "/c" + file[:-4]  + ".ply","wb")as f:
        pickle.dump(tensor, f)"""