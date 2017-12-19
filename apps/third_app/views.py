
from django.shortcuts import render, HttpResponse, redirect
from .models import Course
def index(request):
    
    context = {
        "course" : Course.objects.all(),

    }
    print course 
    


    return render(request, "third_app/index.html", context)

def course(request):
    Course.objects.create(name=request.POST['name'], description=request.POST['description'])

    return redirect('/')

def question(request):
    if request.method == "POST":
        print request.POST['hidden']

        context = {
        "course" : Course.objects.get(id = request.POST['hidden'])

    }
        print course
        return render(request, "third_app/delete.html", context)


def delete(request):
    if request.method == "POST":
        print request.POST['hidden']

    #     context = {
    #     "course" : Course.objects.get(id = request.POST['hidden'])

    # }
        Course.objects.filter(id = request.POST['hidden']).delete()

        return redirect('/')