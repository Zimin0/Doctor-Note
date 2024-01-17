from django.shortcuts import render, redirect
from users.forms import UserRegistrationForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from welcome.decorators import page_in_progress, log_veriables
from users.forms import UserChangeInfoForm

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

@login_required
def profile(request):
    if request.method == 'GET':
        form = UserChangeInfoForm(user=request.user)
        return render(request, 'users/profile.html', {'form': form})
    elif request.method == 'POST':
        form = UserChangeInfoForm(request.POST, user=request.user)
        if form.is_valid():
            user = form.save()
            profile = user.profile
            profile.need_to_send_notifics_on_mail = form.cleaned_data.get('need_to_send_notifics_on_mail')
            profile.save()
            return render(request, 'users/profile.html', {'form': form})
        else:
            return render(request, 'users/profile.html', {'form': form, 'errors': form.errors})