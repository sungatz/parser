from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "7330033768:AAFgy1XiZfsu7EF26n-fT7luxmLgBzmchiU"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка команды /start."""
    await update.message.reply_text("Привет! Я ваш бот. Напишите /report для подачи жалобы.")

async def report(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка команды /report."""
    user = update.message.from_user
    report_text = ' '.join(context.args)  # Получаем текст после команды
    if not report_text:
        await update.message.reply_text("Пожалуйста, добавьте текст жалобы. Пример: /report @username Проблема с пользователем.")
        return

    # Если первый аргумент начинается с "@" — это может быть ник пользователя
    mentioned_user = None
    if context.args[0].startswith('@'):
        mentioned_user = context.args[0]

    # Формируем сообщение жалобы
    message = f"Жалоба от {user.first_name} ({user.id}):\n"
    if mentioned_user:
        message += f"Жалоба на пользователя: {mentioned_user}\n"
    message += f"Текст жалобы: {' '.join(context.args[1:])}"  # Текст жалобы после никнейма

    # ID чата администратора
    CHAT_ID = -1002361281154  # Замените на ваш ID
    await context.bot.send_message(chat_id=CHAT_ID, text=message)
    await update.message.reply_text("Ваша жалоба отправлена администраторам.")

def main():
    """Запуск бота."""
    # Создаем приложение
    application = Application.builder().token(BOT_TOKEN).build()

    # Добавляем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("report", report))

    # Запускаем бота
    application.run_polling()

if __name__ == "__main__":
    main()
