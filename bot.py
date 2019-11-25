from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings



logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
					level=logging.INFO,
					filename='bot.log'
					)

def greet_user(bot, update):
	text = 'Вызван /start'
	logging.info(text)
	update.message.reply_text(text)

def talk_to_me(bot, update):
	user_text = 'Привет {}! Ты написал: {}'.format(update.message.chat.first_name, update.message.text) 
	logging.info('User: %s, Chat id: %s, Message: %s', update.message.chat.username, update.message.chat.id, update.message.text)
	update.message.reply_text(user_text)


def main():
	catbot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)

	

	dp = catbot.dispatcher
	dp.add_handler(CommandHandler("start", greet_user))
	dp.add_handler(MessageHandler(Filters.text, talk_to_me))

	catbot.start_polling()
	catbot.idle()

main()

