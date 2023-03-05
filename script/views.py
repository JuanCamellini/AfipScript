from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "script/index.html")

def pacientes(request):
    if request.method == "POST":
        pass
    #video para hacer script
    #https://www.youtube.com/watch?v=FaVEISsLld0&t=1766s
    