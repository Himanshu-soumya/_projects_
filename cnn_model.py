# first part is to build teh model
#importing the Keras libraries and packages
# we importd teh necessary files
from keras.models import Sequential
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Convolution2D
from keras.layers import Dense, Dropout
from keras import optimizers

# we are initilizing the model cnn with a variable name calculator and assigning it to sequential
calculator = Sequential()

# 1 - step is to add a convolution layer with below parameters
calculator.add(Convolution2D(32, 3,  3, input_shape = (64, 64, 3), activation = 'relu'))

# 2 - step is to do Pooling after doing the convolution
calculator.add(MaxPooling2D(pool_size =(2,2)))

# then we are adding the second convolutuion layers
calculator.add(Convolution2D(32, 3,  3, activation = 'relu'))
calculator.add(MaxPooling2D(pool_size =(2,2)))

#after that we keep on adding teh convolution layers thsi si teh 3rd convolution layer
calculator.add(Convolution2D(64, 3,  3, activation = 'relu'))
calculator.add(MaxPooling2D(pool_size =(2,2)))


#3 - step is to to d flatttennnig g
calculator.add(Flatten())

#4 - step si to do full conmections
calculator.add(Dense(256, activation = 'relu'))
calculator.add(Dropout(0.5))
calculator.add(Dense(10, activation = 'softmax'))

#tehn we are compillong our model
calculator.compile(
              optimizer = 'adam',
              loss = 'categorical_crossentropy',
              metrics = ['accuracy'])
#after successfulling compilling ur model then we are going to sytart the 2nd part that si
# to fitting the cnn model  to the image
#Part 2 we are going to fit the cn to the image
#importing teh keras and teh other libraries
from keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)
# this is going to be the trainning the trainning set we are training our model to the data
# set in teh folder Data /train
training_set = train_datagen.flow_from_directory(
        'Data/train',
        target_size=(64, 64),
        batch_size=32,
        class_mode='categorical')
# after training comes teh testing part
test_set = test_datagen.flow_from_directory(
        'Data/test',
        target_size=(64, 64),
        batch_size=32,
        class_mode='categorical')

model = calculator.fit_generator(
        training_set,
        steps_per_epoch=100,
        epochs=100,
        validation_data = test_set,
        validation_steps = 6500
      )

#no we are going to save the model for that we are importing the h5py
import h5py
calculator.save('Trained_Model.h5')
print("our model is saved successfully ")
#our model will be saved as Trained_Model.h5
print(model.history.keys())
# we can also try to plot some graphs whic are o fno use i think
import matplotlib.pyplot as plt

# now that will summarize history for accuracy
plt.plot(model.history['acc'])
plt.plot(model.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

# that will summarize history for loss
plt.plot(model.history['loss'])
plt.plot(model.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()






