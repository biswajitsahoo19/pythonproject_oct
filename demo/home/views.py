from django.shortcuts import render,redirect
from .forms import UserMasterForm
from .models import UserMaster
from .forms import LoginForm

# Create your views here.
def register(request):
    if request.method=='POST':
        form=UserMasterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    formobj = UserMasterForm()
    ob=UserMaster.objects.all()[::-1]
    return render(request,'register.html',{'form':formobj,'obj':ob})

def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        username=form.data.get('username')
        password=form.data.get('password')
        try:
            user=UserMaster.objects.get(username=username,password=password)
            return redirect('home')
        except Exception as e:
            return render(request,'login.html')
    form = LoginForm()
    return render(request,'login.html',{'form':form})

def home(request):
    return render(request,'home.html')

