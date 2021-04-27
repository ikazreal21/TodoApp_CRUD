from django.urls import path
from .views import Tasklist, TaskDetail


urlpatterns = [
    path('', Tasklist.as_view(), name='home'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='detail'),
]
