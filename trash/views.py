from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    model = {}
    if not request.user.is_authenticated():
        return redirect('/accounts/login/')
    else:
        model['username'] = request.user.username

    return render(request, 'trash/index.html', model)