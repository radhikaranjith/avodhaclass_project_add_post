from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Task
from . forms import avodhaclassforms
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView,DeleteView
from django.urls import reverse_lazy

class TaskListView(ListView):
    model=Task
    template_name = 'task_view.html'
    context_object_name = 'obj1'

class TaskDetailView(DetailView):
    model=Task
    template_name = 'detail.html'
    context_object_name = 'i'

class TaskUpdateView(UpdateView):
    model=Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','post','datetime')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

# Create your views here.
def task_view(request):
    obj1=Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        post = request.POST.get('post')
        datetime = request.POST.get('datetime')
        obj = Task(name=name, post=post, datetime=datetime)
        obj.save()
    return render(request,'task_view.html',{'obj1':obj1})

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvtask')

def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=="POST":
        task.delete()
        return redirect('/')
    return render(request,'delete.html',{'task':task})

def update(request,id):
    task=Task.objects.get(id=id)
    form=avodhaclassforms(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'task':task,'form':form})
