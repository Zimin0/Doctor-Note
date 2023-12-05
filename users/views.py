from django.shortcuts import render, redirect
from users.forms import UserRegistrationForm

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
        else:
            print("Форма регистрации невалидна!")
            print(form.errors)
            return render(request, 'users/register.html', {'form':form, 'errors': form.errors})
    else:
        form = UserRegistrationForm()
        return render(request, 'users/register.html', {'form': form})