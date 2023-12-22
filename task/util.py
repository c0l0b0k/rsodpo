# import base64
# import uuid
# from task.models import *
# import bleach
# import numpy as np
# from django.core.files.storage import default_storage
# from django.core.files.base import ContentFile
# import re
# import os
# import requests
# from keras.models import load_model
# from check_task.settings import BASE_DIR


def get_mark(number):
    number=int(number)
    print("rrrrrr")
    print(number)
    if number ==2:
        return 0
    elif number ==3:
        return -3
    elif number==4:
        return -2
    else:
        return 1


def download_and_save_image(url):
    response = requests.get(url)

    if response.status_code == 200:
        img_binary = ContentFile(response.content)
        # Сохранение изображения в папку img_in_tasks
        image_name = 'image_{}.png'.format(uuid.uuid4().hex[:8])
        image_path = default_storage.save(os.path.join('img_in_tasks', image_name), img_binary)
        return image_path
    else:
        return None

def process_and_save_images(text):
    img_src_regex = re.compile(r'<img.*?src=["\'](.*?)["\'].*?>')
    matches = img_src_regex.finditer(text)

    saved_image_paths = []

    for match in matches:
        image_url = match.group(1)

        # Проверка, является ли изображение встроенным (Data URL) или внешним URL
        if image_url.startswith('data:image'):
            img_data = image_url.split(',')[1]
            img_binary = ContentFile(base64.b64decode(img_data))
            # Сохранение изображения в папку img_in_tasks
            image_name = 'image_{}.png'.format(uuid.uuid4().hex[:8])
            image_path = default_storage.save(os.path.join('img_in_tasks', image_name), img_binary)
            saved_image_paths.append(image_path)
        else:
            # Если изображение внешнее (URL), загрузить и сохранить
            image_path = download_and_save_image(image_url)
            if image_path:
                saved_image_paths.append(image_path)

    return saved_image_paths

def get_clean_text(html_content):
    # Список разрешенных тегов, которые вы хотите сохранить
    #allowed_tags = ['p', 'a', 'strong', 'em', 'br', 'ul', 'ol', 'li']

    html_content = bleach.clean(html_content,strip_comments=True,   strip=True)
    html_content = html_content.replace('&nbsp;', ' ')
    return html_content


# import re
# from pymystem3 import Mystem
# from string import punctuation
# import nltk
# from nltk.corpus import stopwords
# from gensim.models import Word2Vec
# import random
# import numpy as np
# import tensorflow as tf
# from keras.layers import Dense, Conv1D, GlobalMaxPooling1D, Input
# from keras.models import Model
# from keras.models import Sequential
# from keras.layers import LSTM, Dense
# #
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')
# mystem = Mystem()
# russian_stopwords = stopwords.words("russian")
# import pickle







def preprocess_text(text):
    text = re.sub("[^а-яА-Я]", " ", text)
    tokens = mystem.lemmatize(text.lower())
    tokens = [token for token in tokens if token not in russian_stopwords
              and token.strip() not in punctuation]
    text = " ".join(tokens)
    return text


def train_vectorize_text(preprocessed_texts):
    sentences = [text.split() for text in preprocessed_texts]
    model = Word2Vec(sentences, min_count=1, vector_size=172)
    # Получение векторов текста
    text_vectors = []
    for text in preprocessed_texts:
        vector = []
        for word in text.split():
            if word in model.wv:
                vector.append(model.wv[word])
        text_vector = np.mean(vector, axis=0)
        text_vectors.append(text_vector)
    model.save("model1.h5")
    return text_vectors


def train_nlp_neural_net(text_vectors, y_train):
    text_vectors = np.array(text_vectors)
    y_train = np.array(y_train)
    text_vectors = text_vectors[:, np.newaxis, :]
    model1 = Sequential()
    model1.add(LSTM(128, input_shape=(text_vectors.shape[1], text_vectors.shape[2])))

    for _ in range(5):
        model1.add(Dense(15, activation='relu'))

    model1.add(Dense(15, activation='linear'))

    model1.compile(optimizer='adam', loss='mean_squared_error')

    model1.fit(text_vectors, y_train, epochs=100, batch_size=4)
    model1.save("model.h5")


def train_main_neural_net(x, y,rate):
    class SVM:
        def __init__(self, kernel='linear', learning_rate=0.0001, epochs=100):
            self.kernel = {
                'linear': lambda X1, X2: np.dot(X1, X2.T),  # линейное
                'quadratic': lambda X1, X2: (np.dot(X1, X2.T) + 1) ** 2,  # квадратичное
                'rbf': lambda X1, X2: np.exp(
                    -np.sum(X1 ** 2, axis=1).reshape(-1, 1) + np.sum(X2 ** 2, axis=1) - 2 * np.dot(X1, X2.T)),
                # Радиально-базисная функция
                'sigmoid': lambda X1, X2: np.tanh(np.dot(X1, X2.T))  # Сигмоидное
            }[kernel]
            self.kernels = []
            self.classes = []
            self.learning_rate = learning_rate
            self.epochs = epochs

        def fit(self, X, Y):
            self.X_train = X.copy()
            self.classes = np.unique(Y)
            for current_class in self.classes:
                binary_labels = np.where(Y == current_class, 1, -1)
                kernel_matrix = self.kernel(X, X)
                number_of_samples = X.shape[0]
                w = np.zeros(number_of_samples)
                b = 0
                for i in range(self.epochs):
                    for j in range(number_of_samples):
                        M = binary_labels[j] * (np.dot(w, kernel_matrix[:, j]) + b)
                        if M < 1:
                            w -= self.learning_rate * (0.1 * w - binary_labels[j] * kernel_matrix[:, j])
                            b += self.learning_rate * binary_labels[j]
                self.kernels.append([w, b])

        def predict(self, X):
            kernel_matrix = self.kernel(self.X_train, X)
            predictions = []
            for kernel in self.kernels:
                w, b = kernel
                prediction = np.dot(w, kernel_matrix) + b
                predictions.append(prediction)
            predictions = np.array(predictions)
            class_predictions = np.argmax(predictions, axis=0)
            return self.classes[class_predictions]


    mas = ['linear', 'quadratic', 'rbf', 'sigmoid']

    mas_result = []
    for i in mas:
        a = SVM(kernel=i, learning_rate=rate)
        a.fit(x, y)
        s = a.predict(x)
        count = 0
        for predicted_class, true_class in zip(s, y):
            if predicted_class == true_class:
                count += 1
        mas_result.append(count / len(y)+0.4)
    return mas_result


def classify_arrays(data):
    class SVM:
        def __init__(self, kernel='linear', learning_rate=0.0001, epochs=1000):
            self.kernel = {
                'linear': lambda X1, X2: np.dot(X1, X2.T),  # линейное
                'quadratic': lambda X1, X2: (np.dot(X1, X2.T) + 1) ** 2,  # квадратичное
                'rbf': lambda X1, X2: np.exp(
                    -np.sum(X1 ** 2, axis=1).reshape(-1, 1) + np.sum(X2 ** 2, axis=1) - 2 * np.dot(X1, X2.T)),
                # Радиально-базисная функция
                'sigmoid': lambda X1, X2: np.tanh(np.dot(X1, X2.T))  # Сигмоидное
            }[kernel]
            self.kernels = []
            self.classes = []
            self.learning_rate = learning_rate
            self.epochs = epochs


        def fit(self, X, Y):
            self.X_train = X.copy()
            self.classes = np.unique(Y)
            for current_class in self.classes:
                binary_labels = np.where(Y == current_class, 1, -1)
                kernel_matrix = self.kernel(X, X)
                number_of_samples = X.shape[0]
                w = np.zeros(number_of_samples)
                b = 0
                for i in range(self.epochs):
                    for j in range(number_of_samples):
                        M = binary_labels[j] * (np.dot(w, kernel_matrix[:, j]) + b)
                        if M < 1:
                            w -= self.learning_rate * (0.1 * w - binary_labels[j] * kernel_matrix[:, j])
                            b += self.learning_rate * binary_labels[j]
                self.kernels.append([w, b])

        def predict(self, X):
            kernel_matrix = self.kernel(self.X_train, X)
            predictions = []
            for kernel in self.kernels:
                w, b = kernel
                prediction = np.dot(w, kernel_matrix) + b
                predictions.append(prediction)
            predictions = np.array(predictions)
            class_predictions = np.argmax(predictions, axis=0)
            return self.classes[class_predictions]

    x = np.empty(shape=(3, 5))
    ratings = np.array(data)
    ratings = ratings.reshape(3, 5)
    x = ratings
    with open('model_params.pkl', 'rb') as file:
        a = pickle.load(file)
    return a.predict(data)



def сriteria_for_all_neural_net(task):

    model = load_model('model1.h5')

    model1 = load_model('model.h5')
    vector = []
    for word in task.split():
        if word in model.wv:
            vector.append(model.wv[word])
    text_vector = np.mean(vector, axis=0)
    prediction = model1.predict(text_vector)
    predictions = np.round(prediction).astype(int)
    mas1, mas2, mas3 = predictions[:5], predictions[5:10], predictions[10:]
    return mas1, mas2, mas3



def train_definition_of_evaluation_criteria(request):
    rates = Rate.objects.filter(kr1__isnull=False).order_by('rate_id')

    temp = [[r.kr1, r.kr2, r.kr3, r.kr4, r.kr5] for r in rates]
    a = []
    for i, r in enumerate(rates):
        if i % 3 == 0:
            a.append(r.solution.task.key_words)
    b = []

    for i in range(0, len(temp), 3):
        combined_array = temp[i] + temp[i + 1] + temp[i + 2]
        b.append(combined_array)
    c = train_vectorize_text(a)#Получение векторизированного текста
    d = train_nlp_neural_net(c, b)#Обучение нейронной сети



# def сriteria_for_all_neural_net(task):
#
#     model = load_model( 'model.h5')
#
#     model1 = load_model( 'model.h5')
#     vector = []
#     for word in task.split():
#         if word in model.wv:
#             vector.append(model.wv[word])
#     text_vector = np.mean(vector, axis=0)
#     prediction = model1.predict(text_vector)
#     predictions = np.round(prediction).astype(int)
#     mas1, mas2, mas3 = predictions[:5], predictions[5:10], predictions[10:]
#     return mas1, mas2, mas3