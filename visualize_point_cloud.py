import pickle
import open3d as o3d

file_path = "file_path"
with open(file_path, 'rb') as f:
        pointData = pickle.load(f)
pointcloud1 = o3d.geometry.PointCloud()
pointcloud1.points = o3d.utility.Vector3dVector(pointData)
o3d.visualization.draw_geometries([pointcloud1])