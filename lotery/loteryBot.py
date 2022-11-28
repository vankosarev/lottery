import telebot
import ticket

bot = telebot.AsyncTeleBot("5719193324:AAHO9GKQYIIl3TSI3AAWXtKkmRJeYClVd5M")

@bot.message_handler(commands=['start'])

def send_welcome(message):
	bot.reply_to(message, "Привет, мы проводим тестовый розыгрыш нашей лотереи что бы проверить работоспособность бота. Трансляцию с розыгрышом проведём 20.11.2022 в 20:00. Что бы получить билет напиши - /ticket_get ")

@bot.message_handler(commands=['ticket'])

def ticketp(message):
    bot.reply_to(message,'Лотерейный билет стоит 10 ₽, как только ты оплатишь я тебе отправлю твой лотерейный билет, что бы получить билет напиши "билет"/ticket_get')
        
@bot.message_handler(commands=['ticket_get'])
    
def ticket_get(message):
    ticket_py()
    photo = open(r'C:\Users\иван\Desktop\lotery\ticket_try.png', 'rb')
    bot.send_photo(message.chat.id, photo)

def ticket_py():
    ticket.print_number()

bot.infinity_polling()
    
