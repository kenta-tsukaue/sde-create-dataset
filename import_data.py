
from kaolin.datasets import shapenet
from torch.utils.data import DataLoader

shapenet_dir = "/public/tsukaue/graduation/sde-datas/ShapeNetCore.v2"
meshes = shapenet.ShapeNet_Meshes(root=shapenet_dir, categories=['plane'])
voxels = shapenet.ShapeNet_Voxels(root=shapenet_dir, categories=['plane'])
points = shapenet.ShapeNet_Points(root=shapenet_dir, categories=['plane'])

print(meshes[0])
print(voxels[0])
print(points[0])