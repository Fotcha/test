import requests
from telebot import types
import telebot
import base64
from bs4 import BeautifulSoup
import json,time

took = input('8028547309:AAHFuwHer16a-Nn4-xkejRVYnFD6FCs5bu8: ')
bot = telebot.TeleBot(took)

@bot.message_handler(commands=['start'])
def sd(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("channel", url="https://t.me/HexUnitPH")
    markup.add(btn)

    sd.sd = message.from_user.first_name
    bot.send_message(message.chat.id, f"Welcome {sd.sd} to the AI bot. Send your question to get an answer.", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    saad = message.text
    a = message.from_user.first_name  
    Fix = saad 
    response = requests.get("https://ghostbin.site/csxio")
    LevIi = base64.b64decode(BeautifulSoup(response.text, 'html.parser').find('div', id='code').get_text(strip=True)).decode()

    url = "http://pass-gpt.nowtechai.com/api/v1/pass"
    payload = json.dumps({
        "contents": [
            {"role": "system", "content": LevIi},
            {"role": "user", "content": Fix}
        ]
    })

    headers = {
        'User-Agent': "Ktor client",
        'Connection': "Keep-Alive",
        'Accept': "application/json",
        'Accept-Encoding': "gzip",
        'Content-Type': "application/json",
        'Key': "Q_B_H/l4RKTuqNDrIyUechJ0hp7d3z1zbe8o8eBrFlpMo0If/Q_B_H+w==",
        'Accept-Charset': "UTF-8"
    }

    # Sending a temporary response message
    temp_msg = bot.send_message(message.chat.id, "Generating response, please wait...")

    try:
        response = requests.post(url, data=payload, headers=headers)
        content_text = "".join(json.loads(line[5:])["content"] for line in response.text.splitlines() if '"status":"stream"' in line)
        bot.send_message(message.chat.id, content_text)
    except Exception as e:
        bot.send_message(message.chat.id, "An error occurred while processing the request.")
    finally:
        # Deleting the temporary message after a short delay
        time.sleep(2)  # Wait for 3 seconds
        bot.delete_message(message.chat.id, temp_msg.message_id)

bot.infinity_polling()