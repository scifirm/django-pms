
from django.shortcuts import render, redirect
from .models import Project, Task, ActivityLog
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    projects = Project.objects.filter(owner=request.user)
    total_projects = projects.count()
    completed = projects.filter(status='Completed').count()

    ActivityLog.objects.create(user=request.user, action='Visited Dashboard')

    return render(request, 'projects/dashboard.html', {
        'projects': projects,
        'total_projects': total_projects,
        'completed': completed,
    })

@login_required
def create_project(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']

        Project.objects.create(
            name=name,
            description=description,
            start_date=start_date,
            end_date=end_date,
            owner=request.user
        )

        ActivityLog.objects.create(user=request.user, action='Created Project')
        return redirect('dashboard')

    return render(request, 'projects/create_project.html')
