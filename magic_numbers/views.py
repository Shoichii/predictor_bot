from django.shortcuts import render
import magic_numbers.models as mdl
from numerologist.settings import TG_TOKEN
import json
import requests
from django.http import JsonResponse
from datetime import datetime

# Create your views here.


def queries(request):
    # if request.method == 'POST':
    #     data = request.get_json()
    #     adm_id = data.get('adm_id')
    #     user_id = data.get('user_id')
    #     if user_id:
    #         URL = 'https://api.telegram.org/bot' + TG_TOKEN + '/sendMessage'
    #         button_data = f'answer_button:{user_id}'
    #         reply_markup = {
    #             'inline_keyboard': [[{'text': 'Ответить', 'callback_data': button_data}]]
    #         }
    #         data = {'chat_id': ADM_ID, 
    #                 'text': f'Ответить пользователю {user_id}?', 'reply_markup': json.dumps(reply_markup)}
    #         requests.post(URL, data=data)
    #     if adm_id != int(ADM_ID): #6060015605
    #         return jsonify({'status': 'denied'})
    #     users = User.query.filter_by(question_was_send=True, was_answer=False).all()
    #     queries = []
    #     for user in users:
    #         queries.append({
    #             'user_id': user.user_id,
    #             'question': user.question
    #         })
    #     return jsonify({'queries': queries})
    return render(request, 'queries.html')


def donate(request):
    if request.method == 'POST':
        data = request.get_json()
        user_id = data.get('id')
        user = mdl.User.query.filter_by(user_id=user_id).first()
        seals = data.get('seals')
        URL = 'https://api.telegram.org/bot' + TG_TOKEN + '/sendMessage'
        today = datetime.now().date()
        #при покупке печатей
        if seals != 'consultation':
            user.seals = user.seals + seals
            user.save()
            match seals:
                case 10: money = 50
                case 50: money = 350
                case 100: money = 500
            new_entry = mdl.UserAction(user=user, date=today, action=f'{seals} печатей', money=money)
            reply_markup = {
                'inline_keyboard': [[{'text': 'В главное меню', 'callback_data': 'back_to_main_menu_button'}]]
            }
            data = {'chat_id': user_id, 
                    'text': f'Вам добавлено {seals} печатей.', 'reply_markup': json.dumps(reply_markup)}
        #при покупке консультации
        else:
            new_entry = mdl.UserAction(user=user, date=today, action=f'Консультация', money=300)
            data = {'chat_id': user_id, 
                'text': '''Спасибо за донат! Теперь Вы можете задать свой вопрос нумерологу и получить ответ в течении 24 часов.

Внимание!!! Вопрос должен быть в текстовом формате и содержаться в одном сообщении!
                '''}
            mdl.Consultation.objects.create(user=user, date_time=datetime.now())
        new_entry.save()
        requests.post(URL, data=data)
        return JsonResponse({'status': 'ok'})
    return render(request, 'index.html')