from __future__ import absolute_import

from keras.models import Model, Sequential, model_from_json
from keras.callbacks import ModelCheckpoint, CSVLogger, Callback
from keras.layers.core import Dense, Dropout, Flatten
from keras.layers import Embedding, GRU, TimeDistributed, RepeatVector, LSTM, concatenate, Input, Reshape, Dense
from keras.layers.convolutional import Conv2D
from keras.optimizers import RMSprop

# from .ModelUtils import *
from classes.dataset.Dataset import *

MAX_LENGTH = 48
MAX_SEQ = 150


class SketchCodeModel:
    def __init__(self, model_output_path, model_json_file=None, model_weight_file=None):
        # 创建模型输出路径
        self.model_output_path = model_output_path

        # 如果有训练好的模型就加载
        if model_weight_file is not None and model_json_file is not None:
            self.model = self.load_model(model_json_file, model_weight_file)
            optimizer = RMSprop(lr=0.0001, clipvalue=1.0)
            self.model.compile(loss='categorical_crossentropy', optimizer=optimizer)
            print("Loaded pretrained model from disk")
