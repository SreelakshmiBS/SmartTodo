from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_task/', views.add_task, name='add_task'),
    path('view_tasks/', views.view_tasks, name='view_tasks'),  
    path('add_reminder/<int:task_id>/', views.add_reminder, name='add_reminder'), 
    path('mark_completed/<int:task_id>/', views.mark_completed, name='mark_completed'),
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('edit_reminder/<int:reminder_id>/', views.edit_reminder, name='edit_reminder'),
    path('delete_reminder/<int:reminder_id>/', views.delete_reminder, name='delete_reminder'),
]