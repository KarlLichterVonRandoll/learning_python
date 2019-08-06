#!/usr/bin/env python
from __future__ import print_function
from __future__ import absolute_import

# 命令行参数解析模块
from argparse import ArgumentParser

from classes.model.SketchCodeModel import *

VAL_SPLIT = 0.2


def build_parser():
    parser = ArgumentParser()
    # 添加参数：输入数据路径
    parser.add_argument('--data_input_path', type=str,
                        dest='data_input_path', help='directory containing images and guis',
                        required=True)
    # 添加参数：验证集划分，默认 0.2
    parser.add_argument('--validation_split', type=float,
                        dest='validation_split', help='portion of training data for validation set',
                        default=VAL_SPLIT)
    # 添加参数：训练轮数
    parser.add_argument('--epochs', type=int,
                        dest='epochs', help='number of epochs to train on',
                        required=True)
    # 添加参数：模型输出路径
    parser.add_argument('--model_output_path', type=str,
                        dest='model_output_path', help='directory for saving model data',
                        required=True)
    # 添加参数：模型json格式文件
    parser.add_argument('--model_json_file', type=str,
                        dest='model_json_file', help='pretrained model json file',
                        required=False)
    # 添加参数：模型权重文件
    parser.add_argument('--model_weights_file', type=str,
                        dest='model_weights_file', help='pretrained model weights file',
                        required=False)
    # 添加参数：训练数据参数，默认为 1
    parser.add_argument('--augment_training_data', type=int,
                        dest='augment_training_data', help='use Keras image augmentation on training data',
                        default=1)
    return parser


def main():
    parser = build_parser()  # 添加参数解析对象
    options = parser.parse_args()  # 添加参数
    data_input_path = options.data_input_path  # 输入数据
    validation_split = options.validation_split  # 验证集划分
    epochs = options.epochs  # 训练轮数
    model_output_path = options.model_output_path  # 模型输出路径
    model_json_file = options.model_json_file  # 模型的json格式文件
    model_weights_file = options.model_weights_file  # 模型的权重文件
    augment_training_data = options.augment_training_data  # 增加训练数据

    # 加载模型
    model = SketchCodeModel(model_output_path, model_json_file, model_weights_file)

    # Create the model output path if it doesn't exist
    if not os.path.exists(model_output_path):
        os.makedirs(model_output_path)

    # Split the datasets and save down image arrays
    training_path, validation_path = ModelUtils.prepare_data_for_training(data_input_path, validation_split,
                                                                          augment_training_data)

    # Begin model training
    model.train(training_path=training_path,
                validation_path=validation_path,
                epochs=epochs)


if __name__ == "__main__":
    main()
