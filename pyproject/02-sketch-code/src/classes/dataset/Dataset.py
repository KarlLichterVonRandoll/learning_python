import os
import numpy as np
import shutil
import hashlib
import pdb

from keras.preprocessing.text import Tokenizer, one_hot
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical

from classes.dataset.ImagePreprocessor import *

VOCAB_FILE = '../../vocabulary.vocab'
TRAINING_SET_NAME = "training_set"
VALIDATION_SET_NAME = "validation_set"
BATCH_SIZE = 64


class Dataset:
    def __init__(self, data_input_folder, test_set_folder=None):
        self.data_input_folder = data_input_folder
        self.test_set_folder = test_set_folder

    def split_datasets(self, validation_split):
        """
        # 切分数据集，设置训练集和验证集
        :param validation_split: 验证集数据百分比
        :return: 训练集文件夹相对路径、验证集文件夹相对路劲
        """
        sample_ids = self.populate_sample_ids()  # 得到所有.gui文件的文件名作为 id
        print("Total number of samples:", len(sample_ids))  # 1700

        train_set_ids, val_set_ids, shuffled_sampled_ids = self.get_all_id_sets(
            validation_split, sample_ids
        )
        training_path, validation_path = self.split_samples(train_set_ids, val_set_ids)

        return training_path, validation_path

    def split_samples(self, train_set_ids, val_set_ids):
        """
        把分好的数据集拷贝到各自的文件夹
        :param train_set_ids: 训练集数据id列表
        :param val_set_ids: 验证集数据id列表
        :return: 训练集文件夹相对路径、验证集文件夹相对路劲
        """
        training_path, validation_path = self.create_data_folders()
        self.copy_files_to_folder(train_set_ids, training_path)
        self.copy_files_to_folder(val_set_ids, validation_path)

        return training_path, validation_path

    def preprocess_data(self, training_path, validation_path, augment_training_data):
        """
        对图片数据预处理
        :param training_path: 训练集文件夹
        :param validation_path: 验证集文件夹
        :param augment_training_data:
        :return: None
        """
        train_img_preprocessor = ImagePreprocessor()
        train_img_preprocessor.build_image_dataset(training_path, augment_data=augment_training_data)
        val_img_preprocessor = ImagePreprocessor()
        val_img_preprocessor.build_image_dataset(validation_path, augment_data=0)

    def create_data_folders(self):
        """
        创建训练集和验证集文件夹
        :return: 训练集数据和验证集数据文件夹名，相对路径
        """
        training_path = "{}/{}".format(os.path.dirname(self.data_input_folder), TRAINING_SET_NAME)
        validation_path = "{}/{}".format(os.path.dirname(self.data_input_folder), VALIDATION_SET_NAME)

        self.delete_existing_folder(training_path)  # 如果存在同名的文件夹，就删了
        self.delete_existing_folder(validation_path)  # 如果存在同名的文件夹，就删了

        if not os.path.exists(training_path):
            os.makedirs(training_path)
        if not os.path.exists(validation_path):
            os.makedirs(validation_path)
        return training_path, validation_path  # ./training_set ./validation_set

    def copy_files_to_folder(self, sample_ids, output_folder):
        """
        # 拷贝文件到文件夹
        :param sample_ids: 对应的数据集
        :param output_folder: 保存数据的文件夹
        :return: None
        """
        copied_count = 0
        for sample_id in sample_ids:
            sample_id_png_path = "{}/{}.png".format(self.data_input_folder, sample_id)
            sample_id_gui_path = "{}/{}.gui".format(self.data_input_folder, sample_id)
            if os.path.exists(sample_id_png_path) and os.path.exists(sample_id_gui_path):
                output_png_path = "{}/{}.png".format(output_folder, sample_id)
                output_gui_path = "{}/{}.gui".format(output_folder, sample_id)
                shutil.copyfile(sample_id_png_path, output_png_path)
                shutil.copyfile(sample_id_gui_path, output_gui_path)
                copied_count += 1

        print("Moved {} files from {} to {}".format(copied_count, self.data_input_folder, output_folder))

    def delete_existing_folder(self, folder_to_delete):
        """
        # 删除已存在的文件夹
        :param folder_to_delete: 文件夹名
        :return: None
        """
        if os.path.exists(folder_to_delete):
            shutil.rmtree(folder_to_delete)
            print("Deleted existing folder:{}".format(folder_to_delete))

    def populate_sample_ids(self):
        """
        不知道这样处理是干嘛
        :return: 所有.gui文件的文件名组成的列表
        """
        all_sample_ids = []
        full_path = os.path.realpath(self.data_input_folder)
        for f in os.listdir(full_path):
            if f.find(".gui") != -1:
                file_name = f[:f.find(".gui")]
                if os.path.isfile("{}/{}.png".format(self.data_input_folder, file_name)):
                    all_sample_ids.append(file_name)
        return all_sample_ids

    def get_all_id_sets(self, validation_split, sample_ids):
        """
        把数据拆分成 训练集 和 验证集
        :param validation_split: 验证集所占的比率
        :param sample_ids: 所有的数据集
        :return: 训练集数据id列表，验证集数据id列表
        """
        np.random.shuffle(sample_ids)
        val_count = int(validation_split * len(sample_ids))
        train_count = len(sample_ids) - val_count
        print("Splitting datasets, training samples:{}, validation samples:{}".format(
            train_count, val_count
        ))
        train_set, val_set = self.split_paths(sample_ids, train_count, val_count)

        return train_set, val_set, sample_ids

    def split_paths(self, sample_ids, train_count, val_count):
        """
        切分数据集，并且保证验证集中数据互不相同
        :param sample_ids: 数据集列表
        :param train_count: 训练集数量
        :param val_count: 验证集数量
        :return: 训练集列表、验证集列表
        """
        train_set = []
        val_set = []
        hashes = []
        for sample_id in sample_ids:
            f = open("{}/{}.gui".format(self.data_input_folder, sample_id), 'r', encoding='utf-8')

            with f:
                chars = ""
                for line in f:
                    chars += line
                content_hash = chars.replace(" ", "").replace("\n", "")
                # 这里使用哈希算法将文件内容转化为哈希编码
                content_hash = hashlib.sha256(content_hash.encode('utf-8')).hexdigest()

                if len(val_set) == val_count:  # 如果验证集列表满了就把数据放入训练集列表中
                    train_set.append(sample_id)
                else:
                    is_unique = True
                    for h in hashes:  # 遍历这里的哈希列表，判断每个数据是否唯一
                        if h is content_hash:
                            is_unique = False
                            break

                    if is_unique:  # 如果数据是唯一的就放入验证集中
                        val_set.append(sample_id)
                    else:  # 否则，放入训练集
                        train_set.append(sample_id)
                # 每次完成上面操作，就在哈希列表中就增加数据，用于之后的判断
                hashes.append(content_hash)

        assert len(val_set) == val_count  # 如果验证集数据没有满，就触发异常

        return train_set, val_set
