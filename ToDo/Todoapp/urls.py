from django.urls import path
from . import views

app_name = 'ToDoApp'

urlpatterns = [
    path('', views.index, name="todo"),
    path('/del/<int:item_id>/', views.remove, name="del"),
]
