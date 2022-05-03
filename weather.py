import requests


def kelv_to_cels(kel):
    return round(kel - 273.15)


def main(bot, token):
    @bot.message_handler(commands=['weather'])
    def trigger_weather(message):
        bot.send_message(message.chat.id, "Введите город:")
        bot.register_next_step_handler(message, weather)

    def weather(message):
        city = message.text
        resp = requests.get(
            'http://api.openweathermap.org/data/2.5/find?q=' + city + ',RU' + '&type=like&APPID=' + token)
        temp = resp.json()['list'][0]['main']['temp']
        humidity = resp.json()['list'][0]['main']['humidity']
        wind_speed = resp.json()['list'][0]['wind']['speed']
        bot.send_message(message.chat.id, 'Температура: {}℃\nВлажность: {}%\nСкорость ветра: {} метр/сек'
            .format(str(temp), str(humidity), str(wind_speed)))
