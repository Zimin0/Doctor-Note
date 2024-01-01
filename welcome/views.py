from django.shortcuts import render
from django.urls import reverse


def welcome(request):
    request.session['message-in-redirect-page'] = 'Вы зарегистрированы!'
    return render(request, 'welcome/welcome.html', {})

def page_in_progress(request):
    return render(request, 'welcome/inWork.html', {})

def redirect_page_with_reason(request, url_pattern_name:str):
    """ 
    Перенаправление на заданную страницу с сообщением.
    * to_url_name - строка формата "" welcome:page_in_progress 
    """
    message = request.session.pop('message-in-redirect-page', 'Успешно!')
    context = {
        'message': message,
        'redirect_url' : request.build_absolute_uri(reverse(url_pattern_name))
        }
    return render(request, 'welcome/redirect.html', context)