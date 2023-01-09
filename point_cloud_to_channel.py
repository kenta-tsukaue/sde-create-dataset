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
    file_path = os.path.join(data_pointCloud_path, o)
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






    """XとYとZの最大値を取って一番大きい値から32を作成する"""
    print("======x======\n" + "最小値:" + str(x_min) + "\n最大値" + str(x_max))
    print("======y======\n" + "最小値:" + str(y_min) + "\n最大値" + str(y_max))
    print("======z======\n" + "最小値:" + str(z_min) + "\n最大値" + str(z_max))
    ziku_max = x_max
    if ziku_max < abs(x_min):
        ziku_max = abs(x_min)
    if ziku_max < abs(y_min):
        ziku_max = abs(y_min)
    if ziku_max < y_max:
        ziku_max = y_max
    if ziku_max < abs(z_min):
        ziku_max = abs(z_min)
    if ziku_max < z_max:
        ziku_max = z_max
    print("軸の最大は" + str(ziku_max))






    """ziku_maxからxとyとzの値を修正する"""
    ratio = 16 / ziku_max

    for i in pointData:
        i[0] = int(math.ceil(i[0] * ratio + 15))
        i[1] = int(math.ceil(i[1] * ratio + 15))
        i[2] = int(math.ceil(i[2] * ratio + 15))
    # print(pointData)







    """Zを10等分する (zも上のコードで指定してあるので必要なし)
    print("======z======\n" + "最小値:" + str(z_min) + "\n最大値" + str(z_max))

    z_range = z_max -z_min
    step = z_range / 32
    #step = math.floor(step * 1000) / 1000
    print("z方面の範囲は" + str(z_range))
    print("step幅は" + str(step))

    z_list = []

    for i in range(32):
        z = z_min + i * step
        #z_list.append(math.floor(z * 100) / 100)
        z_list.append(z)
    # print(z_list)"""






    """基本の画像の行列を作成"""
    standard_vector = []
    for i in range(32):
        standard_vector.append(0)
    standard_matrix = []
    for i in range(32):
        standard_matrix.append(standard_vector)
    standard_tensor = []
    for i in range(32):
        standard_tensor.append(standard_matrix)


    standard_tensor = np.array(standard_tensor)

    for i in pointData:
        x = int(i[0])
        y = int(i[1])
        z = int(i[2])
        #追加
        standard_tensor[x][y][z] += 1
        """
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
        elif i[2] >= z_list[9] and i[2] < z_list[10]:
            standard_tensor[9][x][y] +=1
        elif i[2] >= z_list[10] and i[2] < z_list[11]:
            standard_tensor[10][x][y] +=1
        elif i[2] >= z_list[11] and i[2] < z_list[12]:
            standard_tensor[11][x][y] +=1
        elif i[2] >= z_list[12] and i[2] < z_list[13]:
            standard_tensor[12][x][y] +=1
        elif i[2] >= z_list[13] and i[2] < z_list[14]:
            standard_tensor[13][x][y] +=1
        elif i[2] >= z_list[14] and i[2] < z_list[15]:
            standard_tensor[14][x][y] +=1
        elif i[2] >= z_list[15] and i[2] < z_list[16]:
            standard_tensor[15][x][y] +=1
        elif i[2] >= z_list[16] and i[2] < z_list[17]:
            standard_tensor[16][x][y] +=1
        elif i[2] >= z_list[17] and i[2] < z_list[18]:
            standard_tensor[17][x][y] +=1
        elif i[2] >= z_list[18] and i[2] < z_list[19]:
            standard_tensor[18][x][y] +=1
        elif i[2] >= z_list[19] and i[2] < z_list[20]:
            standard_tensor[19][x][y] +=1
        elif i[2] >= z_list[20] and i[2] < z_list[21]:
            standard_tensor[20][x][y] +=1
        elif i[2] >= z_list[21] and i[2] < z_list[22]:
            standard_tensor[21][x][y] +=1
        elif i[2] >= z_list[22] and i[2] < z_list[23]:
            standard_tensor[22][x][y] +=1
        elif i[2] >= z_list[23] and i[2] < z_list[24]:
            standard_tensor[23][x][y] +=1
        elif i[2] >= z_list[24] and i[2] < z_list[25]:
            standard_tensor[24][x][y] +=1
        elif i[2] >= z_list[25] and i[2] < z_list[26]:
            standard_tensor[25][x][y] +=1
        elif i[2] >= z_list[26] and i[2] < z_list[27]:
            standard_tensor[26][x][y] +=1
        elif i[2] >= z_list[27] and i[2] < z_list[28]:
            standard_tensor[27][x][y] +=1
        elif i[2] >= z_list[28] and i[2] < z_list[29]:
            standard_tensor[28][x][y] +=1
        elif i[2] >= z_list[29] and i[2] < z_list[30]:
            standard_tensor[29][x][y] +=1
        elif i[2] >= z_list[30] and i[2] < z_list[31]:
            standard_tensor[30][x][y] +=1
        elif i[2] >= z_list[31] and i[2] < z_list[32]:
            standard_tensor[31][x][y] +=1
        elif i[2] >= z_list[32] and i[2] < z_list[33]:
            standard_tensor[32][x][y] +=1
        elif i[2] >= z_list[33] and i[2] < z_list[34]:
            standard_tensor[33][x][y] +=1
        elif i[2] >= z_list[34] and i[2] < z_list[35]:
            standard_tensor[34][x][y] +=1
        elif i[2] >= z_list[35] and i[2] < z_list[36]:
            standard_tensor[35][x][y] +=1
        elif i[2] >= z_list[36] and i[2] < z_list[37]:
            standard_tensor[36][x][y] +=1
        elif i[2] >= z_list[37] and i[2] < z_list[38]:
            standard_tensor[37][x][y] +=1
        elif i[2] >= z_list[38] and i[2] < z_list[39]:
            standard_tensor[38][x][y] +=1
        elif i[2] >= z_list[39] and i[2] < z_list[40]:
            standard_tensor[39][x][y] +=1
        elif i[2] >= z_list[40] and i[2] < z_list[41]:
            standard_tensor[40][x][y] +=1
        elif i[2] >= z_list[41] and i[2] < z_list[42]:
            standard_tensor[41][x][y] +=1
        elif i[2] >= z_list[42] and i[2] < z_list[43]:
            standard_tensor[42][x][y] +=1
        elif i[2] >= z_list[43] and i[2] < z_list[44]:
            standard_tensor[43][x][y] +=1
        elif i[2] >= z_list[44] and i[2] < z_list[45]:
            standard_tensor[44][x][y] +=1
        elif i[2] >= z_list[45] and i[2] < z_list[46]:
            standard_tensor[45][x][y] +=1
        elif i[2] >= z_list[46] and i[2] < z_list[47]:
            standard_tensor[46][x][y] +=1
        elif i[2] >= z_list[47] and i[2] < z_list[48]:
            standard_tensor[47][x][y] +=1
        elif i[2] >= z_list[48] and i[2] < z_list[49]:
            standard_tensor[48][x][y] +=1
        elif i[2] >= z_list[49] and i[2] < z_list[50]:
            standard_tensor[49][x][y] +=1
        elif i[2] >= z_list[50] and i[2] < z_list[51]:
            standard_tensor[50][x][y] +=1
        elif i[2] >= z_list[51] and i[2] < z_list[52]:
            standard_tensor[51][x][y] +=1
        elif i[2] >= z_list[52] and i[2] < z_list[53]:
            standard_tensor[52][x][y] +=1
        elif i[2] >= z_list[53] and i[2] < z_list[54]:
            standard_tensor[53][x][y] +=1
        elif i[2] >= z_list[54] and i[2] < z_list[55]:
            standard_tensor[54][x][y] +=1
        elif i[2] >= z_list[55] and i[2] < z_list[56]:
            standard_tensor[55][x][y] +=1
        elif i[2] >= z_list[56] and i[2] < z_list[57]:
            standard_tensor[56][x][y] +=1
        elif i[2] >= z_list[57] and i[2] < z_list[58]:
            standard_tensor[57][x][y] +=1
        elif i[2] >= z_list[58] and i[2] < z_list[59]:
            standard_tensor[58][x][y] +=1
        elif i[2] >= z_list[59] and i[2] < z_list[60]:
            standard_tensor[59][x][y] +=1
        elif i[2] >= z_list[60] and i[2] < z_list[61]:
            standard_tensor[60][x][y] +=1
        elif i[2] >= z_list[61] and i[2] < z_list[62]:
            standard_tensor[61][x][y] +=1
        elif i[2] >= z_list[62] and i[2] < z_list[63]:
            standard_tensor[62][x][y] +=1
        else:
            standard_tensor[63][x][y] +=1
        """






    """それぞれの要素を 0 ~ 256 の範囲に収める
    temp=0
    for k in range(64):
        for i in range(64):
            s = standard_tensor[k][i]
            for j in range(64):
                p = s[j]
                if p > temp:
                    temp = p
    
    print(temp)
    standard_tensor = standard_tensor.astype(np.float32)
    standard_tensor = standard_tensor / temp * 256
    standard_tensor = standard_tensor.astype(np.int32)
    """

    """それぞれの要素を 0 ~ 256 の範囲に収める"""
#    mean = standard_tensor.mean()
#    std = standard_tensor.std()
    mean = standard_tensor[standard_tensor>0].mean()
    std = standard_tensor[standard_tensor>0].std()
#    print(mean,std)
    standard_tensor = (standard_tensor - mean) / std *128 + 128
    standard_tensor[standard_tensor>255] = 255
    standard_tensor[standard_tensor<0] = 0
    standard_tensor = standard_tensor.astype(np.int32)
    print('range of standard_tensor=',standard_tensor.min(),standard_tensor.max())

    




    """それぞれのチャネルの内容を表示
    for i in range(64):
        print("==========================[" + str(i+1) + "チャネル目]=============================")
        for j in range(64):
            print(standard_tensor[i][j])
        print("=================================================================")
    """
    



    
    """3x32x32 => 32x32x3に変更
    standard_tensor = np.array(standard_tensor)
    standard_tensor = np.transpose(standard_tensor, (1, 2, 0))
    """





    """トレーニング用と検証用に分けて保存する"""
    random_num = random.random()
    #ファイル名
    channel_file_path_train = "train_tensors/" + o[:-4]+".npy"
    channel_file_path_test = "test_tensors/" + o[:-4]+".npy"

    #パス名(/public/tsukaue/graduation/sde-datas/)
    channel_data_path = os.path.join(sde_datas_path, "data-channel-64") #ここのdata_channel_3をパラメータで受け取れるようにしたい
    
    if random_num <= 0.8:
        channel_file_path = os.path.join(channel_data_path, channel_file_path_train)
    else:
        channel_file_path = os.path.join(channel_data_path, channel_file_path_test)
    with open(channel_file_path,"wb") as f:
        pickle.dump(standard_tensor,f)


