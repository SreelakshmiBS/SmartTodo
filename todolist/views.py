# views.py

from django.shortcuts import render, redirect, get_object_or_404

from .models import Today_Task, Reminder


def home(request):

    tasks = Today_Task.objects.all()

    reminders = Reminder.objects.all()

    return render(
        request,
        'index.html',
        {
            'tasks': tasks,
            'reminders': reminders
        }
    )


def add_task(request):

    if request.method == 'POST':

        title = request.POST.get('title')

        description = request.POST.get('description')

        Today_Task.objects.create(
            title=title,
            description=description
        )

        return redirect('home')

    return redirect('home')


def view_tasks(request):

    tasks = Today_Task.objects.all()

    return render(
        request,
        'view_task.html',
        {
            'tasks': tasks
        }
    )


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

    return render(
        request,
        'add_reminder.html',
        {
            'task': task
        }
    )
    
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


def delete_task(request,task_id):
    task =get_object_or_404(
        Today_Task,id=task_id)
    task.delete()
    return redirect('home')

def delete_reminder(request,reminder_id):
    reminder = get_object_or_404(
        Reminder,
        id=reminder_id
    )
    reminder.delete()
    return redirect('home')

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
    

    

    