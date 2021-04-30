from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy


from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


from .models import Task

# Create your views here.


class NewLoginView(LoginView):
    template_name = "baseapp/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("home")


class RegisterPage(FormView):
    template_name = "baseapp/register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("home")
        return super(RegisterPage, self).get(*args, **kwargs)


class Tasklist(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasklist"
    template_name = "baseapp/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasklist"] = context["tasklist"].filter(user=self.request.user)
        context["count"] = context["tasklist"].filter(complete=False).count()

        search_in = self.request.GET.get("search-area") or ""
        if search_in:
            context["tasklist"] = context["tasklist"].filter(title__startswith=search_in)

        context["search_in"] = search_in
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = "detail"
    template_name = "baseapp/detail.html"


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ["title", "description", "complete"]
    success_url = reverse_lazy("home")
    template_name = "baseapp/create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ["title", "description", "complete"]
    success_url = reverse_lazy("home")
    template_name = "baseapp/create.html"


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = "detail"
    success_url = reverse_lazy("home")
    template_name = "baseapp/delete.html"
