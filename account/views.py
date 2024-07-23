from django.shortcuts import render, redirect
from . forms import CreateUserForm
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render (request, 'account/index.html')

#create registration form
def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('my-login')
    context = {'RegisterForm' : form}
    return render (request, 'account/register.html', context)


def my_login(request):
    

    form = AuthenticationForm
    
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username') #username / email
            password = request.POST.get('password')

            #username / email
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_writer == True:
                login(request, user)
                return redirect ('writer-dashboard')
                
                #return HttpResponse('Welcome Writer')
            
            #if user is not a writer
            if user is not None and user.is_writer == False:
                login(request, user)
                return redirect ('client-dashboard')
                
                #return HttpResponse('Welcome Client')
            
    context = {'LoginForm' : form}

    return render (request, 'account/my-login.html', context)


#Define user logout function
def user_logout (request):
    
    logout(request)
    
    return redirect ("my-login")
    