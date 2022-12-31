import pickle
import open3d as o3d
import numpy as np
import os

file_path = "./iter_95000"
dir = os.listdir(file_path)
for file in dir:
    path = os.path.join(file_path, file)
    with open(path, 'rb') as f:
        pointData = np.load(f)
    pointcloud1 = o3d.geometry.PointCloud()
    pointcloud1.points = o3d.utility.Vector3dVector(pointData)
    o3d.visualization.draw_geometries([pointcloud1])