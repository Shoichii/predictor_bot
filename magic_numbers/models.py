from django.db import models


class User(models.Model):
    telegram_id = models.BigIntegerField(verbose_name='Телеграм ID')
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='ФИО')
    birthday = models.DateField(null=True, blank=True, verbose_name='День рождения')
    seals = models.BigIntegerField(null=True, blank=True, verbose_name='Количество печатей')

    def __str__(self):
        return str(self.telegram_id)
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class UserBaseNumbers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    life_path_number = models.IntegerField(verbose_name='Число жизненного пути', null=True, blank=True)
    birthday_number = models.IntegerField(verbose_name='Число дня рождения', null=True, blank=True)
    expression_number = models.IntegerField(verbose_name='Число экспрессии', null=True, blank=True)
    spirit_awake_number = models.IntegerField(verbose_name='Число духовного пробуждения', null=True, blank=True)
    personality_number = models.IntegerField(verbose_name='Число личности', null=True, blank=True)

    def __str__(self):
        return self.user.name
    
    class Meta:
        verbose_name = 'Базовое число'
        verbose_name_plural = 'Базовые числа'


class UserDayJournal(models.Model):
    # Счётчик посещений разделов за день
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    date = models.DateField(verbose_name='Дата')
    numerology_count = models.IntegerField(verbose_name='Раздел нумерологии')
    core_synthesis = models.IntegerField(verbose_name='Синтез ядра')
    forecast = models.IntegerField(verbose_name='Прогноз')

    def __str__(self):
        return self.user.name
    
    class Meta:
        verbose_name = 'Журнал посещений раздел'
        verbose_name_plural = 'Журналы посещений раздел'


class Consultation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    date_time = models.DateTimeField(verbose_name='Время и Дата')
    question = models.TextField(verbose_name='Вопрос', null=True, blank=True)
    answer = models.TextField(verbose_name='Ответ', null=True, blank=True)
    answer_pics = models.ManyToManyField('AnswerPic', verbose_name='Картинки ответа', blank=True)

    def __str__(self):
        return str(self.user)
    
    class Meta:
        verbose_name = 'Консультация'
        verbose_name_plural = 'Консультации'


class AnswerPic(models.Model):
    pic_consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE, verbose_name='Консультация')
    pic_id = models.TextField(verbose_name='Картинка')

    def __str__(self):
        return str(self.consultation)
    
    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'


class UserAction(models.Model):
    # покупки кроме консультаций
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    date = models.DateField(verbose_name='Дата')
    action = models.TextField(verbose_name='Действие')
    money = models.IntegerField(verbose_name='Количество рублей')

    def __str__(self):
        return self.action
    
    class Meta:
        verbose_name = 'Действие'
        verbose_name_plural = 'Действия'