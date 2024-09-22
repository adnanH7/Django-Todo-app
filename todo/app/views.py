from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def addTask(request):
    if request.method == "POST":
        task_name = request.POST.get('task')
        due_date = request.POST.get('due_date')

        Task.objects.create(name=task_name, due_date= due_date)
    return render(request,'app/addTask.html')

def tasklist(request):
    tasks = Task.objects.all()
    return render(request, 'app/tasklist.html',{
        'tasks':tasks
    })

def deleteTask(request,task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('tasklist')

