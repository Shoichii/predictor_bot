from aiogram.dispatcher.filters.state import State, StatesGroup


class User_Data_State(StatesGroup):
    name = State()
    birthday = State()


class User_Data_Change(StatesGroup):
    name_change = State()
    birthday_change = State()


class Numbers(StatesGroup):
    first_numb = State()
    second_numb = State()
    individual_year = State()
    individual_month_year = State()
    individual_month_month = State()
    individual_day_month = State()
    individual_day_day = State()


class Adm(StatesGroup):
    message_for_all = State()
    text_for_all = State()
    photo_for_all = State()
    consult_action = State()
    seals_action = State()
    user_id = State()
    answer = State()