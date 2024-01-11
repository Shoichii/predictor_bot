from asgiref.sync import sync_to_async
from magic_numbers import models as mdl
from datetime import datetime
import bot.django_crud_utils as cu

# проверка на новичка. если новенький, то записываем телеграм ID
@sync_to_async()
def check_for_newbie(telegram_id):
    user = mdl.User.objects.filter(telegram_id=telegram_id).first()
    if user:
        return False
    mdl.User.objects.create(telegram_id=telegram_id)
    return True


# запись данных пользователя
@sync_to_async()
def set_new_user_data(telegram_id, name, birthday):
    user = mdl.User.objects.filter(telegram_id=telegram_id).first()
    user.name = name
    birthday = datetime.strptime(birthday, "%d.%m.%Y")
    user.birthday = birthday
    user.seals = 30
    user.save()
    mdl.UserBaseNumbers.objects.create(user=user)



# прочитать количество печатей
@sync_to_async()
def get_seals_amount(telegram_id):
    user = mdl.User.objects.filter(telegram_id=telegram_id).first()
    seals_amount = user.seals
    return seals_amount


# вычесть печати
@sync_to_async()
def minus_seals(telegram_id, price):
    user = mdl.User.objects.filter(telegram_id=telegram_id).first()
    user.seals = user.seals - price
    user.save()


# расчёт числа жизненного пути
@sync_to_async()
def life_path_number_handler(telegram_id):
    user = mdl.User.objects.filter(telegram_id=telegram_id).first()
    numbers = mdl.UserBaseNumbers.objects.filter(user=user).first()
    if numbers.life_path_number:
        return numbers.life_path_number
    birthday = user.birthday.strftime("%d.%m.%Y").split('.')
    life_path_number = cu.calc_life_path_number(birthday)
    numbers.life_path_number = life_path_number
    numbers.save()
    return life_path_number


# расчёт числа дня рождения
@sync_to_async()
def birthday_number_handler(telegram_id):
    user = mdl.User.objects.filter(telegram_id=telegram_id).first()
    numbers = mdl.UserBaseNumbers.objects.filter(user=user).first()
    if numbers.birthday_number:
        return numbers.birthday_number
    birthday = user.birthday.strftime("%d.%m.%Y").split('.')
    birthday_number = cu.calc_birthday_number(birthday)
    numbers.birthday_number = birthday_number
    numbers.save()
    return birthday_number


# расчёт числа экспрессии
@sync_to_async()
def number_of_expression_handler(telegram_id):
    user = mdl.User.objects.filter(telegram_id=telegram_id).first()
    numbers = mdl.UserBaseNumbers.objects.filter(user=user).first()
    if numbers.expression_number:
        return numbers.expression_number
    name = user.name
    expression_number = cu.calc_expression_number(name)
    numbers.expression_number = expression_number
    numbers.save()
    return expression_number


# расчёт числа душевного пробуждения
@sync_to_async()
def spirit_awake_number_handler(telegram_id):
    user = mdl.User.objects.filter(telegram_id=telegram_id).first()
    numbers = mdl.UserBaseNumbers.objects.filter(user=user).first()
    if numbers.spirit_awake_number:
        return numbers.spirit_awake_number
    name = user.name
    spirit_awake_number = cu.calc_spirit_awake_number(name)
    numbers.spirit_awake_number = spirit_awake_number
    numbers.save()
    return spirit_awake_number


# расчёт числа личности
@sync_to_async()
def personality_number_handler(telegram_id):
    user = mdl.User.objects.filter(telegram_id=telegram_id).first()
    numbers = mdl.UserBaseNumbers.objects.filter(user=user).first()
    if numbers.personality_number:
        return numbers.personality_number
    name = user.name
    personality_number = cu.calc_personality_number(name)
    numbers.personality_number = personality_number
    numbers.save()
    return personality_number


# получить базовые числа
@sync_to_async()
def get_base_numbers_data(telegram_id):
    user = mdl.User.objects.filter(telegram_id=telegram_id).first()
    numbers = mdl.UserBaseNumbers.objects.filter(user=user).first()
    return numbers


# информация о пользователе
@sync_to_async()
def get_user_data(telegram_id):
    user = mdl.User.objects.filter(telegram_id=telegram_id).first()
    return user


# новое имя
@sync_to_async()
def set_new_name(telegram_id, name):
    user = mdl.User.objects.filter(telegram_id=telegram_id).first()
    user.name = name
    user.save()


# новая дата дня рождения
@sync_to_async()
def set_new_birthday(telegram_id, birthday):
    user = mdl.User.objects.filter(telegram_id=telegram_id).first()
    birthday = datetime.strptime(birthday, "%d.%m.%Y")
    user.birthday = birthday
    user.save()


# сброс всех чисел
@sync_to_async()
def reset_base_numbers(telegram_id):
    user = mdl.User.objects.filter(telegram_id=telegram_id).first()
    numbers = mdl.UserBaseNumbers.objects.filter(user=user).first()
    numbers.life_path_number = None
    numbers.birthday_number = None
    numbers.expression_number = None
    numbers.spirit_awake_number = None
    numbers.personality_number = None
    numbers.save()


# проверка куплена ли консультация
@sync_to_async()
def check_consultation_buy(telegram_id):
    user = mdl.User.objects.filter(telegram_id=telegram_id).first()
    consultations = mdl.Consultation.objects.filter(user=user,question=None).all()
    if consultations:
        return True
    return False


# записываем вопрос
@sync_to_async()
def set_question(telegram_id, question):
    user = mdl.User.objects.filter(telegram_id=telegram_id).first()
    consultations = mdl.Consultation.objects.filter(user=user,question=None).all()
    if consultations:
        consultation = consultations[0]
        consultation.question = question
        consultation.save()


# сбор общей статистики
@sync_to_async()
def get_all_statistic():
    # за всё время
    all_time_stat_num_core = 0
    all_time_stat_core_synthesis = 0
    all_time_stat_forecast = 0
    counters = mdl.UserDayJournal.objects.all()
    for counter in counters:
        all_time_stat_num_core += counter.numerology_count
        all_time_stat_core_synthesis += counter.core_synthesis
        all_time_stat_forecast += counter.forecast
    purchases = mdl.UserAction.objects.all()
    all_time_purchases = len(purchases)
    all_time_consultations = 0
    all_time_purchases_sum = 0
    for purchase in purchases:
        if purchase.action == 'Консультация':
            all_time_consultations += 1
        all_time_purchases_sum += purchase.money

    # за месяц
    months_stat_num_core = 0
    months_stat_core_synthesis = 0
    months_stat_forecast = 0
    today = datetime.now()
    counters = counters.filter(      
                                date__year=today.year,
                                date__month=today.month,
                            ).all()
    for counter in counters:
        months_stat_num_core += counter.numerology_count
        months_stat_core_synthesis += counter.core_synthesis
        months_stat_forecast += counter.forecast
    purchases = mdl.UserAction.objects.filter(      
                                                date__year=today.year,
                                                date__month=today.month,
                                            ).all()
    months_stat_purchases = len(purchases)
    months_stat_consultations = 0
    months_stat_purchases_sum = 0
    for purchase in purchases:
        if purchase.action == 'Консультация':
            months_stat_consultations += 1
        months_stat_purchases_sum += purchase.money

    return {
        'all_time_stat_num_core': all_time_stat_num_core,
        'all_time_stat_core_synthesis': all_time_stat_core_synthesis,
        'all_time_stat_forecast': all_time_stat_forecast,
        'all_time_consultations': all_time_consultations,
        'all_time_purchases': all_time_purchases,
        'all_time_purchases_sum': all_time_purchases_sum,
        'months_stat_num_core': months_stat_num_core,
        'months_stat_core_synthesis': months_stat_core_synthesis,
        'months_stat_forecast': months_stat_forecast,
        'months_stat_consultations': months_stat_consultations,
        'months_stat_purchases': months_stat_purchases,
        'months_stat_purchases_sum': months_stat_purchases_sum
    }


# получаем телеграм ID всех пользователей
@sync_to_async()
def get_all_users_id():
    users = mdl.User.objects.all()
    users_ids = [user.telegram_id for user in users]
    return users_ids


# добавление или удаление печатей пользователю
@sync_to_async()
def set_seals(telegram_id, seals, action):
        user = mdl.User.objects.filter(telegram_id=telegram_id).first()
        if action == 'add':
            user.seals = user.seals + seals
        else:
            user.seals = user.seals - seals
        user.save()


# проверяем существует ли пользователь
@sync_to_async()
def check_user_exists(telegram_id: int):
    user = mdl.User.objects.filter(telegram_id=telegram_id).first()
    if user: return True
    return False


# считаем статистику за день
@sync_to_async()
def set_stat(telegram_id, section):
    today = datetime.today().date()
    user = mdl.User.objects.filter(telegram_id=telegram_id).first()
    stat_entry = mdl.UserDayJournal.objects.filter(user=user, date=today).first()
    if stat_entry:
        if section == 'numerology_count':
            stat_entry.numerology_count += 1
        elif section == 'core_synthesis':
            stat_entry.core_synthesis += 1
        elif section == 'forecast':
            stat_entry.forecast += 1
    else:
        stat_entry = mdl.UserDayJournal(user=user, date=today, 
                                        numerology_count=0, 
                                        core_synthesis=0, forecast=0)
        if section == 'numerology_count':
            stat_entry.numerology_count = 1
        elif section == 'core_synthesis':
            stat_entry.core_synthesis = 1
        elif section == 'forecast':
            stat_entry.forecast = 1
    stat_entry.save()