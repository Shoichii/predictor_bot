from aiogram import types
from numerologist.settings import ADM_IDS
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

async def show_adm_menu(statistic, msg):
    all_time_stat_num_core = statistic.get('all_time_stat_num_core')
    all_time_stat_core_synthesis = statistic.get('all_time_stat_core_synthesis')
    all_time_stat_forecast = statistic.get('all_time_stat_forecast')
    all_time_consultations = statistic.get('all_time_consultations')
    all_time_purchases = statistic.get('all_time_purchases')
    all_time_purchases_sum = statistic.get('all_time_purchases_sum')
    months_stat_num_core = statistic.get('months_stat_num_core')
    months_stat_core_synthesis = statistic.get('months_stat_core_synthesis')
    months_stat_forecast = statistic.get('months_stat_forecast')
    months_stat_consultations = statistic.get('months_stat_consultations')
    months_stat_purchases = statistic.get('months_stat_purchases')
    months_stat_purchases_sum = statistic.get('months_stat_purchases_sum')

    message = f'''<b>Статистика</b>

<b>За месяц</b>
<b>Посещение нумерологического ядра:</b> {months_stat_num_core} раз
<b>Посещение синтеза ядра:</b> {months_stat_core_synthesis} раз
<b>Посещение прогноза:</b> {months_stat_forecast} раз
<b>Покупка личных консультаций:</b> {months_stat_consultations} раз
<b>Всего покупок:</b> {months_stat_purchases} раз
<b>Общая сумма покупок:</b> {months_stat_purchases_sum} рублей

<b>За всё время</b>
<b>Посещение нумерологического ядра:</b> {all_time_stat_num_core} раз
<b>Посещение синтеза ядра:</b> {all_time_stat_core_synthesis} раз
<b>Посещение прогноза:</b> {all_time_stat_forecast} раз
<b>Покупка личных консультаций:</b> {all_time_consultations} раз
<b>Всего покупок:</b> {all_time_purchases} раз
<b>Общая сумма покупок:</b> {all_time_purchases_sum} рублей

<b>Оповещатель</b> - нажми, чтобы написать сообщение всем участникам бота.

<b>Печати</b> - начислить печати или отнять

<b>Заявки</b> - заявки на консультации
        '''
    base_address = os.environ.get('BASE_ADDRESS')
    web_app = types.web_app_info.WebAppInfo(url=f'{base_address}queries')
    queries_button = types.InlineKeyboardButton(text='Заявки', web_app=web_app)
    speaker_button = types.InlineKeyboardButton('Оповещатель', callback_data='speaker_button')
    add_or_del_seals_button = types.InlineKeyboardButton('Печати', callback_data='add_or_del_seals_button')
    keyboard = types.InlineKeyboardMarkup().add(speaker_button).add(add_or_del_seals_button)\
    .add(queries_button)
    await msg.answer(message, reply_markup=keyboard, parse_mode='HTML')