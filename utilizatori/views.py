from django.shortcuts import render
from .models import Users

def index(request):
        obiecte = Users.objects.all()
        return render(request, "utilizatori/index.html", {'lst': obiecte})

