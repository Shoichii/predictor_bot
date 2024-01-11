from django.contrib import admin
import magic_numbers.models as md

# Register your models here.
@admin.register(md.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'telegram_id', 'birthday', 'seals')
    list_filter = ('name', 'telegram_id', 'birthday', 'seals')
    readonly_fields = ('name', 'telegram_id', 'birthday')
    list_per_page = 25


@admin.register(md.UserBaseNumbers)
class UserNumbersAdmin(admin.ModelAdmin):
    list_display = ('user', 'life_path_number', 'birthday_number', 'expression_number', 'spirit_awake_number',
                    'personality_number')
    list_filter = ('user', 'life_path_number', 'birthday_number', 'expression_number', 'spirit_awake_number',
                    'personality_number')
    list_per_page = 25


@admin.register(md.Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_time', 'question', 'answer')
    list_filter = ('user', 'date_time', 'question', 'answer')
    readonly_fields = ('user', 'date_time', 'question', 'answer')
    list_per_page = 25


@admin.register(md.AnswerPic)
class AnswerPicAdmin(admin.ModelAdmin):
    list_display = ('consultation', 'pic_id')
    list_filter = ('consultation', 'pic_id')
    readonly_fields = ('consultation', 'pic_id')
    list_per_page = 25


@admin.register(md.UserAction)
class UserActionAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'money')
    list_filter = ('user', 'action', 'money')
    readonly_fields = ('user', 'action', 'money')
    list_per_page = 25