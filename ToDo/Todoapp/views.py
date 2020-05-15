from django.shortcuts import render, redirect
from .models import ToDo
from .forms import ToDoForm


def index(request):
    item_list = ToDo.objects.order_by("-created")
    if request.method == 'POST':
        task_form = ToDoForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('ToDoApp:todo')
    task_form = ToDoForm()

    page = {
        "forms": task_form,
        "list": item_list,
    }
    return render(request, 'index.html', page)


def remove(request, item_id):
    item = ToDo.objects.get(id=item_id)
    item.delete()
    return redirect('ToDoApp:todo')
