from django.shortcuts import render, redirect
from .forms import LoginForm,RegisterForm
from django.contrib.auth import authenticate,login
# Create your views here.
def index(request):
    return render(request,'index.html')

def users_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('users_login')
        return redirect('users_register')
    
    if request.method == 'GET' and not request.user.is_authenticated:
        context = {'form':RegisterForm}
        return render(request,'accounts/register.html', context )
    return redirect('note_list')

def users_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username = username ,password = password)
        if user is not None:
            login(request,user)
            return redirect('note_list')
        return redirect('users_login')


    if request.method == 'GET' and not request.user.is_authenticated:
        context = {'form':LoginForm}
        return render(request,'accounts/login.html',context)
    return redirect('note_list')