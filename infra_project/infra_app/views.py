from django.http import response


def index(request):
    return response('У меня получилось!')


def second_page(request):
    return response('А это вторая страница')
