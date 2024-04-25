import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import SimpleRNN, Dense

# Veri setini yükle / Load dataset
data = pd.read_csv('dataset/path')

# Girdi ve çıktı verilerini ayır / Separate to input and output
x = data.drop(columns=['label']).values
y = data['label'].values

# Veri setini eğitim ve test setlerine ayır / Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# RNN için girdi şeklini düzenle / Edit input shape for RNN
n_steps = 1  # Örnek başına zaman adımlarının sayısı / Number of time steps per sample
n_features = 1  # Her bir zaman adımındaki özellik sayısı / Number of features in each time step
x_train = x_train.reshape((x_train.shape[0], n_steps, n_features))
x_test = x_test.reshape((x_test.shape[0], n_steps, n_features))

# RNN modelini oluştur / Create RNN model
model = Sequential()
model.add(SimpleRNN(50, activation='relu', input_shape=(n_steps, n_features)))
model.add(Dense(1, activation='sigmoid'))

# Modeli derle / Compile model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Modeli eğit / Train model
model.fit(x_train, y_train, epochs=10, batch_size=32, validation_data=(x_test, y_test))

# Modeli değerlendir / Evaluate model
loss, accuracy = model.evaluate(x_test, y_test)
print('Test Loss:', loss)
print('Test Accuracy:', accuracy)
