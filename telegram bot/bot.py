import telegram
from telegram.ext import Updater, CommandHandler
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

# Замените на свои значения
TELEGRAM_TOKEN = '6424413720:AAFc058kU0oq1j2MBk56cC-5oDmu_dgvjfY'
BITCOIN_RPC_USER = 'YOUR_BITCOIN_RPC_USERNAME'
BITCOIN_RPC_PASSWORD = 'YOUR_BITCOIN_RPC_PASSWORD'
BITCOIN_RPC_HOST = 'localhost'
BITCOIN_RPC_PORT = '8332'

# Инициализация клиента Bitcoin RPC
rpc_connection = AuthServiceProxy(f'http://{BITCOIN_RPC_USER}:{BITCOIN_RPC_PASSWORD}@{BITCOIN_RPC_HOST}:{BITCOIN_RPC_PORT}')

# Функция для генерации нового адреса
def get_new_address(update, context):
    new_address = rpc_connection.getnewaddress()
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"New address generated: {new_address}")

# Функция для получения баланса
def get_balance(update, context):
    balance = rpc_connection.getbalance()
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Balance: {balance} BTC")

def main():
    # Инициализация бота Telegram
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Добавляем обработчики команд
    dispatcher.add_handler(CommandHandler("getnewaddress", get_new_address))
    dispatcher.add_handler(CommandHandler("getbalance", get_balance))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
