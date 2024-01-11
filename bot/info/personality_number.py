from bot.prices import personality_numbers_price
from aiogram import types

# Описание числа жизненного пути
message_text = f'''
<b>Число личности - 👁 {personality_numbers_price} печать</b> - в нумерологии число личности ассоциируется с телом, с тем, что всем видно вне зависимости, хочет челове кэтого или нет.
Это то, что у Вас уже есть по факту: качества, навыки и прочее. Нравятся они Вам или нет, используете Вы их или нет. Они у Вас просто есть и этого не изменить. Кроме того, число личности тесно связано с число душевного пробуждения.
'''

#кнопки
get_personality_numbers_button = types.InlineKeyboardButton(f'Сорвать 👁 печати', callback_data='get_personality_numbers_button')


info = {
    '1': {
        'img' : 'personality_numbers_1.png',
        'value' : '''Число личности.

1️⃣ - имидж единицы это рвение, инициативность, решительность и готовность рисковать.  Вы производите впечатление уверенного в себе человека, энергичного и самодостаточного. Предпочитаете иметь дело я с такими же яркими личностями как Вы сами. Вам важно поддерживать себя в спортивной форме. Если Вы долго сидите перед компьютером или просто за фоисным столом, то необходимо подумать о нагрузках, которые будут разгонять кровь и разжигать тепло в мышцах. 
В одежде единица предполагает насыщенные яркие цвета, в том числ жёлтый, красный и оранжевый.
'''
    },
    '2': {
        'img' : 'personality_numbers_2.png',
        'value' : '''Число личности.

2️⃣ - имидж двойки это мягкость, внимательность к деталям, готовность к компромиссам и часто - это интерес к искусству. Вы всем своим видом словно приглашаете других к диалогу, чтобы выслушать, понять, посочувствовать. Но в то же время Вы не станете тратить последние силы или отдавать всего себя чужой проблеме т.к. для Вас важен баланс и равновесие. Чтобы избавиться от груза чужих забот Вам нужен спокойный отдых, к примеру на природе. Кроме того, очень важно иметь стабильные и тёплые отношения с любимым человеком. Находясь в паре, двойка усиливает себя многократно. 
Характерная для Вас одежда содержит спокойные цвета и оттенки, схожие с теми, что есть в окружающей природе. Из украшений Вам больше подойдут те, что содержат природные матриалы: камни, жемчуг, дерево.
'''
    },
    '3': {
        'img' : 'personality_numbers_3.png',
        'value' : '''Число личности.

3️⃣ - во многих случаях тройка - это привлекательная внешность. А имидж тройки предполагает общительность и оптимизм, а так же талант быть хорошим рассказчиком, но в том же время и отличным слушателем. С таким слушателем как Вы люди готовы выкладывать о себе буквально всё. Скорее всего, Вы имеете неплохое чувство юмора и умеете радоваться жизни и всему вокруг. Вас тянет к людям, которые способны делать что-либо необычное и оригинальное. К Вам могут часто обращаться на улице спросить время или как куда-либо пройти - настолько Вы способны привлкать людей. И для Вас это важно, т.к. для трок необходимо общение - освобождать голову от накопившихся мыслей, идей и образов, иначе они будут скапливаться и вызывать дискомфорт. 
Характерная одежда тройки это что-то оригинальное и неповторимое с самыми разными украшениями. То, что отражает вкус носителя такой одежды.
'''
    },
    '4': {
        'img' : 'personality_numbers_4.png',
        'value' : '''Число личности.

4️⃣ - Вы предпочитаете иметь дело с людьми, которым можете помочь в работе или они Вам могут помочь. Ваш вид показывает, как будто вы постоянно заняты чем-то очень важным и Вас не нужно отвлекать. А для имиджа четвёрки в целом характерны серьёзность, ответственность и надёжность. Поэтому в весёлых компаниях Вы будете восприниматься как угрюмый и без чувства юмора. Но обратная сторона монеты в том, что Ваш вид показывает, что Вы очень надёжная личность и если Вам что-то доверить, то Вы обязательно это выполните.
Вас тяготят моменты вынужденного безделия в жизни и их хочется устранять хоть какими-то действиями, хоть немножко полезных дел за день. И Вы способны постоянно трудится только в условиях спокойствия и неторопливости и совершенно не можете работать с людьми, которые творят хаос, излучают через чур много энергии, скоростные и переменчивые.
Для Вас характерен деловой стиль одежды, официальный, иногда немного старомодная или Вам может нравится Ваша униформа, если она предполагается на работе. 
'''
    },
    '5': {
        'img' : 'personality_numbers_5.png',
        'value' : '''Число личности.

5️⃣ - Ваш имидж это разносторонность и любознательность. Вы способны сопостоавлять множество разных мнений и собирать из них как конструктор одно своё мнение на все случаи жизни. Поэтому Вы стремитесь общаться со всеми всегда и везде, лишь бы развеять свою скуку или извлечь из общения что-то необходимое и ползеное. К Вам можно обращаться абсолютно по любому вопросу и Вы готовы будете помочь, обсудить и всё решить. Но только если конкретное дело не занимает много времени, потому что Вы не способны долго концентрироваться на чём-то одном из-за большого количества интересов.
В одежде для Вас характерны совршенно разные стили или их смешение. Вы часто меняете наряды и сочитаете невосмстимы вещи, которые в итоге выглядят привлекательно вместе.
'''
    },
    '6': {
        'img' : 'personality_numbers_6.png',
        'value' : '''Число личности.

6️⃣ - быть хорошим семьянином или интересоваться жизнью общества - это Ваш имидж. Вы приятны и мягки в общении и умеете тонко распоряжаться делами, чтобы всё решать и никого не обижать. Без криков и ссор Вы способны поставить на место кого угодно, т.к. знаете за какие рычаги нужно дёргать, чтобы успокоить человека. Однако, старатесь избегать общения с конфликтными или нетактичными людьми.
К Вам часто тянуться более слабые люди, потому что находят в Вашей личности покой и равновесие для себя.
Личность шестёрки уделяет большое внимание своей внешности. Вы тщательно подходите к выбору стилей, цветов и тому, что будете надевать. А украшения это обязательный атрибут всего образа.
'''
    },
    '7': {
        'img' : 'personality_numbers_7.png',
        'value' : '''Число личности.

7️⃣ - имидж семи это загадочность и скрытность. Люди личности семи себе на уме, знающие гораздо больше, чем окружающие. И так же предпочитают общение с людьми, которые глубоко в чём-то разбираются. Если же Вы попадёте в поверзностную и обыденную беседу, то будете чувствовать себя неуютно, а в худшем случае будете проявлять заносчивость и высокомерие. Круг общения для Вас это люди эзотерики, психологи, астрономы и прочее подобное - всё то, что недоступно простым обывателям.
В одежде Вы обычно консервативны и не особо следите за модой. Однако, Вам подойдут совершенно разные образы: от неряхи, который не следит за собой, до профессора в классическом старомодном, но ресспектабельном костюме.
'''
    },
    '8': {
        'img' : 'personality_numbers_8.png',
        'value' : '''Число личности.

8️⃣ - восьмёрки это люди, которые стараются привлечь к себе внимание других людей, используя совершенно разные образы. Однако, среди представителей числа личности 8 есть и те, кто привлекает людей просто своим сущсвованием или природным обянием. Вам нравится больше иметь дело с теми, кто больше всего подвержен Вашему влиянию. А если рядом оказывается тот, кто пытается навязать своё влияние, то Вы стараетесь его избегать или вступаете в конфликт.
Ваша одежда зависит от Вашего образа, который вы используете для заманивания других людей в Ваши сети.
'''
    },
    '9': {
        'img' : 'personality_numbers_9.png',
        'value' : '''Число личности.

9️⃣ - Вы живёте для других и открыты каждому - всё ради человечества и ничего себе. Поэтому люди невольно тянуться к Вам, однако, Вы не способны уделять много внимания кому-то конкретному, потому что Ваши замыслы раздачи изобилия слишком масштабны и нет времени на кого-то конкретного.
Характерный стиль одежды это нечто оригинальное и возможны яркие цвета, чтобы выделяться среди других. Кроме того, Вы предпочитает часто менять наряды, чтобы производить новое впечатление на других людей.
'''
    },
    '11': {
        'img' : 'personality_numbers_11.png',
        'value' : '''Число личности.

1️⃣1️⃣ - Вы человек слегка странный и переменчивый, но в то же время с интересным обаянием. Для других Вы кажетесь словно присутствующим здесь и сейчас и в то же время, как будто Вы в другом измерении в данный момент. Вы довольно доверчивый человек, из-за чего можете стать жертвой обмана или мошеннических действий. 
В одежде Вы подобны людям с личностью двойки: спокойные тона и оттенки, которые как правило схожи с природными цветами.
'''
    },
    '22': {
        'img' : 'personality_numbers_22.png',
        'value' : '''Число личности.

2️⃣2️⃣ - личности этого числа схожи с личностью четвёрки: ответственные, трудолюбивые, надёжные. Но люди 22х производят более сильное впчатление. Вы без сомнения способны на великие свершения, но будет ли Вы применять эту способность - зависит от разных факторов: как от других нумерологических показателей, так и от Вашего собственного желания. Кроме того, Вы способны добиваться своего. Сила Вашей личности такова, что к Вам невозможно относиться нейтрально. Так или иначе Вас или любят или ненавидят, или доверяют или нет.
'''
    },
    '33': {
        'img' : 'personality_numbers_33.png',
        'value' : '''Число личности.

3️⃣3️⃣ - во много личности 33х схожи с личностью шести: гармония отношений и равновесие. Но главное отличие в масштабности. Скоре всего Ваши слова, мысли и поступки способны влиять на массы людей, а не на кого-то конкретного. Сам Ваш облик способен вызывать резонанс, а Ваши мысли идеи или сразу принимают с открытыми руками или мгновенно отвергают. Из Вас - человека с числом 33 может получится отличный политик, преподаватель, общественный деятель.
'''
    }
}