from django.shortcuts import render, redirect
from .models import Tasks
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.


def deleteTask(request, pk):
    task = Tasks.objects.get(id=pk)
    task.delete()
    return redirect('/')


@login_required(login_url='/users/register')
def taskView(request):
    user = request.user
    if request.method == 'POST':
        items = request.POST.dict()
        if items.get('title') is not None and items.get('text') is not None:
            task = Tasks(title=items["title"], task_text=items["text"], user=user)
            task.save()
        else:
            if items.get('search') is not None:
                tasks = Tasks.objects.filter(user=user.id, title__contains=items["search"])
                return render(request, "task/tasks.html", context={"tasks": tasks})
            else:
                tasks = Tasks.objects.all()
                for task in tasks:
                    task.status = False
                    task.save()
                for key, val in items.items():
                    try:
                        key = int(key)
                        task = Tasks.objects.get(id=key)
                        if val == 'on':
                            task.status = True
                            task.save()
                    except ValueError:
                        if 'delete' in key:
                            id = int(key.split('delete')[1])
                            task = Tasks.objects.get(id=id)
                            task.delete()
        return redirect('/')
    tasks = Tasks.objects.filter(user=user.id)
    return render(request, "task/tasks.html", context={"tasks": tasks})


def newApp(request):
    tasks = Tasks.objects.all()
    return render(request, "new_app.html", context={"tasks": tasks})


def search_view(request):
    query = request.GET.get('query')
    return render(request, "new_app.html", {"query": query})


