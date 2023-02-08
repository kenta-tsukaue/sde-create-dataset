import os
import numpy as np
import pickle
import random

path="/public/yasudak/tsukaue/GPCR/rot"
new_path = "/public/tsukaue/graduation/sde-datas/data-GPCR-1"
dir=os.listdir(path)

for folder in dir:
    folder_path = os.path.join(path,folder)
    try:
        dir2=os.listdir(folder_path)
    except NotADirectoryError:
        continue
    for ply in dir2:
        file_path = os.path.join(folder_path,ply)
        with open(file_path, 'rb') as f:
            pointData = pickle.load(f)

        random_num = random.random()

        #ファイル名
        channel_file_path_train = "train/" + ply[:-4]+".npy"
        channel_file_path_test = "test/" + ply[:-4]+".npy"
        
        #どちらにも保存

        
        if random_num <= 0.8:
            channel_file_path = os.path.join(new_path, channel_file_path_train)
        else:
            channel_file_path = os.path.join(new_path, channel_file_path_test)
        with open(channel_file_path,"wb") as f:
            pickle.dump(pointData,f)
