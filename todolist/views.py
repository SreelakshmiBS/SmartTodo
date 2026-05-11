# views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Today_Task, Reminder
from django.utils import timezone
from django.utils.timezone import now
from .forms import RegistrationForm, TaskForm, ReminderForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_view')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})

    # ✅ THIS IS REQUIRED (GET request)
    return render(request, 'login.html')
        
def logout_view(request):
    logout(request)
    return redirect('index')

    
@login_required
def home(request):

    tasks = Today_Task.objects.filter(user=request.user)
    reminders = Reminder.objects.all()
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(status='Completed').count()
    pending_tasks = tasks.filter(status='Pending').count()
    total_reminders = reminders.count()
    todays_tasks = tasks.filter(created_at__date=now().date()).count()

    context = {
        'tasks': tasks,
        'reminders': reminders,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'total_reminders': total_reminders,
        'todays_tasks': todays_tasks,
    }

    return render(request, 'home.html', context)

@login_required
def add_task(request):

    if request.method == 'POST':

        title = request.POST.get('title')

        description = request.POST.get('description')

        Today_Task.objects.create(
            user =request.user,
            title=title,
            description=description
        )

        return redirect('home')

    return redirect('home')

@login_required
def view_tasks(request):
    search_query = request.GET.get('search', '')
    
    if search_query:
        tasks = tasks.filter(title__icontains=search_query)
    else:
        tasks = Today_Task.objects.filter(user=request.user)

    return render(
        request,
        'view_task.html',
        {
            'tasks': tasks
        }
    )

@login_required
def add_reminder(request, task_id):

    task = get_object_or_404(
        Today_Task,
        id=task_id
    )

    if request.method == 'POST':
        reminder_time = request.POST.get('reminder_time')
        message = request.POST.get('message')
        Reminder.objects.create(
            task=task,
            reminder_time=reminder_time,
            message=message
        )

        return redirect('home')

    return render(request,'add_reminder.html',
        {
            'task': task
        }
    )
@login_required 
def mark_completed(request, task_id):

    task = get_object_or_404(
        Today_Task,
        id=task_id
    )

    # TOGGLE STATUS

    if task.status == 'Pending':

        task.status = 'Completed'

        Reminder.objects.filter(
            task=task
        ).update(status='Completed')

    else:

        task.status = 'Pending'

        Reminder.objects.filter(
            task=task
        ).update(status='Pending')

    task.save()

    return redirect('home')

@login_required
def delete_task(request,task_id):
    task =get_object_or_404(
        Today_Task,id=task_id)
    task.delete()
    return redirect('home')

@login_required
def delete_reminder(request,reminder_id):
    reminder = get_object_or_404(
        Reminder,
        id=reminder_id
    )
    reminder.delete()
    return redirect('home')

@login_required
def edit_task(request,task_id):
    task = get_object_or_404(
        Today_Task,
        id=task_id
    )
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.save()
        return redirect('home')
    return render(
        request,
        'edit_task.html',
        {
            'task': task
        }
    )
    
@login_required
def edit_reminder(request,reminder_id):
    reminder = get_object_or_404(
        Reminder,
        id=reminder_id
    )
    if request.method == 'POST':
        reminder.reminder_time = request.POST.get('reminder_time')
        reminder.message = request.POST.get('message')
        reminder.save()
        return redirect('home')
    return render(
        request,
        'edit_reminder.html',
        {
            'reminder': reminder
        }
    )

    

    

    