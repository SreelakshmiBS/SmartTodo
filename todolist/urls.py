from django.urls import path
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login_view/', views.login_view, name='login_view'),
    path('logout_view/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('add_task/', views.add_task, name='add_task'),
    path('view_tasks/', views.view_tasks, name='view_tasks'),  
    path('add_reminder/<int:task_id>/', views.add_reminder, name='add_reminder'), 
    path('mark_completed/<int:task_id>/', views.mark_completed, name='mark_completed'),
    path('edit_task/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
    path('edit_reminder/<int:reminder_id>/', views.edit_reminder, name='edit_reminder'),
    path('delete_reminder/<int:reminder_id>/', views.delete_reminder, name='delete_reminder'),


    # Forgot Password (enter email)
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='password_reset.html'
    ), name='password_reset'),

    # Email sent success page
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'
    ), name='password_reset_done'),

    # Link from email (set new password)
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'
    ), name='password_reset_confirm'),

    # Success page after password reset
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'
    ), name='password_reset_complete'),
]

