import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import openai

# Set up the Telegram bot
bot_token = "YOUR_TELEGRAM_BOT_TOKEN_HERE"
bot = telegram.Bot(token=bot_token)

# Set up the OpenAI API client
openai.api_key = "YOUR_OPENAI_API_KEY_HERE"
model_engine = "text-davinci-002"

# Define a function to handle incoming messages from users
def handle_message(update, context):
    message = update.message.text
    response = openai.Completion.create(
        engine=model_engine,
        prompt=message,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    bot.send_message(chat_id=update.effective_chat.id, text=response.choices[0].text)

# Set up the Telegram bot updater and add the message handler
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

# Start the bot
updater.start_polling()
