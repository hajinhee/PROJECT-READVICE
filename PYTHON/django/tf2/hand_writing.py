import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras  # 이미지 처리는 keras
from tensorflow.python.tpu import datasets
import tensorflow as tf
from tensorflow.keras import datasets, layers, models


# 데이터는 init에 넣어준다.
class Solution:
    def __init__(self):
        self.mnist = keras.datasets.mnist

        (train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()
        train_images = train_images.reshape((60000, 28, 28, 1))  # (데이터, 이미지 높이, 이미지 높이, 컬러 채널)
        test_images = test_images.reshape((10000, 28, 28, 1))
        # 픽셀 값을 0~1 사이로 정규화합니다.
        self.train_images, self.test_images = train_images / 255.0, test_images / 255.0
        self.layers = layers
        self.model = models.Sequential()
        self.train_labels = train_labels

    def solution(self):
        self.modeling()
        self.training()

    def modeling(self):
        model = self.model
        model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Conv2D(64, (3, 3), activation='relu'))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Conv2D(64, (3, 3), activation='relu'))
        model.add(layers.Flatten())
        model.add(layers.Dense(64, activation='relu'))
        model.add(layers.Dense(10, activation='softmax'))

        # 모델의 구조 출력
        model.summary()

    def training(self):
        model = self.model
        model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])

        model.fit(self.train_images, self.train_labels, epochs=5)


if __name__ == '__main__':
    Solution().solution()
