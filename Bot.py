#
# import telebot
# from telebot import types
# import requests
#
# OPENWEATHER_API_KEY = "4184aa44e3528943ccde1627befd10a1"
# bot = telebot.TeleBot('6437532876:AAHoPS5uV3WxRAn2bbZtcrzZ4Idx9LwMGuw')
#
#
# def get_weather(city):
#     base_url = 'https://api.openweathermap.org/data/2.5/weather'
#     params = {
#         'q': city,
#         'appid': "4184aa44e3528943ccde1627befd10a1",
#         'units': 'metric'
#     }
#
#     response = requests.get(base_url, params=params)
#
#     weather_data = response.json()
#
#     if response.status_code == 200:
#         return weather_data
#     else:
#         return None
#
#
# @bot.message_handler(commands=['start'])
# def main(message):
#     markup = types.InlineKeyboardMarkup(row_width=2)
#     item1 = types.InlineKeyboardButton('London💨', callback_data='London')
#     item2 = types.InlineKeyboardButton('Dnipro💦', callback_data='Dnipro')
#     item3 = types.InlineKeyboardButton('Paris🌦', callback_data='Paris')
#     item4 = types.InlineKeyboardButton('Lviv☀️', callback_data='Lviv')
#     item5 = types.InlineKeyboardButton('Kyiv💨', callback_data='Kyiv')
#     item6 = types.InlineKeyboardButton('Washington💦', callback_data='Washington')
#     item7 = types.InlineKeyboardButton('Odessa🌦', callback_data='Odessa')
#     item8 = types.InlineKeyboardButton('Chernigov☀️', callback_data='Chernigov')
#     markup.add(item1, item2, item3, item4, item5, item6, item7, item8)
#     bot.send_message(message.chat.id, f"🌤Hi which city would you like to choose?🌦", reply_markup=markup)
#
#
# city_weather = ''
#
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback_handler(call):
#     global city_weather
#
#     if call.data in ['London', 'Chernigov', 'Odessa', 'Washington', 'Kyiv', 'Paris', 'Dnipro']:
#         city_weather = get_weather(call.data)
#         if city_weather:
#             print(city_weather)
#
#             temperature = city_weather['main']['temp']
#             description = city_weather['weather'][0]['description']
#             bot.send_message(call.message.chat.id,
#                              f"☀️Weather in🌥 {call.data}:\n🌡Temperature: {temperature}C\n📄Description: {description} ",
#                              reply_markup=markup)
#         else:
#             bot.send_message(call.message.chat.id, "Could not fetch data")
#
#     if call.data in ['More']:
#         speed_wind = city_weather['wind']['speed']
#         humidity = city_weather['main']['humidity']
#         bot.send_message(call.message.chat.id,
#                          f"🌬speed wind: {speed_wind}\n💧humidity: {humidity} ",
#                          reply_markup=markup)
#
#     if call.data in ['Menu']:
#         main(call.message)
#
#
# menu = types.InlineKeyboardButton('Menu', callback_data='Menu')
# more = types.InlineKeyboardButton('More', callback_data='More')
# markup = types.InlineKeyboardMarkup(row_width=2)
# markup.add(menu, more)
#
#
# @bot.message_handler(commands=['menu'])
# def button_menu(message):
#     main(message)
#
#
# bot.polling(none_stop=True)
print("Hello world")