# Convolutional Neural Network (CNN) Nedir?

CNN (Convolutional Neural Network), özellikle görüntü işleme alanında başarılı olan derin öğrenme modellerinden biridir. Özellikle görsel veri analizi için tasarlanmış olup, öğrenme işleminde konvolüsyon (evrişim) ve havuzlama (pooling) gibi işlemleri kullanır.

## Temel Yapısı

- **Evrişim Katmanları (Convolutional Layers):** Girdi verisini bir dizi filtre ile evrişimleyerek (convolve ederek) farklı özellikleri çıkartır. Bu sayede, örneğin kenarlar, köşeler veya desenler gibi düşük seviye özellikler algılanabilir.
  
- **Aktivasyon Fonksiyonları:** Evrişim sonrası çıktılar üzerinde uygulanır. ReLU (Rectified Linear Unit) sıklıkla kullanılır.

- **Havuzlama Katmanları (Pooling Layers):** Evrişim sonrası elde edilen özellik haritalarını özetlemek için kullanılır. Max pooling ve average pooling gibi yöntemlerle özellik haritalarının boyutu küçültülür.

- **Tam Bağlı Katmanlar (Fully Connected Layers):** Havuzlama katmanlarından sonra, özellik haritalarını düzleştirip (flatten) tam bağlı katmanlara bağlanır. Bu katmanlar genellikle sınıflandırma işlemi için kullanılır.

## CNN'in Avantajları

- **Özellik Hiyerarşisi Öğrenme:** Evrişim ve havuzlama katmanları sayesinde, model daha düşük seviye özelliklerden daha yüksek seviye özelliklere kadar bir hiyerarşi öğrenebilir.

- **Çoklu Boyutlar İşleme:** Görüntü gibi çoklu boyutlarda verileri işlemek için uygun bir yapı sunar.

- **Veri Uzayında Durağanlık:** Evrişim ve havuzlama katmanları, görüntülerdeki nesnelerin konumunu öğrenirken veri uzayında durağanlığı (translation invariance) sağlar.

## Nasıl Kullanılır?

CNN'ler genellikle Keras, TensorFlow veya PyTorch gibi derin öğrenme kütüphaneleri üzerinde uygulanır. Bu kütüphanelerde CNN modeli oluşturmak için önceden tanımlanmış sınıflar ve fonksiyonlar bulunur.

# ------------------------------------------------------------------------------

# Convolutional Neural Network (CNN) Overview

CNN (Convolutional Neural Network) is a deep learning model particularly successful in image processing. It is designed for visual data analysis and utilizes convolution and pooling operations in the learning process.

## Basic Structure

- **Convolutional Layers:** Extract features by convolving the input data with a set of filters. This process highlights different features such as edges, corners, or patterns.
  
- **Activation Functions:** Applied on the outputs of convolutional layers. ReLU (Rectified Linear Unit) is commonly used.

- **Pooling Layers:** Used to summarize feature maps. They reduce the size of feature maps using methods like max pooling or average pooling.

- **Fully Connected Layers:** After pooling layers, feature maps are flattened and connected to fully connected layers. These layers are often used for classification.

## Advantages of CNN

- **Learning Feature Hierarchies:** CNN can learn hierarchies of features from low-level features to high-level features.
  
- **Processing Multidimensional Data:** Provides a suitable structure for processing data with multiple dimensions, such as images.

- **Translation Invariance in Data Space:** Convolution and pooling layers provide translation invariance in the data space while learning the position of objects in images.

## How to Use CNN

CNNs are typically implemented using deep learning libraries such as Keras, TensorFlow, or PyTorch. These libraries provide pre-defined classes and functions for creating CNN models.
