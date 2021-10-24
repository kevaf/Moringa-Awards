from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile, Projects, Comments, Ratings
from django.contrib.auth.models import User
from .forms import NewProjectForm, EditprofileForm, CommentForm


# Create your views here.

@login_required(login_url = '/accounts/login/')
def index(request):
    all_projects = Projects.all_projects()
    
    return render(request, 'index.html', {'all_projects': all_projects})

@login_required(login_url = '/accounts/login/')
def profile(request):
    all_projects = Projects.objects.filter(user = request.user)
    return render(request,'profile.html',{'all_projects':all_projects})

@login_required(login_url = '/accounts/login/')
def new_project(request):
    if request.method=='POST':
        form = NewProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()

            return redirect('home')

    else:
        form = NewProjectForm()
    return render(request,'new_project.html',{'form':form})