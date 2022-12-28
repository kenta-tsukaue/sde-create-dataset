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
    print("頂点の数" + str(vertex.shape[0]))
    print("表面の数" + str(len(faces)))
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

            if(index % 1000 == 0):
                print(S)

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
    print("頂点の数" + str(vertex.shape[0]))
    print("表面の数" + str(len(faces)))
    if(vertex.shape[0] > 10000):
        print("増量後の頂点の数" + str(vertex.shape[0]))
        vertex = point_num_to_10000(vertex)
        print("修正後の頂点の数" + str(vertex.shape[0]))
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

            if(index % 1000 == 0):
                print(S)

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
        vertex = point_num_to_10000(vertex)
        print("修正後の頂点の数" + str(vertex.shape[0]))
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

#保存
def save_point(points, file_name):
    #print(points)
    with open(file_name,"wb")as f:
        pickle.dump(points, f)

#print(v)
#print(get_more_point(v, f))