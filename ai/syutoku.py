# -*- coding: utf-8 -*-

import os
#現在いるディレクトリを返す
current_dir = os.getcwd()
#次のファイルがあるかどうかを返す
os.path.exists('./myfile.png')
#ファイル名取得
filename = os.path.basename('./test/myfile.png')

#現ディレクトリ内の画像ファイルを行列に取り込む
import numpy as np
import cv2
T_train = np.zeros([50,10000])
i = 0
for x in os.listdir(current_dir + '/roboint/illust/test/'):
    if x[-4:] == '.png':
        a = cv2.imread(current_dir + '/roboint/illust/test/' + x)
        b = np.array(a)
        T[i,:] = b[:,:,0].reshape(10000)
        
print (T)

#globを使うと＊が使える
import glob
path_list = glob.glob('./test/*.jpg')

