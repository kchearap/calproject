from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import auth
from datetime import datetime
from django.core.exceptions import ValidationError

def signup(request):
    User = get_user_model()
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']:
            userinput = request.POST['username']
            if not userinput:
                return render(request, 'accounts/signup.html', {'error':'Please enter user name'})
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'Username has already been taken'})
            except User.DoesNotExist:
                try:
                    user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'],email=request.POST['email'],weight=float(request.POST['weight']),height=float(request.POST['height']),sex=request.POST['sex'],birth_date=datetime.strptime(request.POST['birth_date'], "%d/%m/%Y").date())
                    auth.login(request,user)
                    return redirect('home')
                except ValidationError:
                    return render(request, 'accounts/signup.html', {'error':'Validation Field Error'})
        else:
            return render(request, 'accounts/signup.html', {'error':'Passwords must match'})
    else:
        # User wants to enter info
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html',{'error':'username or password is incorrect.'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
