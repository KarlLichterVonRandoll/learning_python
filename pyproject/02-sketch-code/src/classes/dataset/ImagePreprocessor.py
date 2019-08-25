"""
    图片数据预处理
"""
import os
import sys

import numpy as np
from PIL import Image
import cv2
from keras.preprocessing.image import ImageDataGenerator


class ImagePreprocessor:
    """
        数据预处理类
    """

    def __init__(self):
        pass

    # 创建图像数据集
    def build_image_dataset(self, data_input_folder, augment_data=True):
        print("Converting images from {} into arrays, augmentation: {}"
              .format(data_input_folder, augment_data))

        resized_img_arrays, sample_ids = self.get_resized_images(data_input_folder)

        if augment_data == 1:
            self.augment_and_save_images(resized_img_arrays, sample_ids, data_input_folder)
        else:
            self.save_resized_img_arrays(resized_img_arrays, sample_ids, data_input_folder)

    def save_resized_img_arrays(self, resized_img_arrays, sample_ids, output_folder):
        count = 0
        for img_arr, sample_id in zip(resized_img_arrays, sample_ids):
            npz_filename = "{}/{}.npz".format(output_folder, sample_id)
            np.savez_compressed(npz_filename, features=img_arr)
            retrieve = np.load(npz_filename)["features"]
            assert np.array_equal(img_arr, retrieve)
            count += 1
        print("Saved down {} resized images to folder {}".format(count, output_folder))
        del resized_img_arrays

    # 图像增强函数,用以生成一个batch的图像数据，支持实时数据提升
    def augment_and_save_images(self, resized_img_arrays, sample_ids, data_input_folder):
        # 使用keras中的图片生成器
        datagen = ImageDataGenerator(
            rotation_range=2,  # 整数，数据提升时图片随机转动的角度
            width_shift_range=0.05,  # 浮点数，图片宽度的某个比例，数据提升时图片水平偏移的幅度
            height_shift_range=0.05,  # 浮点数，图片高度的某个比例，数据提升时图片竖直偏移的幅度
            zoom_range=0.05  # 浮点数,随机缩放的幅度，若为浮点数，则相当于[lower,upper] = [1 - zoom_range, 1+zoom_range]
        )
        # 接收numpy数组和标签为参数,生成经过数据提升或标准化后的batch数据,并在一个无限循环中不断的返回batch数据
        keras_generator = datagen.flow(resized_img_arrays, sample_ids, batch_size=1)

        count = 0
        for i in range(len(resized_img_arrays)):
            img_arr, sample_id = next(keras_generator)
            img_arr = np.squeeze(img_arr)
            npz_filename = "{}/{}.npz".format(data_input_folder, sample_id[0])
            im = Image.fromarray(img_arr.astype('uint8'))
            np.savez_compressed(npz_filename, features=img_arr)
            retrieve = np.load(npz_filename)["features"]
            assert np.array_equal(img_arr, retrieve)
            count += 1
        print("Saved down {} augmented images to folder {}".format(count, data_input_folder))
        del resized_img_arrays

    # 获取处理好的图像
    def get_resized_images(self, pngs_input_folder):
        all_files = os.listdir(pngs_input_folder)

        png_files = [f for f in all_files if f.find(".png") != -1]

        images = []
        labels = []
        for png_file_path in png_files:
            png_path = "{}/{}".format(pngs_input_folder, png_file_path)

            sample_id = png_file_path[:png_file_path.find(".png")]

            resized_img_arr = self.resize_img(png_path)  # (256, 256, 3)
            images.append(resized_img_arr)
            labels.append(sample_id)  # labels 是对应的文件名

        return np.array(images), np.array(labels)

    # 图像处理函数
    def resize_img(self, png_file_path):
        # 读取图片rgb值, 返回数组
        img_rgb = cv2.imread(png_file_path)  # (1380, 2400, 3)
        # 将RGB图片转换为灰度图像
        img_grey = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)  # (1380, 2400)
        # 将图像二值化, 对应值 0 或 255
        img_adapted = cv2.adaptiveThreshold(img_grey, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                            cv2.THRESH_BINARY, 101, 9)  # (1380, 2400)

        img_stacked = np.repeat(img_adapted[..., None], 3, axis=2)  # (1380, 2400, 3)

        resized = cv2.resize(img_stacked, (200, 200), interpolation=cv2.INTER_AREA)  # (200, 200, 3)

        bg_img = 255 * np.ones(shape=(256, 256, 3))
        bg_img[27:227, 27:227, :] = resized
        bg_img /= 255

        return bg_img  # (256, 256, 3)
