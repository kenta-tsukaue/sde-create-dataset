import os
import numpy as np
import pickle
import random

path="/public/tsukaue/graduation/sde-datas/data-point-10000_pre"
new_path = "/public/tsukaue/graduation/sde-datas/data-point-10000"
dir=os.listdir(path)

for ply in dir:
    file_path = os.path.join(path,ply)
    with open(file_path, 'rb') as f:
        pointData = pickle.load(f)
    
    random_num = random.random()

    #ファイル名
    channel_file_path_train = "train_tensors/" + ply[:-4]+".npy"
    channel_file_path_test = "test_tensors/" + ply[:-4]+".npy"

    if random_num <= 0.8:
        channel_file_path = os.path.join(new_path, channel_file_path_train)
    else:
        channel_file_path = os.path.join(new_path, channel_file_path_test)
    with open(channel_file_path,"wb") as f:
        pickle.dump(pointData,f)
