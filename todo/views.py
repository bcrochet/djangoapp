from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect

from .forms import TodoForm
from .models import Todo

# Create your views here.
def index(request):
    form = TodoForm()

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    todo_list = Todo.objects.order_by('add_date')
    # context = {
    #     'todo_list': todo_list,
    # }
    # return render(request, 'todo/index.html', context)
    return render(request, "todo/index.html", {"todo_form": form, "todo_list": todo_list})

def update_todo(request, pk):
    todo = Todo.objects.get(id=pk)

    form = TodoForm(instance=todo)

    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("index")

    return render(request, "todo/update_todo.html", {"todo_edit_form": form})

def delete_todo(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect("index")
