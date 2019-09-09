# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
demo03_mfcc.py  mfcc矩阵
"""
import scipy.io.wavfile as wf
import python_speech_features as sf
import matplotlib.pyplot as mp
import numpy as np

# 读取音频的mfcc矩阵
sample_rate, sigs = wf.read(
    '../ml_data/speeches/training/apple/apple01.wav')
print(sample_rate, sigs.shape)
# 提取mfcc矩阵
mfcc = sf.mfcc(sigs, sample_rate)

mp.matshow(mfcc.T, cmap='gist_rainbow')
mp.show()
