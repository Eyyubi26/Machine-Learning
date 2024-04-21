# LSTM ile Zaman Serisi Tahmini

Bu proje, LSTM (Uzun Kısa Vadeli Bellek) kullanarak zaman serisi tahmini yapmayı amaçlamaktadır. LSTM, özellikle zaman serileri gibi dizisel verilerle çalışırken kullanılan bir yapay sinir ağı modelidir.

## Nasıl Çalışır?

- Veriler yüklenir ve girdi ve çıktı verileri ayrılır.
- Veriler, eğitim ve test setlerine ayrılır.
- LSTM modeli oluşturulur. Model, bir LSTM katmanı ve ardından bir yoğun katman içerir.
- Model derlenir ve eğitilir.
- Eğitim sırasında oluşan kayıplar bir CSV dosyasına kaydedilir.
- Model, test verileri üzerinde değerlendirilir ve test kaybı hesaplanır.

## LSTM Nedir?

LSTM, Uzun Kısa Vadeli Bellek anlamına gelir ve zaman serileri gibi dizisel verilerle çalışırken kullanılan bir yapay sinir ağı modelidir. LSTM'ler, geleneksel RNN'lerden (Rekürrent Sinir Ağları) farklı olarak, zaman serisi verilerindeki uzun vadeli bağımlılıkları daha etkili bir şekilde işleyebilirler. Bu nedenle, zaman serileri analizi, doğal dil işleme ve benzeri uygulamalarda sıklıkla kullanılırlar.

# ------------------------------------------------------------------------------

# Time Series Forecasting with LSTM

This project aims to perform time series forecasting using LSTM (Long Short Term Memory). LSTM is an artificial neural network model used especially when working with sequential data such as time series.

## How does it work?

- Data is loaded and input and output data are separated.
- Data is divided into training and test sets.
- The LSTM model is created. The model contains an LSTM layer followed by a dense layer.
- The model is compiled and trained.
- Losses during training are saved in a CSV file.
- The model is evaluated on test data and the test loss is calculated.

## What is LSTM?

LSTM stands for Long Short Term Memory and is an artificial neural network model used when working with sequential data such as time series. Unlike traditional RNNs (Recurrent Neural Networks), LSTMs can more effectively handle long-term dependencies in time series data. Therefore, they are often used in time series analysis, natural language processing and similar applications.