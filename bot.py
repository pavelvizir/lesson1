from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
	level=logging.INFO,
	filename='bot.log'
	)

def greet_user(bot, update):
	
	text = 'Вызван /start'
	print(text)
	print(update)
	update.message.reply_text(text)

def talk_to_me(bot, update):
	user_text = update.message.text
	print(user_text)
	#update.message.reply_text(user_text[::-1].swapcase())
	update.message.reply_text(user_text[::-1])

def main():
	updater = Updater("542301182:AAE7MWQzPnu4nDeDEn_vBqqgvceBrSbRoYs")

	dp = updater.dispatcher
	dp.add_handler(CommandHandler("start", greet_user))
	dp.add_handler(MessageHandler(Filters.text, talk_to_me))

	updater.start_polling()
	updater.idle()

main()