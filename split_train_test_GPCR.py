import os
import numpy as np
import pickle
import random

path="/public/yasudak/tsukaue/GPCR/rot"
new_path = "/public/tsukaue/graduation/sde-datas/data-GPCR-1"
dir=os.listdir(path)

for ply in dir:
    file_path = os.path.join(path,ply)
    with open(file_path, 'rb') as f:
        pointData_list = pickle.load(f)
    pointData = pointData_list[0]

    for i in range(pointData.shape(0)):
        for j in range(pointData.shape(1)):
            for k in range(pointData.shape(2)):
                print(pointData[i][j][k])
    #次元の順番を変更
    pointData = pointData.transpose(3, 0, 1, 2)

    #ファイル名
    channel_file_path_train = "train/" + ply[:-7]+".npy"
    channel_file_path_test = "test/" + ply[:-7]+".npy"
    
    #どちらにも保存
    """
    file_path_train = os.path.join(new_path, channel_file_path_train)
    file_path_test = os.path.join(new_path, channel_file_path_test)
    with open(file_path_train,"wb") as f:
        pickle.dump(pointData,f)
    with open(file_path_test,"wb") as f:
        pickle.dump(pointData,f)"""