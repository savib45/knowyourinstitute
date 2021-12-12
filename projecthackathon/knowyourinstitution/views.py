from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import auth
from knowyourinstitution.UserForm import UserFormModel
from knowyourinstitution.UserLoginForm import UserLoginFormModel
from knowyourinstitution.UserForm import UserProfileFormModel
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from knowyourinstitution.RatingForm import RatingForm
from .models import College
# Create your views here.
def index(request):
    all_college = College.objects.all()
    return render(request, 'pages/index.html',{'colleges':all_college})

def register(request):

    if request.method == 'POST':
        user_form = UserFormModel(request.POST)
        profile_form = UserProfileFormModel(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit = False)
            profile.user = user
            profile.save()
            messages.success(request, 'User Created Successfully')
            return redirect('/login')
        else:
            messages.warning(request, 'Invalid Data Entered')
            return redirect('/register')
    else:
        user_form = UserFormModel()
        profile_from = UserProfileFormModel()
        return render(request,'pages/register.html',{'user_form':user_form,'profile_form':profile_from})

def login(request):

    if request.method == 'POST':
        print(request.POST['username'])
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username , password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request, 'invalid credentials')
            return redirect("/login")
    else:
        form = UserLoginFormModel()
        return render(request, 'pages/login.html',{'form':form})

@login_required
def dash(request):
    return render(request, 'pages/dashboard.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

@login_required
def review(request):

    if request.method == "GET":
        colleges = College.objects.all()
        form = RatingForm()
        return render(request, 'pages/review.html',{'form':form,'colleges':colleges})
    else:
        review = RatingForm(request.POST)
        review = review.save(commit=False)
        review.college = College.objects.get(college_id = request.POST['id_college'])
        review.user = request.user
        review.save()
        return redirect('home')


def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        found = College.objects.filter(college_name=searched)
        return render(request, 'pages/search.html',{'searched':searched,'found':found})
    else:
        return redirect('home')