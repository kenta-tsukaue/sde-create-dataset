import open3d as o3d
import pickle
import numpy as np
import os
point10_path = "/public/tsukaue/graduation/sde-datas/new-data-pointCloud-point10"
point10_dir = os.listdir(point10_path)
for folder in point10_dir:
    folder_path = os.path.join(point10_path, folder)
    dir = os.listdir(folder_path)
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
        voxel_grid=o3d.geometry.VoxelGrid.create_from_point_cloud(pcd,voxel_size=0.08)
        voxels = voxel_grid.get_voxels()
        indices = np.stack(list(vx.grid_index for vx in voxels))
        #print(indices[0])
        max = 0
        for i in indices:
            #print(i)
            if i[0] > max:
                max = i[0]
            if i[1] > max:
                max = i[1]
            if i[2] > max:
                max = i[2]

    print(folder + "の最大値は" + str(max)+ "です")

    """
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