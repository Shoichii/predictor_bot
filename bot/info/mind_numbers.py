from bot.prices import mind_number_price
from aiogram import types

# Описание числа жизненного пути
message_text = f'''
<b>Число разума - 👁 {mind_number_price} печать</b> - это число является сопоставлением характеристик имени и даты рождения. Оно отражает способ мышления человека. По нему можно определить способ подачи информации человеку или метод его обучения. В более широком смысле это число показывает, как человек воспринимает реальность вокруг себя. И так как информацию извне мы обрабатываем своим разумом, поэтому это число и называется числом разума.
'''

#кнопки
get_mind_numbers_button = types.InlineKeyboardButton(f'Сорвать 👁 печати', callback_data='get_mind_numbers_button')


info = {
    '1': {
        'img' : 'mind_numbers_1.png',
        'value' : '''1️⃣ - лучший метод обучения для Вас - это самостоятельное обучение. Своё мнение Вы цените гораздо больше, чем чужое и в целом имеете независимое свободное мышление. Любите упрощенность и логичность.
'''
    },
    '2': {
        'img' : 'mind_numbers_2.png',
        'value' : '''2️⃣ - наиболее подходящий метод обучение - это обучение с преподавателем, с которым Вы не имеете никаких трудностей в отношениях. Вы придаёте большое значение деталям и нюансам. А также, способны видеть обратные стороны вещей. Отсюда бывают сложности с принятием решений. Ещё Вы прислушиваетесь и очень восприимчивы к мнению других людей.
'''
    },
    '3': {
        'img' : 'mind_numbers_3.png',
        'value' : '''3️⃣ - для Вас лучшим методом обучения будет в форме игры. Не стереотипное и творческое мышление делает Вас хорошим генератором идей, особенно когда требуется свежий взгляд на вещи. Однако, если нужно иметь дело с фактами, документами и в целом тем, что Вам не нравится, то тут могут возникать трудности.
'''
    },
    '4': {
        'img' : 'mind_numbers_4.png',
        'value' : '''4️⃣ - здесь лучшим методом обучения будет практика. Именно на практике Вы лучше всего сможете оттачивать новые знания. Вам тип мышления склонен к формированию шаблоном и систематизированности. И благодаря этому мышлению Вы способны воспринимать даже не интересную и порой даже сложную информацию. Процесс восприятия может быть не быстрым, но результативным.
'''
    },
    '5': {
        'img' : 'mind_numbers_5.png',
        'value' : '''5️⃣ - обучаться Вы способны лучшего всего взаимодействуя с окружающим миром и людьми. Вы способны схватывать информацию на лету и быстро ориентироваться, благодрая гибкому уму и разносторонности.
'''
    },
    '6': {
        'img' : 'mind_numbers_6.png',
        'value' : '''6️⃣ - для лучшего восприятия информации извне для Вас важен эмоциональный и физический комфорт, а также, хорошие отношения с преподавателем. Легче и ближе по душе для Вас информация, которая связана с семьёй, жизнью в обществе или искусством.
'''
    },
    '7': {
        'img' : 'mind_numbers_7.png',
        'value' : '''7️⃣ - самым надёжным и лучшим способом обучение является самостоятельное и без вмешательств со стороны. Вы склонны к разгадыыванию тайн и загадок, порой интересуетесь чем-то непознанным и таинственным. Вам нравится терзать своё разум разными аналитическими загадками или глубоким познанием чего-либо.
'''
    },
    '8': {
        'img' : 'mind_numbers_8.png',
        'value' : '''8️⃣ - для Вас лучшим способом обучения являются семинарские занятия, где присутствует множество людей. Вы любите производить впечатление на других людей своими знаниями, иногда участвуете в дискуссиях. И хорошо понимаете, какую силу дают знания.
'''
    },
    '9': {
        'img' : 'mind_numbers_9.png',
        'value' : '''9️⃣ - лучший способ познания это лекции талантливых людей. Кроме того, вероятно, Вам захочется делиться своими знаниями с теми, кто не знаком с этими темами. У Вас творческий ум, не придующий большого смысла практической стороне дела.
'''
    },
}