import os
import telebot

TOKEN = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "👋 به باشگاه نقطه خوش اومدی!\n\n"
        "اینجا قراره ۴۰ روز کنار هم برای ساختن یک سبک زندگی بهتر تلاش کنیم. 🌱\n\n"
        "🚀 شروع چالش\n"
        "ℹ️ چالش چیه؟\n"
        "🏆 جوایز\n"
        "❓ سوالات متداول"
    )

bot.infinity_polling()
