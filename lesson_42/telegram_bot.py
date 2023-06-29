import os
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import aiohttp
import asyncio


async def get_weather():
   url = 'https://api.openweathermap.org/data/2.5/weather' \
         '?appid=2a4ff86f9aaa70041ec8e82db64abf56&q=Minsk&units=metric'
   async with aiohttp.ClientSession() as session:
       async with session.get(url) as response:
           return await response.json()

def generate_expression() -> tuple[str, int]:
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    return f'{a} + {b}', a + b


async def start(update: Update, context: CallbackContext):
    await update.message.reply_html(rf"Hi {update.effective_user.mention_html()}!")

    expression, expected_answer = generate_expression()
    context.user_data['expected_answer'] = expected_answer
    await update.message.reply_text(expression)

async def check_answer(update: Update, context: CallbackContext) -> None:
    if update.message.text.isdigit():
        answer = int(update.message.text)
        expected_answer = context.user_data['expected_answer']
        if answer == expected_answer:
            await update.message.reply_text('Correct!')
        else:
            await update.message.reply_text(f'Incorrect! Expected answer: {expected_answer}')
    else:
        await update.message.reply_text(f'Expected digits!')

    expression, expected_answer = generate_expression()
    context.user_data['expected_answer'] = expected_answer
    await update.message.reply_text(expression)

async def weather(update: Update, context: CallbackContext):
    data = await get_weather()
    await update.message.reply_text(f'Temperature: {data["main"]["temp"]} C')

if __name__ == "__main__":
    application = Application.builder().token(os.environ['TELEGRAM_BOT_TOKEN']).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("weather", weather))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_answer))
    application.run_polling()


