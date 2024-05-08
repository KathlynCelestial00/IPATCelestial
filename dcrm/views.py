from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForms
# Create your views here.

def home(request):
    #do something 
 return render(request, 'home.html')

def register(request):
 

  if request.methed == 'POST':
         form= SignUpForms(request.POST)
         if form.is_valid():
          form.save()
 
          username = forms.cleaned_date[ 'username']
          password = forms.cleaned_date[ 'password1']
          user = authenticate(username=username, password=password)
          login(request, user)
          return redirect('home')

         else: 
          form = SignUpForms()
          return render(request,'register.html', {'form': form})



  return render(request, 'register.html')