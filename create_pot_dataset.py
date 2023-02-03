# -*- coding: utf-8 -*-
import numpy as np
import os
import pickle

dataset_path = "/public/tsukaue/graduation/sde-datas/data-voxel10-3"
save_path = "/public/tsukaue/graduation/sde-datas/data-voxel10-3-pot"

folder_list = os.listdir(dataset_path)

# 電荷からポテンシャルに変更
def chgtopot(chg,clamp=False):
  maxpixel = chg.shape[0]
  assert chg.shape[1]==maxpixel
  assert chg.shape[2]==maxpixel
  chgk = np.fft.fftn(chg)
  freq = np.fft.fftfreq(maxpixel)
  for kx in range(maxpixel):
    for ky in range(maxpixel):
      for kz in range(maxpixel):
        k2 = freq[kx]**2 + freq[ky]**2 + freq[kz]**2
        if abs(k2)<1e-5: continue
        chgk[kx,ky,kz] /= k2  
  pot = np.fft.ifftn(chgk).real
  if clamp:
    maxval = pot.max(); minval = pot.min()
    pot = (pot-minval) / (maxval-minval) * 255
  return pot

for folder in folder_list:
    folder_path = os.path.join(dataset_path, folder)
    data_list = os.listdir(folder_path)
    
    for file in data_list:
        file_path = os.path.join(folder_path, file)

        with open(file_path,'rb') as f1:
            tensor = np.load(f1, allow_pickle=True)
        
        #電荷からポテンシャルに変更
        tensor = chgtopot(tensor)

        #(-1:1の間に)正規化
        tensor = np.clip(tensor, -1, 1)

        #保存
        with open(save_path + "/" + folder + "/" + file[:-7] + ".ply","wb")as f:
            pickle.dump(tensor, f)

