from aiogram import types
from bot.info.main_numbs_menu import back_to_main_menu_button

# кнопка возврата в главное меню базовых чисел
back_to_relationships_button = types.InlineKeyboardButton('Назад', callback_data='back_to_relationships_button')

async def relationships(msg: types.Message) -> None:
    main_message = '''<b>Это раздел про нумерологию взаимоотношений.</b>

    И он не требует от Вас печатей. Он просто описывает несколько вероятных совпадений и то, что они приносят.
    Вы можете узнать свои числа и числа Вашей второй половинки в других разделах. Затем зайти сюда и посмотреть на вероятные совпадения.
    <b>Приятного изучения.</b>

    '''

    #главное меню раздела взаимоотношений
    spirit_awake_num_button = types.InlineKeyboardButton('Душевное пробуждение', callback_data='spirit_awake_num_button')
    expression_num_button = types.InlineKeyboardButton('Экспрессия', callback_data='expression_num_button')
    other_num_button = types.InlineKeyboardButton('Другие', callback_data='other_num_button')

    numerology_relationship_keyboard = types.InlineKeyboardMarkup().add(spirit_awake_num_button).add(expression_num_button)\
        .add(other_num_button).add(back_to_main_menu_button)
    await msg.answer(main_message, reply_markup=numerology_relationship_keyboard)



#душевное пробуждение совпадает с одним из чисел нумерологического ядра
spirit_awake_message = '''<b>Число душевного пробуждения</b> совпадает с одним из чисел нумерологического ядра.
При этом совпадении получается самая сильная и устойчивая связь.

Выберите интересующее Вас совпадение.
'''

spirit_awake_with_spirit_awake_button = types.InlineKeyboardButton('Число душевного пробуждения', callback_data='spirit_awake_with_spirit_awake_button')
spirit_awake_with_personality_button = types.InlineKeyboardButton('Число личности', callback_data='spirit_awake_with_personality_button')
spirit_awake_with_expression_button = types.InlineKeyboardButton('Число экспрессии', callback_data='spirit_awake_with_expression_button')
spirit_awake_with_life_path_button = types.InlineKeyboardButton('Число жизненного пути', callback_data='spirit_awake_with_life_path_button')
spirit_awake_with_birthday_button = types.InlineKeyboardButton('Число дня рождения', callback_data='spirit_awake_with_birthday_button')

spirit_awake_keyboard = types.InlineKeyboardMarkup().add(spirit_awake_with_spirit_awake_button).\
    add(spirit_awake_with_personality_button).add(spirit_awake_with_expression_button)\
    .add(spirit_awake_with_life_path_button).add(spirit_awake_with_birthday_button).add(back_to_relationships_button)


spirit_awake_with_spirit_awake_message = '''Если у вас совпадают числа душевного пробуждения, то получается, то вы хотите одного и того же в основном. Хорошо это или плохо? Трудно сказать. Это может быть и хорошо и плохо. У кого как складывается.
Если у вас совпали 1 и 5, то ситуация может быть сложной т.к. не смотря на схожесть интереснов - каждый будет тянуть одеяло на себя. Если двойка и шестёрка, то скорее всего вы будете уступчивы друг перед другом. Остальные числа получаться 50 на 50. Всё будет зависеть от ваших характеров.
'''

spirit_awake_with_personality_message = '''Больше всего реакция идёт при совпадении числа душевного пробуждения с числом личности. Однако такое притяжение может быть слабым, если Ваше число душевного пробуждения не совпадает с другими нумерологическими характеристиками человека.
А при сильном притяжении Вы скорее всего будете выставлять своего партнёра/партнёршу вперёд себя, как бы демонстрируя его внешность, манеры и презентабельность, считая, что так вы оба выглядите гораздо лучше в обществе.
'''

spirit_awake_with_expression_message = '''Это пожалуй самый прочный вариант связи. Всё потому, что число экспресии это не какое-то обещание, а уже случившийся факт. То, что уже есть у человека. Таким образом Вы можете начать чувствовать очень прочную духовную связь друг с другом.
'''

spirit_awake_with_life_path_message = '''В этом случае отношения могут быть самыми стабильными. Дело в том, что число жизненного пути это то, что человек делает на протяжении жизни. Его смысл жизни по сути. Поэтому если Вам это нравится, то и отношения весь этот жизненный путь будут вполне себе приятными для Вас.
'''

spirit_awake_with_birthday_message = '''Здесь во второй половинке Вам может нравится его/её стиль, поведение, подход к вопросу. Эти отношения обещают быть так же долговечны, как и при совпадении с числом жизненного пути.
'''



#экспрессия совпадает с одним из чисел нумерологического ядра
expression_message = '''<b>Число экспрессии</b> совпадает с одним из чисел нумерологического ядра.
Выберите интересующее Вас совпадение.
'''

expression_with_expression_button = types.InlineKeyboardButton('Число экспрессии', callback_data='expression_with_expression_button')
expression_with_personality_button = types.InlineKeyboardButton('Число личности', callback_data='expression_with_personality_button')
expression_with_life_path_button = types.InlineKeyboardButton('Число жизненного пути', callback_data='expression_with_life_path_button')
expression_with_birthday_button = types.InlineKeyboardButton('Число дня рождения', callback_data='expression_with_birthday_button')

expression_keyboard = types.InlineKeyboardMarkup().add(expression_with_expression_button)\
    .add(expression_with_personality_button)\
    .add(expression_with_life_path_button).add(expression_with_birthday_button)\
    .add(back_to_relationships_button)


expression_with_personality_message = '''В этом случае, как и при совпадении с числом дня рождения, партнёры могут сразу узнать друг в друге близкого человека. Однако, если у Вашей половинки число личности перекликается с более глубокими нумерологическими характеристиками, то Ваша связь может начать пропадать при сближении.
'''

expression_with_expression_message = '''Это довольно гармоничное сочитание. Только будьте осторожны, если у Вас совпадают единицы. Это может привести к соперничеству. Постарайтесь использовать свои умения и таланты во благо общего дела. В остальных случаях совпадений Вы вполне сможете друг друга дополнять своими навыками.
'''

expression_with_life_path_message = '''При это совпадении может получится очень хороший союз. Число экспрессии это Ваши таланты и способности, которые могут помогать Вашей второй половинке на всём жизненном пути. Но так же зависит от того, какие числа у Вас совпадают. К примеру 4 и 8 будут хорошим союзом для работы и дел, а 3 или 5 сделают отношения более весёлыми и открытыми.
'''

expression_with_birthday_message = '''При таком совпадении у партнёров возникает ощущение, что они давно друг друга знают. Они словно сразу узнают друг в друге родственную или близкую связь.
'''



#другие совпадения
other_message = '''<b>Иные варианты совпадений</b>.
Выберите интересующее Вас совпадение.

<b>1 - Совпадение чисел жизненого пути
2 - Совпадение числа жизненного пути с числом дня рождения
3 - Числа жизненного пути и дня рождения совпадают с числом личности
4 - Совпадение чисел личности
</b>
'''

life_path_with_life_path_button = types.InlineKeyboardButton('1', callback_data='life_path_with_life_path_button')
life_path_with_birthday_button = types.InlineKeyboardButton('2', callback_data='life_path_with_birthday_button')
life_path_birthday_with_personality_button = types.InlineKeyboardButton('3', callback_data='life_path_birthday_with_personality_button')
personality_with_personality_button = types.InlineKeyboardButton('4', callback_data='personality_with_personality_button')

other_keyboard = types.InlineKeyboardMarkup().row(life_path_with_life_path_button,life_path_with_birthday_button,\
    life_path_birthday_with_personality_button,personality_with_personality_button)\
    .add(back_to_relationships_button)

personality_with_personality_message = '''При таком совпадении Ваши вкусы внешних атрибутов, стилей или украшений могут совпадать, что в принципе и может послужить началом Вашего знакомства. Однако, если другие характеристики или Ваши характеры и взгляды расхожи, то этот союз может быть недолговечным.
'''

life_path_with_life_path_message = '''Это совпадение говорит о схожих судьбах и понимании о том, что у Вас общий совместный путь до самого конца. Если Вы решите начать совместное дело, то оно должно принести хорошие плоды.
'''

life_path_with_birthday_message = '''Интересное совпадение и довольно выгодный союз. Сначала обладатель совпадающего числа на жизненном пути будет зависеть от обладателя числа дня рождения, а затем когда второй разглядит получше своего партнёра, то вы поменяетесь местами в том, кто кому нужнее. В целом будет получаться так, что один помогает другому не сбиваться с пути, а второй ведёт первог по нужной тропе.
'''

life_path_birthday_with_personality_message = '''В данном совпадении внещность и манеры одного человека могут оказаться полезны для того, чем занимается другой человек, если он конечно следует своему пути и использует данные ему инструменты.
'''