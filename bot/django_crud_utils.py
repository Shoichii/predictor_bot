

# расчёт числа жизненного пути
def calc_life_path_number(birthday):
    day = birthday[0]
    month = birthday[1]
    year = birthday[2]
    day_sum = 0
    month_sum = 0
    year_sum = 0
    
    #расчёт дня
    if day == '11' or day == '22':
        day_sum = int(day)
    else:
        day_sum = int(day[0]) + int(day[1])
    
    #расчёт месяца
    if month == '11':
        month_sum = int(month)
    else:
        month_sum = int(month[0]) + int(month[1])
        
    #расчёт года
    year_sum = int(year[0]) + int(year[1]) + int(year[2]) + int(year[3])
    
    life_path_number = day_sum + month_sum + year_sum
    while life_path_number not in range(1,10):
        number_sum = 0
        for d in str(life_path_number):
            number_sum += int(d)
        life_path_number = number_sum
        if life_path_number == 11 or life_path_number == 22 or life_path_number == 33:
            break
    
    return life_path_number


# расчёт числа дня рождения
def calc_birthday_number(birthday):
    birthday_number = birthday[0]
    if birthday_number[0] == '0':
        birthday_number = int(birthday_number)
    birthday_number = str(birthday_number)
    return birthday_number


# расчёт числа экспрессии
def calc_expression_number(name):
    letters_list = [['А', 'И', 'С', 'Ъ',], ['Б', 'Й', 'Т', 'Ы',],['В', 'К', 'У', 'Ь',],['Г', 'Л', 'Ф', 'Э',],
                    ['Д', 'М', 'Х', 'Ю',],['Е', 'Н', 'Ц', 'Я',],['Ё', 'О', 'Ч'],['Ж', 'П', 'Ш'],
                    ['З', 'Р', 'Щ']]
    words_sums = []
    for word in name:
        word_sum = 0
        for letter in word:
            for i, inside_list in enumerate(letters_list):
                if letter in inside_list:
                    word_sum += i + 1
                    break
        words_sums.append(word_sum)
    
    expression_number = sum(words_sums)
    if expression_number != 11 or expression_number != 22 or expression_number != 33:
        while expression_number not in range(0,10):
            number_sum = 0
            for numb in str(expression_number):
                number_sum += int(numb)
            expression_number = number_sum
    
    return expression_number


# расчёт числа душевного пробуждения
def calc_spirit_awake_number(name):
    letters_list = {
        'А': 1,
        'Е': 6,
        'Ё': 7,
        'И': 1,
        'О': 7,
        'У': 3,
        'Э': 4,
        'Ю': 5,
        'Я': 6,
    }
    keys = list(letters_list)
    words_sums = []

    for word in name:
        word_sum = 0
        for letter in word:
            if letter.upper() in keys:
                word_sum += letters_list[letter.upper()]
        words_sums.append(word_sum)

    spirit_awake_number = sum(words_sums)
    if spirit_awake_number != 11 or spirit_awake_number != 22 or spirit_awake_number != 33:
        while spirit_awake_number not in range(0,10):
            number_sum = 0
            for numb in str(spirit_awake_number):
                number_sum += int(numb)
            spirit_awake_number = number_sum
    
    return spirit_awake_number


# расчёт числа личности
def calc_personality_number(name):
    letters_list = {
        'Б': 2,'В': 3,'Г': 4,'Д': 5,'Ж': 8,'З': 9,
        'Й': 2,'К': 3,'Л': 4,'М': 5,'Н': 6,'П': 8,
        'Р': 9,'С': 1,'Т': 2,'Ф': 4,'Х': 5,'Ц': 6,
        'Ч': 7,'Ш': 8,'Щ': 9,'Ъ': 1,'Ь': 3,
    }
    keys = list(letters_list)
    words_sums = []

    for word in name:
        word_sum = 0
        for letter in word:
            if letter.upper() in keys:
                word_sum += letters_list[letter.upper()]
        words_sums.append(word_sum)

    personality_number = sum(words_sums)
    if personality_number != 11 or personality_number != 22 or personality_number != 33:
        while personality_number not in range(0,10):
            number_sum = 0
            for numb in str(personality_number):
                number_sum += int(numb)
            personality_number = number_sum

    return personality_number