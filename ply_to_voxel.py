import pickle
import open3d as o3d
import numpy as np
import os

path = "../datas/point-cloud/point10/bag/bag4a1f62dbe8b091eabc49cae1a831a9e16.ply"
with open(path, 'rb') as f:
    pointData = pickle.load(f)

pcd = o3d.geometry.PointCloud()

#ポイントクラウドを表示
pcd.points = o3d.utility.Vector3dVector(pointData)
o3d.visualization.draw_geometries([pcd])

#ボクセル化
#voxel_grid=o3d.geometry.VoxelGrid.get_voxel(pointData)

voxel_grid=o3d.geometry.VoxelGrid.create_from_point_cloud(pcd,voxel_size=0.01)
print(voxel_grid.VoxelGrid)

vis = o3d.visualization.Visualizer()
# Create a window, name it and scale it
vis.create_window(window_name='Bunny Visualize', width=800, height=600)

# Add the voxel grid to the visualizer
vis.add_geometry(voxel_grid)

# We run the visualizater
vis.run()
# Once the visualizer is closed destroy the window and clean up
vis.destroy_window()