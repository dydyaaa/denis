import telebot


strbtn = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
cartbtn = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
clear = telebot.types.ReplyKeyboardRemove()

btn1 = telebot.types.KeyboardButton(text="💲Рассчитать стоимость")
btn2 = telebot.types.KeyboardButton(text="💵Актуальный курс")
btn3 = telebot.types.KeyboardButton(text="❓Вопросы и ответы")
btn4 = telebot.types.KeyboardButton(text="🛒Каталог")
btn5 = telebot.types.KeyboardButton(text="📲Отзывы")
btn6 = telebot.types.KeyboardButton(text="📞Связь с менеджером")

btnn1 = telebot.types.KeyboardButton(text="👟Кроссовки")
btnn2 = telebot.types.KeyboardButton(text="🧥Верхняя одежда")
btnn3 = telebot.types.KeyboardButton(text="🧦Носки")
btnn4 = telebot.types.KeyboardButton(text="👖Толстовки/Штаны")
btnn5 = telebot.types.KeyboardButton(text="👕Футболки/Шорты")
btnn6 = telebot.types.KeyboardButton(text="🧣Аксессуары")
btnn7 = telebot.types.KeyboardButton(text="⬅️Назад")

strbtn.add(btn1, btn2, btn3, btn5, btn6)
cartbtn.add(btnn1, btnn2, btnn3, btnn4, btnn5, btnn6, btnn7)