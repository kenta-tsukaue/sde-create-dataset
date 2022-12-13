import numpy as np
import os
import random
import pickle
import math
import matplotlib.pyplot as plt
import random

sde_datas_path = "/public/tsukaue/graduation/sde-datas/"
data_pointCloud_path = os.path.join(sde_datas_path, "data-pointCloud")
dir = os.listdir(data_pointCloud_path)

for o in dir:
    file_path = os.path.join(dir, o)
    try:
        with open(file_path, 'rb') as f:
            pointData = pickle.load(f)
    except FileNotFoundError:
        continue

    
    #pointcloud1 = o3d.geometry.PointCloud()
    #pointcloud1.points = o3d.utility.Vector3dVector(pointData)
    #o3d.visualization.draw_geometries([pointcloud1])

    #xの最大値と最小値を出す
    x_min = 0
    x_max = 0

    #yの最大値と最小値を出す
    y_min = 0
    y_max = 0

    #zの最大値と最小値を出す
    z_min = 0
    z_max = 0


    for i in pointData:

        if i[0] > x_max:
            x_max = i[0]
        elif i[0] < x_min:
            x_min = i[0]

        if i[1] > y_max:
            y_max = i[1]
        elif i[1] < y_min:
            y_min = i[1]

        if i[2] > z_max:
            z_max = i[2]
        elif i[2] < z_min:
            z_min = i[2]






    """XとYの最大値を取って一番大きい値から32を作成する"""
    print("======x======\n" + "最小値:" + str(x_min) + "\n最大値" + str(x_max))
    print("======y======\n" + "最小値:" + str(y_min) + "\n最大値" + str(y_max))
    ziku_max = x_max
    if ziku_max < abs(x_min):
        ziku_max = abs(x_min)
    if ziku_max < abs(y_min):
        ziku_max = abs(y_min)
    if ziku_max < y_max:
        ziku_max = y_max
    print("軸の最大は" + str(ziku_max))






    """ziku_maxからxとyの値を修正する"""
    ratio = 16 / ziku_max

    for i in pointData:
        i[0] = int(math.ceil(i[0] * ratio + 15))
        i[1] = int(math.ceil(i[1] * ratio + 15))
    # print(pointData)







    """Zを10等分する"""
    print("======z======\n" + "最小値:" + str(z_min) + "\n最大値" + str(z_max))

    z_range = z_max -z_min
    step = z_range / 10
    #step = math.floor(step * 1000) / 1000
    print("z方面の範囲は" + str(z_range))
    print("step幅は" + str(step))

    z_list = []

    for i in range(11):
        z = z_min + i * step
        #z_list.append(math.floor(z * 100) / 100)
        z_list.append(z)
    # print(z_list)






    """基本の画像の行列を作成"""
    standard_vector = []
    for i in range(32):
        standard_vector.append(0)
    standard_matrix = []
    for i in range(32):
        standard_matrix.append(standard_vector)
    standard_tensor = []
    for i in range(10):
        standard_tensor.append(standard_matrix)


    standard_tensor = np.array(standard_tensor)

    for i in pointData:
        x = int(i[0])
        y = int(i[1])
        #print(x, y, i[2])
        if i[2] >= z_list[0] and i[2] < z_list[1]:
            standard_tensor[0][x][y] += 1
        elif i[2] >= z_list[1] and i[2] < z_list[2]:
            standard_tensor[1][x][y] += 1
        elif i[2] >= z_list[2] and i[2] < z_list[3]:
            standard_tensor[2][x][y] += 1
        elif i[2] >= z_list[3] and i[2] < z_list[4]:
            standard_tensor[3][x][y] +=1
        elif i[2] >= z_list[4] and i[2] < z_list[5]:
            standard_tensor[4][x][y] +=1
        elif i[2] >= z_list[5] and i[2] < z_list[6]:
            standard_tensor[5][x][y] +=1
        elif i[2] >= z_list[6] and i[2] < z_list[7]:
            standard_tensor[6][x][y] +=1
        elif i[2] >= z_list[7] and i[2] < z_list[8]:
            standard_tensor[7][x][y] +=1
        elif i[2] >= z_list[8] and i[2] < z_list[9]:
            standard_tensor[8][x][y] +=1
        else:
            standard_tensor[9][x][y] +=1







    """それぞれの要素を 0 ~ 256 の範囲に収める"""
    temp=0
    for k in range(3):
        for i in range(32):
            s = standard_tensor[k][i]
            for j in range(32):
                p = s[j]
                if p > temp:
                    temp = p
    
    print(temp)
    standard_tensor = standard_tensor.astype(np.float32)
    standard_tensor = standard_tensor / temp * 256
    standard_tensor = standard_tensor.astype(np.int32)

    




    """それぞれのチャネルの内容を表示
    for i in range(10):
        print("==========================[" + str(i+1) + "チャネル目]=============================")
        for j in range(32):
            print(standard_tensor[i][j])
        print("=================================================================")

    """



    
    """3x32x32 => 32x32x3に変更"""
    standard_tensor = np.array(standard_tensor)
    standard_tensor = np.transpose(standard_tensor, (1, 2, 0))






    """トレーニング用と検証用に分けて保存する"""
    random_num = random.random()
    #ファイル名
    channel_file_path_train = "train_tensors" + o[:-4]+".npy"
    channel_file_path_test = "test_tensors" + o[:-4]+".npy"

    #パス名(/public/tsukaue/graduation/sde-datas/)
    channel_data_path = os.path.join(sde_datas_path, "data_channel_3") #ここのdata_channel_3をパラメータで受け取れるようにしたい
    
    if random_num <= 0.8:
        channel_file_path = os.path.join(channel_data_path, channel_file_path_train)
    else:
        channel_file_path = os.path.join(channel_data_path, channel_file_path_test)
    with open(channel_file_path,"wb") as f:
        pickle.dump(standard_tensor,f)


