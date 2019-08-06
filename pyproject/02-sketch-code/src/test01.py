from keras.preprocessing.text import Tokenizer
from keras.layers import Embedding, GRU, TimeDistributed, RepeatVector, LSTM, concatenate, Input, Reshape, Dense
from keras.layers.convolutional import Conv2D
from keras.models import Model, Sequential, model_from_json
from keras.layers.core import Dense, Dropout, Flatten


# with open("../vocabulary.vocab") as f:
#     text = f.read().splitlines()[0]
#
# tokenizer = Tokenizer(filters='', split=" ", lower=False)
# tokenizer.fit_on_texts([text])
# vocab_size = len(tokenizer.word_index) + 1
#
# print(vocab_size)
# print(tokenizer.word_docs)

image_model = Sequential()
image_model.add(Conv2D(16, (3, 3), padding='valid', activation='relu', input_shape=(256, 256, 3,)))
image_model.add(Conv2D(16, (3, 3), activation='relu', padding='same', strides=2))
image_model.add(Conv2D(32, (3, 3), activation='relu', padding='same'))
image_model.add(Conv2D(32, (3, 3), activation='relu', padding='same', strides=2))
image_model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
image_model.add(Conv2D(64, (3, 3), activation='relu', padding='same', strides=2))
image_model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
image_model.add(Flatten())
image_model.add(Dense(1024, activation='relu'))
image_model.add(Dropout(0.3))
image_model.add(Dense(1024, activation='relu'))
image_model.add(Dropout(0.3))
image_model.add(RepeatVector(48))
visual_input = Input(shape=(256, 256, 3,))

print(image_model.summary())
