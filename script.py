
import logging
import pdfkit

from telegram.ext import Updater, CommandHandler

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    update.message.reply_text('Hi! Im WATSON nice to meet you!')
    update.message.reply_text('I learn from your experience.')
    update.message.reply_text('Get my windows version from https://drive.google.com/file/d/1_HolW2mhigD8UnlgbNnbG7uh11R3onsO/view')
    update.message.reply_text('/use  - how to use me')
    update.message.reply_text('/about  - more about me')


def use(update, context):
    update.message.reply_text('You can use me to automate pretty much any process.')
    update.message.reply_text('Teach me things as you go by')
    update.message.reply_text('I learn quickly and then automate the process taught to help you get things done faster.')
    update.message.reply_text('Now, if you are convinced get my windows version from https://drive.google.com/file/d/1_HolW2mhigD8UnlgbNnbG7uh11R3onsO/view')
    update.message.reply_text('/help  - show menu')
    update.message.reply_text('/about  - more about me')


def about(update, context):
    update.message.reply_text('I am hyperpersonalised automation tool WATSON Watching And Tracking Software Over Network lets you create your own automation from scratch to increase your productivity and accuracy exponentially. I am designed to solve crisis situation.')
    update.message.reply_text('Developed by - Shashank P. Sharma')
    update.message.reply_text('read more here - https://github.com/shashank404error/WATSON-Project')
    update.message.reply_text('Now, if you are convinced get my windows version from https://drive.google.com/file/d/1_HolW2mhigD8UnlgbNnbG7uh11R3onsO/view')
    update.message.reply_text('/help  - show menu')
    update.message.reply_text('/use  - how to use me')
    
    
       
def set_url(update,context):
    """Add a job to queue"""
    chat_id = update.message.chat_id
    url = context.args[0]
    # update.message.reply_text(url)
    pdfkit.from_url(url,'order.pdf')
    context.bot.send_document(chat_id=chat_id, document=open('./order.pdf', 'rb'))

def main():
    """Run bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    TOKEN = '1312008372:AAHgQayVcazrc_45HUjc4RHWCfyKIeWzjck'
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", start))
    dp.add_handler(CommandHandler("about", about))
    dp.add_handler(CommandHandler("use", use))
    dp.add_handler(CommandHandler("get",set_url,pass_args=True,pass_job_queue=True,pass_chat_data=True ))

    # Start the Bot
    updater.start_polling()

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
