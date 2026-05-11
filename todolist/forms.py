from django import forms
from .models import Today_Task, Reminder
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm  

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class TaskForm(forms.ModelForm):

    class Meta:

        model = Today_Task

        fields = ['title', 'description', 'status']
        
        placeholder = {
            'title': 'Enter task title',
            'description': 'Enter task description',
        }
        
class ReminderForm(forms.ModelForm):

    class Meta:

        model = Reminder

        fields = ['reminder_time', 'message']
        
        placeholder = {
            'reminder_time': 'Select reminder time',
            'message': 'Enter reminder message',
        }
        
        