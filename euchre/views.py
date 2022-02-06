from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def gameDetail(request):
    context = {}
    user_names = [0, 1, 2, 3]
    if 'user_name' in request.POST:
        context['user_name'] = request.POST.get('user_name')
        context['user_names'] = user_names
        print(request.POST.get('user_name'))

    return render(request, "gamescreen.html", context)

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
