import json
import os
import random
from dataclasses import dataclass

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import aiohttp
import asyncio


@dataclass
class Choice:
    text: str
    votes: int


@dataclass
class Question:
    text: str
    choices: list[Choice]

    def get_choice_by_text(self, choice_text):
        for choice in self.choices:
            if choice.text == choice_text:
                return choice
        return None


def read_questions():
    questions = []
    with open('data.json') as f:
        data = json.load(f)
        for question_text, choices_data in data.items():
            question = Question(question_text, [])
            for choice_text, votes in choices_data.items():
                choice = Choice(choice_text, votes)
                question.choices.append(choice)
            questions.append(question)
    return questions


QUESTIONS = read_questions()


def get_random_question():
    return QUESTIONS[random.randint(0, len(QUESTIONS) - 1)]


async def ask_question(update: Update, context: CallbackContext, question: Question):
    context.user_data['question'] = question
    choice_texts = [[choice.text for choice in question.choices]]
    await update.message.reply_text(question.text,
                                    reply_markup=ReplyKeyboardMarkup(choice_texts,
                                                                     one_time_keyboard=True))


async def start(update: Update, context: CallbackContext):
    await update.message.reply_html(rf"Hi {update.effective_user.mention_html()}!")

    question = get_random_question()
    await ask_question(update, context, question)


async def check_answer(update: Update, context: CallbackContext) -> None:
    answer = update.message.text
    question: Question = context.user_data['question']
    selected_choice = question.get_choice_by_text(answer)
    if not selected_choice:
        await update.message.reply_text('You should select from the provided choices.')
    else:
        selected_choice.votes += 1
        choice_statistic = '\n'.join(
            [f'{choice.text} -- {choice.votes}' for choice in question.choices])
        await update.message.reply_text(f'Thanks for the answer! Statistic:\n{choice_statistic}')
        question = get_random_question()

    await ask_question(update, context, question)


if __name__ == "__main__":
    application = Application.builder().token(os.environ['TELEGRAM_BOT_TOKEN']).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_answer))
    application.run_polling()
