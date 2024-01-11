from bot.loader import dp
from aiogram import types
import os
import re
import bot.django_crud as dj
import bot.states as st
from aiogram.dispatcher import FSMContext
from bot.utils import main_buttons, random_message
from random import randint
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

ADM_IDS = os.environ.get('ADM_IDS')

@dp.message_handler(commands=['start'])
async def start_menu(msg: types.Message):
    # меню для админов
    if str(msg.from_user.id) in ADM_IDS:
        pass
    # меню для клиентов
    else:
        # регистрация для новичков
        newbie = await dj.check_for_newbie(msg.from_user.id)
        if newbie:
            current_dir = os.getcwd()
            file_path = os.path.join(current_dir, 'bot', 'imgs', 'main.jpg')
            with open(file_path, 'rb') as photo:
                file = types.InputFile(photo)
                await msg.answer_photo(photo=file, caption='''👋Привет! Я нумеролог. 

🔮Хочу провести Вас по пути мира чисел и показать, насколько глубока кроличья нора.🔮

Но прежде, расскажите немного о себе.
Напишите свои ФИО полностью - это мне лучше поможет найти Ваши личные числа.''')
                await st.User_Data_State.name.set()
        else:
            numbers_button = types.KeyboardButton(main_buttons[1])
            base_address = os.environ.get('BASE_ADDRESS')
            web_app = types.web_app_info.WebAppInfo(url=f'{base_address}donate')
            shop_button = types.KeyboardButton(main_buttons[0], web_app=web_app)
            help = types.KeyboardButton(main_buttons[2])
            data = types.KeyboardButton(main_buttons[3])
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.row(shop_button, numbers_button).row(help, data)
            random_index = randint(0,  len(random_message) - 1)
            message = random_message[random_index]
            await msg.answer(message, reply_markup=keyboard)

# запоминаем имя пользователя
@dp.message_handler(state=st.User_Data_State.name)
async def rememmber_name(msg: types.Message, state: FSMContext):
    string = msg.text
    contains_digit = any(char.isdigit() for char in string)
    if contains_digit:
        await msg.answer('Имя не должно содержать числа')
        return
    await state.update_data(name=msg.text)
    await msg.answer('Отлично! Теперь напишите свой день рождения, например: 01.01.1970')
    await msg.answer('''P.S.
Если вдруг захочется исправить имя или дату рождения,
позже Вы без проблем сможешь это сделать.😉''')
    await st.User_Data_State.birthday.set()

# получаем пользователя день рождения и записываем все данные в бд
@dp.message_handler(state=st.User_Data_State.birthday)
async def set_user_data(msg: types.Message, state: FSMContext):
    date_regex = re.compile(r'^\d{2}\.\d{2}\.\d{4}$')
    match = date_regex.search(msg.text)
    if not match:
        await msg.answer('В сообщении должна быть только дата формата ХХ.ХХ.ХХХХ(пример: 01.01.1970)')
        return
    
    state_data = await state.get_data()
    name = state_data.get('name')
    await dj.set_new_user_data(msg.from_user.id, name, msg.text)
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, 'bot', 'imgs', 'eye.jpg')
    with open(file_path, 'rb') as photo:
        file = types.InputFile(photo)
        numbers_button = types.KeyboardButton(main_buttons[1])
        base_address = os.environ.get('BASE_ADDRESS')
        web_app = types.web_app_info.WebAppInfo(url=f'{base_address}donate?')
        shop_button = types.KeyboardButton(main_buttons[0], web_app=web_app)
        help = types.KeyboardButton(main_buttons[2])
        data = types.KeyboardButton(main_buttons[3])
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.row(shop_button, numbers_button).row(help, data)
        await msg.answer_photo(photo=file, caption='''Рад познакомится.😌 Взамен я дарю Вам 30 👁 печатей и расскажу о себе. Ниже Вы видите главное меню:

🔮 Нумерология - самый главный раздел, в котором Вы можете узнать больше о себе и обо всех, о ком пожелаешь.
🪄 Магазин - здесь Вы можете получить больше печатей 👁 и личную консультацию!
🆘 Помощь - в этом разделе Вы найдёте подсказки по взаимодействию со мной, а также возможность связаться с поддержкой.
📄 Данные - в этом разделе Вы можете изменить ФИО и дату рождения.
Просчитав свои числа, Вы можете просчитать числа своих близких, друзей
и знаменитостей. Просто напишите их ФИО и дату рождения!

И наконец, что же такое печати 👁? 
Это то, что я беру взамен за знания, которые даю.
Всё покрыто туманом неведения, пока не будут сорваны печати.
''', reply_markup=keyboard)
    await state.finish()

