# -*- coding: utf-8 -*-

#pip3 install tensorflow
#pip3 install keras      が必要
#python3 で実行

from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers import Dense, Dropout, Activation,Flatten
from keras.optimizers import Adam 
from keras.utils import np_utils
from keras.preprocessing.image import array_to_img, img_to_array, list_pictures, load_img
import numpy as np

#この場合は手書き文字がAかBかの二クラス分類
categories = ['A', 'B']
nb_classes = len(categories)
image_size = 10

def main():
    X_train = []
    y_train = []
    X_test = []
    y_test = []

    for picture in list_pictures('./roboint/moji/train/pos/'):
        img = img_to_array(load_img(picture, target_size=(image_size,image_size)))
        X_train.append(img)
        y_train.append(0)

    for picture in list_pictures('./roboint/moji/train/neg/'):
        img = img_to_array(load_img(picture, target_size=(image_size,image_size)))
        X_train.append(img)
        y_train.append(1)

    for picture in list_pictures('./roboint/moji/test/pos/'):
        img = img_to_array(load_img(picture, target_size=(image_size,image_size)))
        X_test.append(img)
        y_test.append(0)

    for picture in list_pictures('./roboint/moji/test/neg/'):
        img = img_to_array(load_img(picture, target_size=(image_size,image_size)))
        X_test.append(img)
        y_test.append(1)

    X_train = np.array(X_train)
    y_train = np.array(y_train)
    X_test = np.array(X_test)
    y_test = np.array(y_test)

    X_train = X_train.astype('float32')
    X_train = X_train /255.0
    X_test = X_test.astype('float32')
    X_test = X_test / 255.0
    y_train = np_utils.to_categorical(y_train,nb_classes)
    y_test = np_utils.to_categorical(y_test,nb_classes)

    # モデルを訓練し評価する    
    model = model_train(X_train, y_train)
    model_eval(model, X_test, y_test)
   
    #おまけ(テスト画像の予想を出力)
    """
    pre = model.predict(X_test)
    for i, p in enumerate(pre):
        y = p.argmax()
        print (categories[y])
    """

# モデルを構築
def build_model(in_shape):
    model = Sequential()
    model.add(Convolution2D(32, 3, 3, 
	border_mode='same',
	input_shape=in_shape))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Convolution2D(64, 3, 3, border_mode='same'))
    model.add(Activation('relu'))
    model.add(Convolution2D(64, 3, 3))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Flatten()) 
    model.add(Dense(512))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(nb_classes))
    model.add(Activation('softmax'))
    model.compile(loss='binary_crossentropy',
	optimizer='rmsprop',
	metrics=['accuracy'])
    return model

# モデルを訓練する
def model_train(X, y):
    model = build_model(X.shape[1:])
    model.fit(X, y, batch_size=32, nb_epoch=30, verbose=0)
    # モデルを保存する($pip3 install h5py が必要)
    #hdf5_file = "./image/class-model.hdf5"
    #model.save_weights(hdf5_file)
    return model

# モデルを評価する
def model_eval(model, X, y):
    score = model.evaluate(X, y, verbose=0)
    #print('loss=', score[0])
    print('accuracy=', score[1])

if __name__ == "__main__":
    main()


