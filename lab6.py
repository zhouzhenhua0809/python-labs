import telebot
import requests

TOKEN = '5896503241:AAHDcrepzp5qxqSh4JWce0kqJVwcHYyCed4'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "type currency code e.g EUR for euro to get the exchange rate, the base currency is always the USD: ")

@bot.message_handler(content_types=['text'])
def get_user_text(message):
    params =  {
        'access_key' : '39ef71316134661a5eea6ed6',
        'rates' : message.text.upper()
    }
    print(message.text)
    results = requests.get('https://open.er-api.com/v6/latest/USD',params)
    try:
        bot.send_message(message.chat.id,f"Current Echange Rate: 1 USD is equivelent to  {results.json()['rates'][str(message.text).upper()]}")
    except:
         bot.send_message(message.chat.id,"Please type a currency(money) code e.g RUB for Russian rubbles, or CNY for the Chinese Yuan Renminbi or BYN for the Belarusin rubble to be displayed !!!,,  Examples of valid Currecy Codes can be found on this link https://stockmarketmba.com/listofcurrencies.php")




bot.polling(non_stop=True)