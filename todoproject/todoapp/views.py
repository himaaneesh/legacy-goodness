from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task1
from .forms import Todoform

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView


class Tasklistview(ListView):
    model=Task1
    template_name = 'home.html'
    context_object_name = 'task1'

class TaskDetailview(DetailView):
    model = Task1
    template_name = 'detail.html'
    context_object_name = 'task'

class TaskUpdateview(UpdateView):
    model = Task1
    template_name = 'update.html'
    context_object_name = 'task'
    fields =( 'name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbdetail',kwargs={'pk':self.object.id})

class TaskDeleteview(DeleteView):
    model = Task1
    template_name = 'delete.html'
    success_url = reverse_lazy('cbhome')

# Create your views here.
def add(request):
    task1 = Task1.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date','')
        task = Task1(name=name, priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'task1':task1})

# def details(request):
#
#     return render(request,'detail.html',)

def delete(request,taskid):
    task=Task1.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task=Task1.objects.get(id=id)
    fo=Todoform(request.POST or None,instance=task)
    if fo.is_valid():
        fo.save()
        return redirect('/')
    return render(request,'edit.html',{'fo':fo,'task':task})