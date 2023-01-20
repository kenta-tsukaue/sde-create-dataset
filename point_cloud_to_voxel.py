# -*- coding: utf-8 -*-
import open3d as o3d
import pickle
import numpy as np
import os
from PIL import Image
import pyvista as pv
from pyvista import examples
from pymeshfix import MeshFix


#point10_path = "/public/tsukaue/graduation/sde-datas/new-data-pointCloud-point10"
point10_path = "/Users/tsukauekenta/Downloads/new-data-pointCloud-pre"
save_path = "/Users/tsukauekenta/Downloads/voxel10/bathtub"
point10_dir = os.listdir(point10_path)
for folder in point10_dir:
    if folder != "bathtub":
        print("sofaじゃないのでスキップ")
        continue
    folder_path = os.path.join(point10_path, folder)
    try:
        dir = os.listdir(folder_path)
    except NotADirectoryError:
        continue
    
    max = 0
    for file in dir:
        point_cloud_path = os.path.join(folder_path, file)
        with open(point_cloud_path, 'rb') as f:
                points = pickle.load(f)
        # Separate the into points, colors and normals array

        # Initialize a point cloud object
        pcd = o3d.geometry.PointCloud()
        # Add the points, colors and normals as Vectors
        pcd.points = o3d.utility.Vector3dVector(points)

        # Create a voxel grid from the point cloud with a voxel_size of 0.01
        voxel_grid=o3d.geometry.VoxelGrid.create_from_point_cloud(pcd,voxel_size=0.05) #ちょっと多めに点を取る
        voxels = voxel_grid.get_voxels()
        indices = np.stack(list(vx.grid_index for vx in voxels))
        #print(indices)

        #=================x, y, zを中心化=============
        x_max = 0
        x_min = 0
        for i in indices:
            if i[0] > x_max:
                x_max = i[0]
            if i[0] < x_min:
                x_min = i[0]
        x_mid = (x_max - x_min) / 2 #xの中心
        x_midder = 20 - x_mid
        indices[0] = indices[0] + x_midder

        y_max = 0
        y_min = 0
        for i in indices:
            if i[1] > y_max:
                y_max = i[1]
            if i[1] < y_min:
                y_min = i[1]
        y_mid = (y_max - y_min) / 2 #xの中心
        y_midder = 20 - y_mid
        indices[1] = indices[1] + y_midder

        z_max = 0
        z_min = 0
        for i in indices:
            if i[2] > z_max:
                z_max = i[2]
            if i[2] < z_min:
                z_min = i[2]
        z_mid = (z_max - z_min) / 2 #xの中心
        z_midder = 20 - z_mid
        indices[2] = indices[2] + z_midder

         #==============Maxを出す===============
        max = 0
        for i in indices:
            #print(i)
            if i[0] > max:
                max = i[0]
            if i[1] > max:
                max = i[1]
            if i[2] > max:
                max = i[2]
        #Maxが32になるように正規化
        ratio = 31 / max
        indices = indices * ratio

        """基本のテンソル(32x32x32)を作成"""
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

        #基本全ての要素を128にする
        standard_tensor = standard_tensor + 128

        for i in indices:
            x = int(i[0])
            y = int(i[1])
            z = int(i[2])
            #追加
            standard_tensor[x][y][z] = 255

        #テンソルをテストで表示と画像を保存
        """
        for i in range(32):
            print("=====================[" + str(i+1) + "チャネル目]==================")
            for j in range(32):
                print(standard_tensor[i][j])
        
        
        input_batch = np.clip(standard_tensor, 0, 255).astype(np.uint8) #画像用に補正
        for i in range(32):
            Image.fromarray(input_batch[i]).save( save_path + "/" + file + "_channel" + str(i+1) + ".png")"""
        

        """=================== [ 保存 ] =================="""
        with open(save_path + "/" + file,"wb")as f:
            pickle.dump(standard_tensor, f)


        """=================== [表示] ==================
        points = []; val = []
        tmax = standard_tensor.max(); tmin = standard_tensor.min()
        print(tmax,tmin)
        for ix in range(standard_tensor.shape[0]):
            for iy in range(standard_tensor.shape[1]):
                for iz in range(standard_tensor.shape[2]):
                    points.append((ix,iy,iz))
                    val.append((standard_tensor[ix,iy,iz]-tmin)/(tmax-tmin) * 0.5)
        point_cloud = pv.PolyData(points)
        point_cloud.plot(opacity=val, render_points_as_spheres=False, point_size=15) # , rgba=True)
        """

        """===================================== [ 表示 ] ======================================
        # Initialize a visualizer object
        vis = o3d.visualization.Visualizer()
        # Create a window, name it and scale it
        vis.create_window(window_name='Bunny Visualize', width=800, height=600)

        # Add the voxel grid to the visualizer
        vis.add_geometry(voxel_grid)

        # We run the visualizater
        vis.run()
        # Once the visualizer is closed destroy the window and clean up
        vis.destroy_window()"""
        
    