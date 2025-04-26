import telebot
import os

BOT_TOKEN = os.getenv('BOT_TOKEN')  # Railway'de gizli tutacağız
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Merhaba! 👋 Size nasıl yardımcı olabilirim?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    text = message.text.lower()
    if 'hizmet' in text:
        bot.reply_to(message, "Web uygulamaları, scriptler, sunucu hizmetleri sunuyorum! 📩 (08:00 - 00:00 arası aktifim.)")
    elif 'fiyat' in text:
        bot.reply_to(message, "Hizmetlerimizin fiyatları projeye göre değişmektedir. Detaylı bilgi için iletişime geçin! 🚀")
    else:
        bot.reply_to(message, "Size nasıl yardımcı olabilirim? 📩")

bot.infinity_polling()
