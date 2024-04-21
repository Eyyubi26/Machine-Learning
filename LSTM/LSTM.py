import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from keras.models import Sequential
from keras.layers import LSTM, Dense
from keras.callbacks import CSVLogger

# Verileri yükle / Load dataset
data = pd.read_csv('dataset/path')

# Girdi ve çıktı verilerini ayır / Separate input and output data
X = data
y = data

# Verileri eğitim ve test setlerine ayır / Separate data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

n_steps = 15  # Örnek başına zaman adımlarının sayısı / Number of time steps per sample
n_features = 1  # Her bir zaman adımındaki özellik sayısı / Number of features in each time step

# Modeli oluştur / Create model
model = Sequential()
model.add(LSTM(50, activation='relu', input_shape=(n_steps, n_features)))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')

csv_logger = CSVLogger('Logs/TrainLogs.csv', append=True)

# Modeli eğit / Train model
model.fit(X_train, y_train, epochs=100, verbose=1, callbacks=[csv_logger])

# Modeli değerlendir / Evaluate model
loss = model.evaluate(X_test, y_test)
print('Test Loss:', loss)