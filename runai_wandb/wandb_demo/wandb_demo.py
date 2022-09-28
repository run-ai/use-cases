import tensorflow as tf
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers

## ***********
import wandb
from wandb.keras import WandbCallback
## ***********

list_of_gpus = tf.config.list_physical_devices('GPU')
if len(list_of_gpus) > 0:
    print(f"GPUs detected! {len(list_of_gpus)} GPUs being used")
else:
    print("no GPUs detected =(")

## ***********    
wandb.init(project="wandb-script")

wandb.config = {
  "learning_rate": 0.001,
  "epochs": 15,
  "batch_size": 128
}
## ***********

# Model / data parameters
num_classes = 10
input_shape = (28, 28, 1)

# Load the data and split it between train and test sets
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Scale images to the [0, 1] range
x_train = x_train.astype("float32") / 255
x_test = x_test.astype("float32") / 255
# Make sure images have shape (28, 28, 1)
x_train = np.expand_dims(x_train, -1)
x_test = np.expand_dims(x_test, -1)
print("x_train shape:", x_train.shape)
print(x_train.shape[0], "train samples")
print(x_test.shape[0], "test samples")


# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

model = keras.Sequential(
    [
        keras.Input(shape=input_shape),
        layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Flatten(),
        layers.Dropout(0.5),
        layers.Dense(num_classes, activation="softmax"),
    ]
)

model.summary()

opt = keras.optimizers.Adam(
    learning_rate=wandb.config['learning_rate'] ## ***********
)
model.compile(
    loss="categorical_crossentropy", 
    optimizer=opt, 
    metrics=["accuracy"]
)

model.fit(
    x_train,
    y_train, 
    validation_split=0.1, 
    batch_size=wandb.config['batch_size'], ## ***********
    epochs=wandb.config['epochs'], ## ***********
    callbacks=[WandbCallback()] ## ***********
)