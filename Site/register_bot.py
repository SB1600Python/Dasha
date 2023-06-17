import logging

from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ParseMode
import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, executor, types 

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Site.settings")


import django
django.setup()

from django.contrib.auth.models import User
from blog.models import Profile
from asgiref.sync import sync_to_async

def check_password(password):
    if len(password) <= 8:
        return not password
    elif len(password) >8 and len(password) < 26:
        if not password.istitle():
            return not password
        else:
            return password

API_TOKEN = '6060836398:AAF2QTJ0HYWkwQMTy_MlqCkBK2YVdwQhBTU'

bot = Bot(token=API_TOKEN)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

b1 = types.KeyboardButton('/Yes')
b2 = types.KeyboardButton('/No')
b3 = types.KeyboardButton('/Login')
b4 = types.KeyboardButton('/Password')
b5 = types.KeyboardButton('/Cancel')

key_client_1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
key_client_1.row(b1, b2)
key_client_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
key_client_2.row(b3, b4)
key_client_3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
key_client_3.add(b5)

class RegistrationForm(StatesGroup):
    login = State()
    password = State()

@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    if message.text == '/start':
        await message.answer(
            'Hi! %s!\nI am register bot.\nAre you ready?' % message.from_user.full_name, 
            reply_markup=key_client_1
        )
    elif message.text == '/help':
        await message.answer('Write /start')

@sync_to_async
def check_user(username):
    try:
        profile = Profile.objects.get(username=username)
        if profile:
            return False
        else:
            return True
    except:
        return True

@dp.message_handler(commands=['Yes', 'No'])
async def check_answer(message: types.Message):
    if message.text == '/Yes':
        await RegistrationForm.login.set()
        await message.reply('Write login')
    elif message.text == '/No':
        await message.answer('Are you want registration?')
    else:
        markup = types.ReplyKeyboardRemove()

@dp.message_handler(state='*', commands=['Cancel'])
@dp.message_handler(Text(equals='Cancle', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return False
    
    logging.info('Cancelling state', current_state)
    await state.finish()
    await message.reply('Cancel', reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(state=RegistrationForm.login)
async def process_login(message: types, state: FSMContext):
    async with state.proxy() as data:
        data['login'] = message.text

        await RegistrationForm.next()
        await message.reply("Input password: ")

@dp.message_handler(lambda message: not check_password(message.text), state=RegistrationForm.password)
async def process_password_invalid(message: types):
    return await message.reply("Пароль повинен бути з великої літери та в паролі повинно бути більше 8 символів")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)