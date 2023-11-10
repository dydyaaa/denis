import telebot
import math
import additional as dop
import buttons as btn
import cfg
import rub_rate as rt


bot = telebot.TeleBot(cfg.TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Это пример стартового сообщения.", reply_markup=btn.strbtn)
    
@bot.message_handler(func=lambda message: message.text == "💲Рассчитать стоимость")
def handle_calculate_cost(message):
    bot.send_message(message.chat.id, "Выберите категорию товара:", reply_markup=btn.cartbtn)

@bot.message_handler(func=lambda message: message.text in ["👟Кроссовки", "🧥Верхняя одежда", "🧦Носки", "👖Толстовки/Штаны", "👕Футболки/Шорты", "🧣Аксессуары"])
def handle_product_category(message):
    global current_value 
    current_value = message.text
    bot.send_message(message.chat.id, "Введите стоимость в Юанях:")
    bot.register_next_step_handler(message, process_number)

def process_number(message):
    try:
        number = int(message.text)
        result = perform_operation(number)
        bot.send_message(message.chat.id, f"Стоимость в рублях: {result}")
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите корректное число.")

# Функция с формулами рассчета цен. Можно вывести в отдельный файл для удобства
def perform_operation(number):
    if current_value == "👟Кроссовки":
        return math.ceil(number * rt.get_rub_rate())
    elif current_value == "🧦Носки":
        return math.ceil(number * (rt.get_rub_rate() + 1) + 1000)
    else:
        return math.ceil(number)

@bot.message_handler(func=lambda message: True)
def menu(message):
    if message.text == "💵Актуальный курс":
        mes = f'Текущий курс Юаня: {rt.get_rub_rate()}'
        bot.send_message(message.chat.id, mes)
    elif message.text == "❓Вопросы и ответы":
        bot.send_message(message.chat.id, dop.faq)
    # elif message.text == "🛒Каталог":
    #     bot.send_message(message.chat.id, "Выберете интересующую вас категорию", reply_markup=btn.cartbtn)
    elif message.text == "📲Отзывы":
        bot.send_message(message.chat.id, dop.otzv)
    elif message.text == "📞Связь с менеджером":
        bot.send_message(message.chat.id, "6")
    elif message.text == "⬅️Назад":
        send_welcome(message)
    else:
        bot.send_message(message.chat.id, "Извините, я вас не понимаю")

if __name__ == "__main__":
    bot.polling()