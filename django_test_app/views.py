from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    context = {'user': request.user}
    return render(request, 'django_test_app/index.html', context)