from bot.prices import spirit_awake_numbers_price
from aiogram import types

# Описание числа жизненного пути
message_text = f'''
<b>Число душевного пробуждения - 👁 {spirit_awake_numbers_price} печать</b> - показывает то, куда тянется Ваша внутренняя сущность, душа. Какие вещи Вас вдохновляют и к каким Вы стремитесь. То, что Вас мотивирует и направляет, и что вы действительно желаете.
Это во многом определяет Ваши настоящие мысли, эмоции, принципы и т.д.
.'''

#кнопки
get_spirit_awake_numbers_button = types.InlineKeyboardButton(f'Сорвать 👁 печати', callback_data='get_spirit_awake_numbers_button')


info = {
    '1': {
        'img' : 'spirit_awake_numbers_1.png',
        'value' : '''Число душевного пробуждения.

1️⃣ - Ваше желание и рвение - это стремиться вперёд к независимсоти и первенству. Порой Вы так летите впереди всех, что случаются "аварии" с другими людьми и Вам приходиться объясняться, куда Вас так несло. Быть лидером, первым, открывать неизведанное, вести людей за собой - одно или несколько пунктов из этого списка про Вас. Для Вас Ваше же мнение это мнение номер один. Вы не боитесь выделяться, быть оригинальным. А вот рутина и обыденность совсем не Ваша стезя.
'''
    },
    '2': {
        'img' : 'spirit_awake_numbers_2.png',
        'value' : '''Число душевного пробуждения.

2️⃣ - быть известным и выделяться из толпы не для Вас. Вы стремитесь к спокойной жизни с любимым человеком. Поэтому для Вас важно найти своег партнёра и наладить с ним/ с ней тёплые отношения и взаимопонимание. Вы тактичны и дипломатичны, и поэтому добиваетесь своего исключительно из тени, аккуратно, чтобы оставаться незамеченым или с помощью кого-то, кто не боится выходить на общий взор.
'''
    },
    '3': {
        'img' : 'spirit_awake_numbers_3.png',
        'value' : '''Число душевного пробуждения.

3️⃣ - так как это число творческой души, то и человек, чьё число душевного пробуждения равно трём, склонен к творческому проявлению своего внутреннего Я. Вы любите всё необычное и нестандартное, и терпеть не можете рутину и однотипность. Вам очень часто нужно то, что будет Вас вдохновлять на новые образы, которые Вы так или иначе захотите воплотить в реальность. А когда Вы всё таки оказываетесь в рамках каких-либо общепринятых правил, то тройка сразу заставляет Вас начинать поиск того, что выходит за эти рамки. Тем самым Вы всегда способны видеть нечто иное там, где другим это незаметно. И это же делает Вас довольно оригинальным человеком, способным добавить в скуку и рутину что-нибудь новое и интересное.
'''
    },
    '4': {
        'img' : 'spirit_awake_numbers_4.png',
        'value' : '''Число душевного пробуждения.

4️⃣ - Вы желаете и стремитесь к порядку и предсказуемости - чтобы все правила исполнялись, а все вещи находились на своих местах. В таких условиях Вы можете и готовы работать очень продуктивно и результативно. Результаты, кстати, вдохновляют Вас идти к новым вершинам. Когда Вы проделали долгий и тяжёлый путь и получили впечатляющий результат - это разжигает внутри Вас новый огонь и побуждает к новым действиям. А вот в условиях хаоса и неопределённости Ваша работоспособность снижается и вся деятельность идёт коту под хвост. Но всё же благодаря четвёрке Вашей концентрации и желания неустанно двигаться вперёд может позавидовать любой другой человек.
'''
    },
    '5': {
        'img' : 'spirit_awake_numbers_5.png',
        'value' : '''Число душевного пробуждения.

5️⃣ - человек со свободной и стремительно душой. В любовных делах, как и в целом в жизни, Вам трудно быть постоянным. Безусловно Вы на это способны, но в душе будете мечтать постоянно о новом и ярком. Вы из тех людей, для кого рутина и закрытые пространства - это невыносимо. Путешествия, закомства, новые люди, новые занятия - это про Вас. Вам интересно всё и сразу. Вы способны сидеть на нескольких стульях сразу и раздавать и кучу обещаний. Вы искренне надеятесь их выполнить, но порой это просто невозможно, а некоторые обещания требуют долгой концентрации, что тоже не соотносится с пятёркой.
'''
    },
    '6': {
        'img' : 'spirit_awake_numbers_6.png',
        'value' : '''Число душевного пробуждения.

6️⃣ - обладатель этого числа хочет видеть вокруг гармонию во всём и особенно в человеческих отношениях. Вы так же хотите любить и быть любимыми и проводить больше времени в кругу семьи. По этой причне вполне вероятно, что Вы можете стать домоседом, чтобы проводить больше времени с близкими или Вы просто можете подумывать/мечтать об этом.
Кроме того число душевного пробуждения 6, говорит о том, что Вас может привлекать деятельность, связанная с оказанием помощи людям или забота о людях. Некоторое влияние в обществе могло бы поспособствовать Вам в вполощении желания наведения гармонии и порядка среди людей и в обществе. За неимением такого влияния, Вы вполне можете выступать неплохим советчиком в делах, связанных с человческими отношениями.
'''
    },
    '7': {
        'img' : 'spirit_awake_numbers_7.png',
        'value' : '''Число душевного пробуждения.

7️⃣ - Ваша душевная семёрка может делать Вас слегка странным человеком, выделять Вас из толпы, но для Вас это не проблема, а порой даже наоборот. Ваше стремление и желание познать тайны вселенной и докапаться до сути и мелочей всего и вся, порой не даёт Вам построить нормальные доверительные отношения, т.к. Вы будете везде искать подвох, считая, что не всё так очевидно и однозначно. Однако, Ваш беспокойный ум тянет Вас к познаниям тайн и глубин рахного рода наук и детяльностей. Вы легко способны сосредоточится на чём-то одном и капаться там до конца своих дней или пока не достигните истинного понимания. Ваша мечта это жизнь в уединении в каком-нибудь уютном доме или лаборатории и изучение разного рода тайн, и всякое терзание знаниями собственного разума.
'''
    },
    '8': {
        'img' : 'spirit_awake_numbers_8.png',
        'value' : '''Число душевного пробуждения.

8️⃣ - Вы не боитесь работы и если Вам нужно сделать какую-то работу, то Вы не будете делать её в одиночку, а обязательно убедите кого-то(это может быть и несколько людей) помочь Вам с этим. В одиночку результаты будут не впечатляющими, в то время как в команде Вы способны добиваться многого, а положительные результаты Вашей деятельности способны подталкивать Вас на новые свершения. Вы способны влиять на людей, не силой, не своим положением в обществе, а скорее своим обаянием, своей личностью и силой энергии.
'''
    },
    '9': {
        'img' : 'spirit_awake_numbers_9.png',
        'value' : '''Число душевного пробуждения.

9️⃣ - Стремясь осчастливить человечество, Вы можете принебрегать отношениями с близкими людьми - из-за чего с Вами в отношениях бывает нелегко. Зато Вы обладаете дальнозоркостью и масштабным мышлением, хоть порой и не представляете, как осуществить столь масштабные замыслы. Поэтому не все из Ваших проектов могут быть вполощены в жизнь. Вы так же нередко думаете о далёких странах, других временах и разного рода великих свершениях. Вам хочется всё это сохранить, приумножить и улучшить. Сделать людей счастливее, прекратить множество страданий на Земле и облагородить природу, чтобы её меньше портили и засоряли. Ваши замыслы уходят далеко за пределы обыденной жизни.
'''
    },
    '11': {
        'img' : 'spirit_awake_numbers_11.png',
        'value' : '''Число душевного пробуждения.

1️⃣1️⃣ - ещё с самого детства Вы могли отличаться от других детей своей совсем недетской мудростью. Однако, если Вы посчитали, что гораздо выгоднее не выделяться, то ваше мастер-число душевного пробуждения 11 могло сложиться в простую двойку, где Вам стало гораздо интереснее искать себе вторую половинку и строить хорошие, взаимоуважительные и крепкие отношения. А если же с Вами осталось 11, то скорее всего Вы имеете довольно сильную и развитую интуицию, которая помогает Вам во многом. Правда, возможно, Вы не всегда умеете хорошо её слушать и ещё хуже выражаете свои ощущения другим людям, которые просто Вас не понимают. Если Вы научитесь показывать людям свои образы и чувства, которые получаете от интуиции, то увидете, как приятно удивите людей своими способностями, которые порой могут доходить до экстрасенсорных.
'''
    },
    '22': {
        'img' : 'spirit_awake_numbers_22.png',
        'value' : '''Число душевного пробуждения.

2️⃣2️⃣ - Вам лучше бы посвятить себя какому-то определённому делу, в противном случае 22 станет простой 4, где Вы будете трудолюбивым и безусловно ответственным человеком, однако уже не сможете достигать столь великих и грандиозных целей, как если бы у Вас было число 22. Ведь с ним Вы способны организовывать большие ресурсы и в том числе и людей на свершение великих дел и строительство крупных проектов. Вы будете способны работать много и упорно ради достижения своей цели и привлекать множество людей к своей задмуке. Кстати, человек с числом душевного пробуждения 22 не обязательно может быть лидером и выделяться среди других. Он может быть и небольшим винтиком в компании. Однако, без этого винтика ничего глобального с места не сдвинется.
'''
    },
    '33': {
        'img' : 'spirit_awake_numbers_33.png',
        'value' : '''Число душевного пробуждения.

3️⃣3️⃣ - Вы желаете, чтобы весь мир жил в согласии и гармонии. Вы бы хотели бы быть государственным деятелем или проповедником новой веры/религии/знаний. С одной стороны вы представитель идеализма, а с другой стороны столько несовершнных человеческих систем. Но тем не менее, Вы бы и хотели вклиниться в одну из них или сразу в несколько, чтобы улучшать их и нести людям просветление и знания. Если Вы научитесь взаимодействовать с научными, учебными и другими подобного рода организациями, то у Вас всё получится и Ваша душа получит то, чего так хотела.
'''
    }
}