from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task
# Create your views here.


class Tasklist(ListView):
    model = Task
    context_object_name = 'tasklist'
    template_name = 'baseapp/list.html'


class TaskDetail(DetailView):
    model = Task
    context_object_name = 'detail'
    template_name = 'baseapp/detail.html'
