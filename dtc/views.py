from django.shortcuts import render

def hello_world(request):

    return render(request, 'hello_world.html', {})


def maps(request):

    return render(request, 'maps.html', {})


def welcome(request):

    return render(request, 'welcome.html', {})