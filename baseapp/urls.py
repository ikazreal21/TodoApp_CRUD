from django.urls import path
from .views import (
    Tasklist,
    TaskDetail,
    TaskCreate,
    TaskUpdate,
    TaskDelete,
    NewLoginView,
    RegisterPage
)
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("login/", NewLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page='login'), name="logout"),
    path("register/", RegisterPage.as_view(), name="register"),


    path("", Tasklist.as_view(), name="home"),
    path("task/<int:pk>/", TaskDetail.as_view(), name="detail"),
    path("create-task/", TaskCreate.as_view(), name="create"),
    path("update-task/<int:pk>/", TaskUpdate.as_view(), name="update"),
    path("delete-task/<int:pk>/", TaskDelete.as_view(), name="delete"),
]
