from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import RegisterForm, LoginForm, ProfileForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, TemplateView
from apps.users.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'users/register.html', {"form":form})

    def post(self, request):
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "User succesfully registered")
            return redirect('users:login')
        messages.warning(request, "You`r registration is are not valid !")
        return render(request, "users/register.html", {"form":form})
    

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'users/login.html', {"form":form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request=request, user=user)
                messages.success(request, F"{ username } you are logged ")
                return redirect('books:home')
            else:
                messages.warning(request, "Invalid username or password !")
                return redirect('users:login')
        return render(request, "users/login.html", {"form":form})

class LogoutView(View):
    def get(self, request):
        return render(request, 'users/logout.html')

    def post(self, request):
        logout(request)
        return redirect('books:home')
    
#--------------------------------------------

class ProfileView(LoginRequiredMixin, View):

    def get(self, request, id):
        user = get_object_or_404(User, id=id)
        form = ProfileForm(instance=user)
        return render(request,"users/profile.html", {"form":form})
    
    def post(self, request, id):
        user = get_object_or_404(User, id=id)
        form = ProfileForm(request.POST, request.FILES,  instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "User succsessfully updated")
            return redirect('books:home')
        messages.warning(request, "your acount is not valid!")
        return render(request,"home.html", {"form":form})