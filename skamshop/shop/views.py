from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def main(request):
    return render(request, 'index.html')


def register(request):
    return render(request, 'register.html')
