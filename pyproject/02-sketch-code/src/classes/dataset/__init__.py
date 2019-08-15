import os
import shutil
import pdb
import hashlib
import numpy as np

from keras.preprocessing.text import Tokenizer, one_hot
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical

from classes.dataset.ImagePreprocessor import *

VOCAB_FILE = '../vocabulary.vocab'
TRAINING_SET_NAME = "training_set"
VALIDATION_SET_NAME = "validation_set"
BATCH_SIZE = 64