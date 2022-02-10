from matplotlib.pyplot import imshow
import numpy as np
import cv2


from keras.preprocessing.image import img_to_array
import tensorflow as tf
from tensorflow.keras.layers import Input,Dense,Conv2D,MaxPooling2D,UpSampling2D
from tensorflow.keras.models import Sequential

SIZE = 256
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', padding='same', input_shape=(SIZE, SIZE, 3)))
model.add(MaxPooling2D((2, 2), padding='same'))
model.add(Conv2D(8, (3, 3), activation='relu', padding='same'))
model.add(MaxPooling2D((2, 2), padding='same'))
model.add(Conv2D(8, (3, 3), activation='relu', padding='same'))


model.add(MaxPooling2D((2, 2), padding='same'))

model.add(Conv2D(8, (3, 3), activation='relu', padding='same'))
model.add(UpSampling2D((2, 2)))
model.add(Conv2D(8, (3, 3), activation='relu', padding='same'))
model.add(UpSampling2D((2, 2)))
model.add(Conv2D(32, (3, 3), activation='relu', padding='same'))
model.add(UpSampling2D((2, 2)))
model.add(Conv2D(3, (3, 3), activation='relu', padding='same'))

model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])
model.summary()

img_data = []
img = cv2.imread('images/nishin.jpg',1)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img = cv2.resize(img, (SIZE,SIZE))
img_data.append(img_to_array(img))
img_array = np.reshape(img_data,(len(img_data), SIZE,SIZE,3))

img_array = img_array.astype('float32')/255.0

model.fit(img_array,img_array, epochs = 500,shuffle = True, verbose = 0)

pred = model.predict(img_array)

import matplotlib.pyplot as plt
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.imshow(img_array[0])
ax1.set_title('Original Image')
ax2.imshow(pred[0].reshape(SIZE,SIZE,3))
ax2.set_title('Deconstructed Image')

plt.tight_layout()


