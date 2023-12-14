from django.shortcuts import redirect

def page_in_progress(func):
    """ Страница еще в разработке. Редиректит на страницу-заплатку. """
    def _wrapper_view(*args, **kwargs):
        return redirect("welcome:page_in_progress")
    return _wrapper_view

def log_veriables(func):
    """ Выводит на экран содержимое session, GET, POST, переменные, переданные в функцию"""
    def wrapper(request, *args, **kwargs):
        func_name = func.__name__
        print(f'----------{func_name}----------')
        print(f'------------ARGUMENTS------------')
        arguments_string = ''
        for variable in kwargs.items():
            arguments_string += f""""{variable[0]}":{variable[1]}\n"""
        print(arguments_string[:-1]) if len(arguments_string) > 0 else None
        print(f'-------------SESSION-------------')
        session_string = ''
        for variable in request.session.items():
            session_string += f""""{variable[0]}":{variable[1]}\n"""
        print(session_string[:-1]) if len(session_string) > 0 else None # обрезает последний \n
        print(f'--------------POST---------------')
        post_string = ''
        for variable in request.POST.items():
            post_string += f""""{variable[0]}":{variable[1]}\n"""
        print(post_string[:-1]) if len(post_string) > 0 else None
        print(f'---------------GET---------------')
        get_string = ''
        for variable in request.GET.items():
            get_string += f""""{variable[0]}":{variable[1]}\n"""
        print(get_string[:-1]) if len(get_string) > 0 else None
        print('----------------------------------') 
        return func(request, *args, **kwargs)
    return wrapper