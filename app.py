import tensorflow as tf
from flask import Flask, request, render_template
app = Flask(__name__)

# Загрузка модели
def get_model():
    model = tf.keras.models.load_model('models/neural_model')
    return model


# Функция для выполнения прогноза
def prediction(params):
    model = get_model()
    pred = model.predict([params])
    return pred

@app.route('/', methods=['POST', 'GET']) # Определение маршрута ("/") и методов запроса ("POST" и "GET"), на который будет реагировать приложение Flask.


def predict():
    message = ' '
    if request.method == 'POST': # Проверка, что метод запроса - "POST", то есть это запрос на отправку данных от клиента.
        param_list = ('Плотность, кг/м3', 'модуль упругости, ГПа', 'Количество отвердителя, м.%', 
                      'Содержание эпоксидных групп,%_2', 'Температура вспышки, С_2', 'Поверхностная плотность, г/м2	', 
                      'Модуль упругости при растяжении, ГПа', 'Прочность при растяжении, МПа', 'Потребление смолы, г/м2',
                      'Угол нашивки, град', 'Шаг нашивки', 'Плотность нашивки')
        params = []   #Создание пустого списка для хранения значений параметров.
        for i in param_list: # Цикл для извлечения значений параметров из формы запроса на основе их имен из списка param_list.
            value = request.form.get(i) #Извлечение значения параметра из формы запроса с использованием его имени i
            params.append(value) #Добавление значения параметра в список params. append()принимает один аргумент value и ДОПИСЫВАЕТ его в конец params
        params = [float(i) for i in params] # Преобразование значений параметров в числа с плавающей точкой.

        message = f'Прогноз: {prediction(params)}'  # Форматирование строки message с использованием значения прогноза, полученного с помощью вызова функции prediction() с передачей ей параметров.
    return render_template('index.html', message= message)

if __name__ == '__main__':
    app.run()
