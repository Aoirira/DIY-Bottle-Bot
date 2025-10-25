import telebot
import random
from config import token
bot = telebot.TeleBot(token)

IDEAS =[
    "Rocket 🚀 — Attach fins to a 2-liter bottle, add water and air pressure, then launch it.",
    "Boat ⛵ — Tape multiple bottles together and add a deck.",
    "Catapult 🏹 — Popsicle sticks + rubber bands + bottle cap.",
    "Laptop 💻 — Cut bottle into two parts, decorate.",
    "Squish ✨ — Glitter water sensory bottle."
]

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "👋 Hello! I am a DIY ideas bot.\n\n"
        "Commands:\n"
        "/idea — random idea\n"
        "/list — list of ideas\n"
        "/help — help info\n"
        "/instructions — how to build ideas"
    )

@bot.message_handler(commands=["idea"])
def idea(message):
    bot.send_message(message.chat.id, f"✨ {random.choice(IDEAS)}")

@bot.message_handler(commands=["list"])
def list_ideas(message):
    text = "\n".join(f"{i+1}. {idea}" for i, idea in enumerate(IDEAS))
    bot.send_message(message.chat.id, "📌 Idea list:\n" + text)

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(
        message.chat.id,
        "/idea — random DIY project\n"
        "/list — all ideas\n"
        "/instructions — build guide"
    )

@bot.message_handler(commands=["instructions"])
def instructions(message):
    bot.send_message(
        message.chat.id,
        "📐 Safety instructions:\n"
        "- Be careful with scissors\n"
        "- Ask adult supervision\n"
        "- Launch rockets OUTSIDE"
    )

bot.polling()
