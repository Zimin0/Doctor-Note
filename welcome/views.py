from django.shortcuts import render

def welcome(request):
    return render(request, 'welcome/welcome.html', {})

def page_in_progress(request):
    return render(request, 'welcome/inWork.html', {})