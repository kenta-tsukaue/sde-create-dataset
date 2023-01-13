import pickle
import open3d as o3d
import numpy as np
import os

file_path = "../SDE結果/conv1d-6/iter_315000"
#file_path = "iter_50000"
#file_path = "../datas/point-cloud/point10/can2"

dir = os.listdir(file_path)
for file in dir:
    path = os.path.join(file_path, file)
    with open(path, 'rb') as f:
        pointData = np.load(f)
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
    
    #XとYとZの最大値からziku_maxを取得する
    print("======x======\n" + "最小値:" + str(x_min) + "\n最大値" + str(x_max))
    print("======y======\n" + "最小値:" + str(y_min) + "\n最大値" + str(y_max))
    print("======z======\n" + "最小値:" + str(z_min) + "\n最大値" + str(z_max))
    pointcloud1 = o3d.geometry.PointCloud()
    pointcloud1.points = o3d.utility.Vector3dVector(pointData)
    o3d.visualization.draw_geometries([pointcloud1])