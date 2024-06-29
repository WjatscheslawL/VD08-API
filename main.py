from flask import Flask, render_template, request
import requests

# импортируем объект класса Flask
app = Flask(__name__)

# формируем путь и методы GET и POST

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    news = None
    quotas = None
    if request.method == 'POST':
        city = request.form['city']
        weather = get_weather(city)
        # передаем информацию о погоде в index.html
        news = get_news()
        quotas = get_quotable()
    return render_template("index.html", weather=weather, news=news, quotas=quotas)


# в функции прописываем город, который мы будем вводить в форме
def get_weather(city):
    api_key = "fd2b7a60664909ef6733adc332f7109f"
    # адрес, по которомы мы будем отправлять запрос. Не забываем указывать f строку.
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    # для получения результата нам понадобится модуль requests
    response = requests.get(url)
    # прописываем формат возврата результата
    return response.json()


def get_news():
    api_key = "53198030c8674f16b3e411ad5707a877"
    url = f"https://newsapi.org/v2/top-headlines?country=ru&apiKey={api_key}"
    response = requests.get(url)
    return response.json().get('articles', [])


def get_quotable():
    api_key = "53198030c8674f16b3e411ad5707a877"
    url = f"https://api.quotable.io/random"
    response = requests.get(url)
    return response.json() #.get('articles', [])


if __name__ == '__main__':
    app.run(debug=True)
