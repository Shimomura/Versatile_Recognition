# -*- coding: utf-8 -*-

import classify
import sys, os
import numpy as np

# コマンドラインからファイル名を得る
if len(sys.argv) <= 1:
    print("check.py (ファイル名)")
    quit()

image_size = 10
categories = ['A','B']

# 入力画像をNumpyに変換
X_real = []
for fname in sys.argv[1:]:
    img = img_to_array(load_img(picture, target_size=(image_size,image_size)))
    X_real.append(img)
X_real = np.array(X_real)
X_real = X_real.astype('float32')
X_real = X_real / 255.0

# CNNのモデルを構築(hdf5に保存していた場合)
model = classify.build_model(X.shape[1:])
model.load_weights("./image/class-model.hdf5")

# データを予測
pre = model.predict(X_real)
for i, p in enumerate(pre):
    y = p.argmax()
    print (categories[y])

