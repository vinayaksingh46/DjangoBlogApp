from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            messages.success(request,f'Account Created  successfully !!')
            return redirect('blog-home')
        # else:
        #     # form = UserCreationForm()
            
    else :
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form': form})

def profile(request):
    return render(request,'users/profile.html')