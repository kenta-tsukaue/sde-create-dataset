import os
import numpy as np
import get_point_cloud
path="/public/yasudak/tsukaue/data/ShapeNetCore.v2/"
dir=os.listdir(path)
for d in dir:
    print("===============================================================================================================")
    print("===============================================================================================================")
    print("==================================================" + d + "==================================================")
    print("===============================================================================================================")
    print("===============================================================================================================")
    file00=os.path.join(path,d)
    dir1=os.listdir(file00)
    for s in dir1:
        print("=============" + s + "=============")
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
            pointCloud = get_point_cloud.get_more_point(points, point3)
            print(pointCloud)
            #file04=os.path.join(file01,"models/model_normalized.ply")
            file04=("dataset/" + d + s + ".ply")
            get_point_cloud.save_point(pointCloud, file04)
        except FileNotFoundError:
            print("データがないのでスキップ")