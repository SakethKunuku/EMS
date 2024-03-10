from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
def ProjectHomePage(request):
    return render(request,'ProjectHomePage.html')
def EventManagerHomePage(request):
    return render(request,'EventManagerHomePage.html')
def EventParticipantHomePage(request):
    return render(request,'EventParticipantHomePage.html')
def Signup(request):
    return render(request,'signup.html')

from django.contrib import messages
from django.contrib.auth.models import User, auth


def signup1(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Oops! Username Already Taken.')
                return render(request, 'signup.html')
            else:
                user = User.objects.create_user(username=username, email=email, password=pass1,
                                                first_name=first_name,
                                                last_name=last_name)
                user.save()
                messages.info(request, 'Account created successfully')
                user_details = {
                    'username': username,
                    'email': email,
                    'first_name': first_name,
                    'last_name': last_name
                }
                return render(request, 'ProjectHomePage.html',
                              {'user_details': user_details})  # Redirect to account details page
        else:
            messages.info(request, 'Password does not match')
            return render(request, 'signup.html')

    return render(request, 'signup.html')


def login(request):
    return render(request, 'login.html')


def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        user = auth.authenticate(username=username, password=pass1)
        if user is not None:
            auth.login(request, user)
            if len(username) == 10:
                return redirect('EventParticipantHomePage')
            elif len(username) == 4:
                return redirect('EventManagerHomePage')
            else:
                return redirect('ProjectHomePage')
        else:
            messages.info(request, 'Invalid Credentials')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')




def logout(request):
    auth.logout(request)
    return render(request, 'ProjectHomePage.html')


def account_details(request):
    user_details = {
        'username': request.user.username,
        'email': request.user.email,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name
    }
    user_role = 'Employer' if len(request.user.username) == 4 else 'Job Seeker'
    return render(request, 'account_details.html', {'user_details': user_details, 'user_role': user_role})


def user_profile(request):
    return render(request, 'user_profile.html')


def AboutUs(request):
    return render(request,'Admin_module/AboutUs.html')

def OurServices(request):
    return render(request,'Admin_module/OurServices.html')

def ContactUs(request):
    return render(request,'Admin_module/ContactUs.html')

def MoreInfo(request):
    return render(request,'Admin_module/MoreInfo.html')

def Gallery(request):
    return render(request,'Admin_module/Gallery.html')