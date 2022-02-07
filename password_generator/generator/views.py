from string import ascii_lowercase, ascii_uppercase, digits, punctuation

from django.shortcuts import render
import random


def home(request):
    return render(request, 'generator/home.html', {'title': 'Главная страница'})


def about(request):
    return render(request, 'generator/about.html')


def password(request):
    print(request)

    characters = list(ascii_lowercase)
    generated_password = ''

    if request.GET.get('uppercase'):
        characters.extend(list(ascii_uppercase))

    if request.GET.get('special'):
        characters.extend(list(punctuation))

    if request.GET.get('numbers'):
        characters.extend(list(digits))

    length = int(request.GET.get('length', 10))
    for x in range(length):
        generated_password += random.choice(characters)

    context = {'password': generated_password}
    return render(request, 'generator/password.html', context)
