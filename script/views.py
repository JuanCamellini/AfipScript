from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "script/index.html")

def pacientes(request):
    if request.method == "POST":
        pass
    return render(request, "script/paciente.html")
    
    #video para hacer script
    #https://www.youtube.com/watch?v=FaVEISsLld0&t=1766s
    
def afipGenerar(request):
    return render(request, "script/afipGenerar.html")