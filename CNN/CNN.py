import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.models import Sequential
from keras.layers import Conv1D, MaxPooling1D, Flatten, Dense

# Verileri yükle / Load dataset
data = pd.read_csv('dataset/path')

# Girdi ve çıktı verilerini ayır / Separate input and output data
x = data.drop(columns=['label'])
y = data['label']

# Etiketleri kodla / Encode labels
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Verileri eğitim ve test setlerine ayır / Separate data into training and test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Veri setini CNN modeline uygun hale getir / Reshape data for CNN model
n_steps = 2548  # Örnek başına zaman adımlarının sayısı / Number of time steps per sample
n_features = 1  # Her bir zaman adımındaki özellik sayısı / Number of features in each time step
x_train = x_train.values.reshape((-1, n_steps, n_features))
x_test = x_test.values.reshape((-1, n_steps, n_features))

# Modeli oluştur / Create model
model = Sequential()
model.add(Conv1D(filters=64, kernel_size=3, activation='relu', input_shape=(n_steps, n_features)))
model.add(MaxPooling1D(pool_size=2))
model.add(Flatten())
model.add(Dense(100, activation='relu'))
model.add(Dense(len(label_encoder.classes_), activation='softmax'))  # Çıkış katmanı

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Modeli eğit / Train model
model.fit(x_train, y_train, epochs=10, batch_size=32, validation_data=(x_test, y_test))

# Modeli değerlendir / Evaluate model
loss, accuracy = model.evaluate(x_test, y_test)
print('Test Loss:', loss)
print('Test Accuracy:', accuracy)
