from django.urls import path
from . import views
urlpatterns = [
    path("addtask/",views.addTask,name="addTask"),
    path("tasklist/",views.tasklist,name="tasklist"),
    path('deletetask<int:task_id>',views.deleteTask,name="deletetask")
]
