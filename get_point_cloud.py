import numpy as np
import random
import pickle


#テストデータ
#v = np.array([[0,0,0],[1,0,0],[1,1,0],[0,1,0],[0,0,1],[1,0,1],[1,1,1],[0,1,1]])
#f = [[1,2,5],[2,6,5],[2,6,7],[2,3,7],[3,8,7],[3,8,4],[4,8,1],[1,5,8],[5,8,7],[5,6,7],[1,2,4],[2,3,4]]


#絶対値を計算
def get_norm(vec):
    return np.linalg.norm(vec)


#面積に応じて三角形上に点を打つ

def get_more_point(vertex:np.array, faces:list):
    #print("頂点の数" + str(vertex.shape[0]))
    #print("表面の数" + str(len(faces)))
    if(vertex.shape[0] > 10000):
        print("増量後の頂点の数" + str(vertex.shape[0]))
        vertex = point_num_to_10000(vertex)
        return(vertex)
    else:
        for index, i in enumerate(faces):
            #三つの頂点を出す
            a = vertex[i[0]-1]
            b = vertex[i[1]-1]
            c = vertex[i[2]-1]

            #ベクトルにする
            vec_ab = b - a
            vec_ac = c - a

            #面積を出す
            #print(get_norm(vec_ab) ** 2 * get_norm(vec_ac) ** 2 - np.dot(vec_ab, vec_ac) ** 2)
            S = 0.5 * np.sqrt(get_norm(vec_ab) ** 2 * get_norm(vec_ac) ** 2 - np.dot(vec_ab, vec_ac) ** 2)

            #if(index % 1000 == 0):
            #    print(S)

            num = 0
            point_num = S * 1000

            #点を打つ()
            while num < point_num:
                s = random.random()
                t = random.random()
                if s + t <= 1:
                    point = a + s * vec_ab + t * vec_ac
                    vertex = np.concatenate([vertex, np.array([point])])
                    num += 1
        print("増量後の頂点の数" + str(vertex.shape[0]))
        return vertex

def get_10000_point(vertex:np.array, faces:list):
    #print("頂点の数" + str(vertex.shape[0]))
    #print("表面の数" + str(len(faces)))
    if(vertex.shape[0] > 10000):
        #print("増量後の頂点の数" + str(vertex.shape[0]))
        vertex = point_num_to_10000(vertex)
        #print("修正後の頂点の数" + str(vertex.shape[0]))
        return(vertex)
    else:
        for index, i in enumerate(faces):
            #三つの頂点を出す
            a = vertex[i[0]-1]
            b = vertex[i[1]-1]
            c = vertex[i[2]-1]

            #ベクトルにする
            vec_ab = b - a
            vec_ac = c - a

            #面積を出す
            #print(get_norm(vec_ab) ** 2 * get_norm(vec_ac) ** 2 - np.dot(vec_ab, vec_ac) ** 2)
            S = 0.5 * np.sqrt(get_norm(vec_ab) ** 2 * get_norm(vec_ac) ** 2 - np.dot(vec_ab, vec_ac) ** 2)
            #print(S)
            #if(index % 1000 == 0):
            #    print(S)

            num = 0
            point_num = S * 3000
            
            #print(86, point_num)
            #点を打つ()
            while num < point_num:
                s = random.random()
                t = random.random()
                if s + t <= 1:
                    point = a + s * vec_ab + t * vec_ac
                    vertex = np.concatenate([vertex, np.array([point])])
                    num += 1
        #print("増量後の頂点の数" + str(vertex.shape[0]))
        vertex = point_num_to_10000(vertex)
        #print("修正後の頂点の数" + str(vertex.shape[0]))
        return vertex

#ポイント数を10000にする
def point_num_to_10000(vertex):
    while vertex.shape[0] > 10000:
        max_num = vertex.shape[0] - 1
        #print(max_num)
        #0 ~ max_numまでの数をランダム採取
        delete_index_num = int(random.uniform(0, max_num))
        vertex = np.delete(vertex, delete_index_num, 0)
    return vertex

#点群を正規化する
def norm_point(vertex):
    # 最大値、最小値の更新
    #xの最大値と最小値を出す
    x_min = 0
    x_max = 0

    #yの最大値と最小値を出す
    y_min = 0
    y_max = 0

    #zの最大値と最小値を出す
    z_min = 0
    z_max = 0
    for i in vertex:
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
    #print("======x======\n" + "最小値:" + str(x_min) + "\n最大値" + str(x_max))
    #print("======y======\n" + "最小値:" + str(y_min) + "\n最大値" + str(y_max))
    #print("======z======\n" + "最小値:" + str(z_min) + "\n最大値" + str(z_max))
    ziku_max = x_max
    if ziku_max < abs(x_min):
        ziku_max = abs(x_min)
    if ziku_max < abs(y_min):
        ziku_max = abs(y_min)
    if ziku_max < y_max:
        ziku_max = y_max
    if ziku_max < z_max:
        ziku_max = z_max
    if ziku_max < abs(z_min):
        ziku_max = abs(z_min)
    #print("軸の最大は" + str(ziku_max))
    ratio = 1 / ziku_max

    return vertex * ratio

#保存
def save_point(points, file_name):
    #print(points)
    with open(file_name,"wb")as f:
        pickle.dump(points, f)

#print(v)
#print(get_more_point(v, f))