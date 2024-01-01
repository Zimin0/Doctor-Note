from django.shortcuts import render, redirect
from users.forms import UserRegistrationForm
from django.http import HttpResponse

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['message-in-redirect-page'] = 'Вы заргестрированы!'
            return redirect('welcome:redirect_page_with_reason', url_pattern_name='users:login')
        else:
            print("Форма регистрации невалидна!")
            print(form.errors)
            return render(request, 'users/register.html', {'form':form, 'errors': form.errors})
    else:
        form = UserRegistrationForm()
        return render(request, 'users/register.html', {'form': form})