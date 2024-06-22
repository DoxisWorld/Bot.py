from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Funktion, die auf den /start-Befehl reagiert
def start(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    message = "BrateeLaMousseGame\nhttps://t.me/DoxisGameBot/BrateeLaMousse"
    context.bot.send_message(chat_id=chat_id, text=message)

def main() -> None:
    # Geben Sie hier Ihren Bot-Token ein
    token = '7115505550:AAGXbZJx3qzxNACuX-NicOk3Fmm90qED2A4'
    
    # Erstellen Sie den Updater und Dispatcher
    updater = Updater(token)

    # Holen Sie sich den Dispatcher, um Handler hinzuzufügen
    dispatcher = updater.dispatcher

    # Fügen Sie einen Handler für den /start-Befehl hinzu
    dispatcher.add_handler(CommandHandler("start", start))

    # Starten Sie den Bot
    updater.start_polling()

    # Laufen lassen, bis Sie Strg+C drücken
    updater.idle()

if __name__ == '__main__':
    main()
