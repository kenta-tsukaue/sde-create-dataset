import os
import numpy as np
import get_point_cloud
import random

path="/public/yasudak/tsukaue/data/ShapeNetCore.v2/"
save_path="/public/tsukaue/graduation/sde-datas/new-data-pointCloud/"
dir=os.listdir(path)
for d in dir:
    folder_name = ""
    print("項目は", d)
    if(d!="sofa" and d!="cellPhone" and d!="box" and d!="cap" and d!="bench" and d!="bottle" and d!="bowl" and d!="can" and d!="bag" and d!="bathtub"):
        print("スキップ")
        continue
    folder_name = d
    
    file00=os.path.join(path,d)
    dir1=os.listdir(file00)
    print("ファイル名は", folder_name)
    save_path_folder = os.path.join(save_path,folder_name)
    save_path_folder_listdir = os.listdir(save_path_folder)
    print("この項目の現在のファイルの数は", len(save_path_folder_listdir))
    while len(save_path_folder_listdir) < 6100:
        print("もう一周行います")
        for s in dir1: 
            if len(save_path_folder_listdir) >= 6100:
                print("この項目はデータ数6100に達したので生成は行いません")
                continue
            #print("=============" + s + "=============")
            file01=os.path.join(file00,s)
            file02=os.path.join(file01,"models/model_normalized.obj")
            objFilePath = file02
            try:
                with open(objFilePath) as file:
                    points = []
                    points2 =[]
                    point3 = []
                    while 1:
                        line = file.readline()
                        if not line:
                            break
                        strs = line.split(" ")
                        if strs[0] == "v":
                            points.append((float(strs[1]), float(strs[2]), float(strs[3])))
                        if strs[0] == "f":
                            points2.append((strs[2],strs[3],strs[4]))
                points = np.array(points)
                #print(points)

                for a in points2:
                    s1=a[0].split("/")[0]
                    s2=a[1].split("/")[0]
                    s3=a[2].split("/")[0]
                    point3.append([int(s1),int(s2),int(s3)])
                #point3 = np.array(point3)
                pointCloud = get_point_cloud.get_10000_point(points, point3)
                
                #print("point数", pointCloud.shape[0])
                if(pointCloud.shape[0] < 10000):
                    print("ポイント数が足りないので保存しません")
                else:
                    pointCloud = get_point_cloud.norm_point(pointCloud)
                    #file04=os.path.join(file01,"models/model_normalized.ply")
                    #ランダムで2桁の数字を生成
                    random_num = str(int(random.random() * 100))
                    file04="/public/tsukaue/graduation/sde-datas/new-data-pointCloud/" + folder_name + "/" + d + s + random_num +".ply"
                    get_point_cloud.save_point(pointCloud, file04)
                    #ファイル数を更新
                    save_path_folder_listdir = os.listdir(save_path_folder)
                    print("現在のファイル数は", len(save_path_folder_listdir))
            
            except FileNotFoundError:
                print("データがないのでスキップ")