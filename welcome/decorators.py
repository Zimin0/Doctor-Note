from django.shortcuts import redirect

def page_in_progress(func):
    """ Страница еще в разработке. Редиректит на страницу-заплатку. """
    def _wrapper_view(request, *args, **kwargs):
        return redirect("welcome:page_in_progress")
        #return func(request, *args, **kwargs)
    return _wrapper_view