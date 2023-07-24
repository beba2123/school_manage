from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, get_user_model
from django.contrib import messages

User = get_user_model()
# Create your views here.
def index(request):
    return render(request, 'authentication\index.html')

def login(request):
    # print(request.user.is_authenticated)
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        auth_user = authenticate(request, username=username, password=password)
        if auth_user is not None:
            auth_login(request, auth_user)
            return redirect('index')
        # print(auth_user)

        # print('Requset is', request.POST)
    return render(request, 'authentication\login.html')

def logout(request):
    auth_logout(request)
    return redirect('index')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST.get('last_name', '')
        email = request.POST['email']
        password = request.POST['password']

        try: 
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email= email, password=password)
            auth_login(request, user)
            return redirect('index')
        except Exception as e: 
            print('Error creating User: ',  e)
            messages.error(request, 'Error the username or password exist.')

    return render(request, 'authentication\signup.html')