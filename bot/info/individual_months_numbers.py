from bot.prices import individual_months_number_price
from aiogram import types

# Описание числа жизненного пути
message_text = f'''
<b>Индивидуальные месяцы - 👁 {individual_months_number_price} печать</b>

<b>ВНИМАНИЕ!!!</b>
Для расчёта индивидуального месяца необходимо будет указать число Вашего индивидуального года. Если Вы его не знаете, то вернитесь назад и расчитайте для начала число индвидуального года. А затем возвращайтесь сюда.

Индивидуальный месяцы, как и годы также чередуются. Начинаются с 1 и заканчиваются 9, и потом снова 1. И так по кругу. И как и годы имеют похожие характеристики, только масштабом меньше.
Опять таки, какие-то общие черты будут присущи постоянно всем месяцам соответствующих цифр, но ещё они будут и различаться под влиянием остальных нумерологических характеристик, а так же под Вашей собственной волей.
<b>Подробнее можно узнать в личной консультации у нумеролога.</b>
'''

#кнопки
get_individual_months_numbers_button = types.InlineKeyboardButton(f'Сорвать 👁 печати', callback_data='get_individual_months_numbers_button')


info = {
    '1': {
        'img' : 'individual_months_numbers_1.png',
        'value' : '''1️⃣ - в этом месяце забудте обо всём прошлом и смотрите только в будущее: рискуйте и действуйте. И делайте это самостоятельно, не оглядываясь и не опираясь ни на кого. Это самый подходящий месяц для чего-либо нового: работа, хобби, увлечения, друзья, отношения. Оставайтесь собой и не бойтесь подчёркивать свою индвидуальность.
'''
    },
    '2': {
        'img' : 'individual_months_numbers_2.png',
        'value' : '''2️⃣ - в этом месяце рекоменуется больше быть спокойным и обращать внимание на мелочи и детали. А также, разные намёки. Подумайте над тем, что они могли бы для Вас значить. Не стоит позволять своим эмоциям брать над Вами верх. Бурная активность была в предыдущем месяце, а сейчас старайтесь быть больше наблюдателем. Кроме того, Вы можете оказать поддержку людям со стороны и вполне вероятно, что некоторые из них станут к Вам ближе, чем были до этого.
'''
    },
    '3': {
        'img' : 'individual_months_numbers_3.png',
        'value' : '''3️⃣ - если есть возможность - возьмите отпуск. Этот месяц хорош для творчества, воображения и всего того, что Вам очень нравится. Скучную рутину и обязанности желательно отложить на потом.
'''
    },
    '4': {
        'img' : 'individual_months_numbers_4.png',
        'value' : '''4️⃣ - в это месяце рекомендуется заняться настоящим трудом, делом и наведением порядка. Если Вы будете практичны, рациональны, следовать правилам и некой системе, то значительно преуспеете в своих делах.
'''
    },
    '5': {
        'img' : 'individual_months_numbers_5.png',
        'value' : '''5️⃣ - если Вы привыкли к спокойствию, то этот месяц может показаться Вам слишком сумбурным, хаотичным и суматошным. В противном случае, рекомендуется включится в этот энергетический поток и позволить себе брать от жизни всё: встреча с новыми людбми, разные и разнообразные виды хобби/деятельности, посещение различных мест. Кроме того, в это месяце могут произойти разного рода изменения в некоторых областях Вашей жизни.
'''
    },
    '6': {
        'img' : 'individual_months_numbers_6.png',
        'value' : '''6️⃣ - этот месяц хорош для заключения брака, началу новых романтических отношений и уделению внимания семье и близким. Рекомендуется проявлять больше тепла и заботы к тем, кто Вам дорог. Чем больше Вы отдадите на это своих сил, тем больше вознаграждений от жизни получите. Кроме того, в этом месяце будет благоприятным занятие творчеством, искусством.
'''
    },
    '7': {
        'img' : 'individual_months_numbers_7.png',
        'value' : '''7️⃣ - в этом месяце лучше всего будет открыта интуиция. Так что чаще прислушивайтесь к ней и к своему внутреннему миру, а также, к своим снам. Рекомендуется больше времени уделять в уединении в размышлениях или углубленном изучении чего-либо. Можно заняться исследованиями и/или расследованиями. Всем тем, что разомнёт Ваш ум.
'''
    },
    '8': {
        'img' : 'individual_months_numbers_8.png',
        'value' : '''8️⃣ - в этом месяце попробуйте влиять на других людей и подчинять их своей воле - вполне вероятно, что у Вас это будет получаться. Этот месяц хорош для заработка денег. Так что если у Вас выпадает возможность подработать, взяв на себя какую-либо ответственность, то не бойтесь соглашаться. Действуйте смело и уверенно, особенно если появляется возможность поруководить и организованно достичь каких-либо результатов. Кроме того, этот месяц может наполнить Вашу личность имиджем успешногоо человека. Даже если внешне ничего не поменяется, то какое-то обояние Вы всё же приобретёте.
'''
    },
    '9': {
        'img' : 'individual_months_numbers_9.png',
        'value' : '''9️⃣ - месяц щедрости. Отдавайте другим и будете вознаграждены. В этом месяце лучше всего завершить многие свои дела и приготовится к новому эпициклу. Это можно сделать подумав о том, что можно оставить в прошлом и позади и о том, что бы Вы хотели видеть в будущем. Стремиться вперёд не нужно, просто пока подумайте о том, что хотели бы видеть впереди.
'''
    }
}
