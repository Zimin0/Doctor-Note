from django.shortcuts import render

def welcome(request):
    return render(request, 'welcome/welcome.html', {})

def page_in_progress(request):
    return render(request, 'welcome/inWork.html', {})

def redirect_page_with_reason(request, to_url:str):
    """ 
    Перенаправление на заданную страницу с сообщением.
    * to_url_name - строка формата "" welcome:page_in_progress 
    """
    context = {
        'message': 'Успшено!',
        'redirect_url' : to_url
        }
    return render(request, 'welcome/redirect.html', context)