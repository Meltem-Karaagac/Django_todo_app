from django.shortcuts import get_object_or_404, redirect, render

from .forms import TodoAddForm, TodoUpdateForm
from .models import Todo


def home(request):
    return render(request, "todo/home.html")


def todo_list(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, "todo/todo_list.html", context)


def todo_create(request):
    form = TodoAddForm()
    if request.method == "POST":
        form = TodoAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("house")
    context = {
        'form': form
    }
    return render(request, "todo/todo_create.html", context)


def todo_update(request, id):
    todo = get_object_or_404(Todo, id=id)
    form = TodoUpdateForm(instance=todo)
    if request.method == "POST":
        form = TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("todo-list")
    context = {
        'todo': todo,
        'form': form
    }
    return render(request, "todo/todo_update.html", context)


def todo_delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == "POST":
        todo.delete()
        return redirect("todo-list")
    context = {
        'todo': todo
    }
    return render(request, "todo/todo_delete.html", context)
