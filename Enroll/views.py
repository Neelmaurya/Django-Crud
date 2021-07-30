from django.shortcuts import render, redirect, HttpResponseRedirect
from Enroll.models import Registration, Student
from django.contrib.auth.models import User, auth
from .forms import StudentRegistration
from django.contrib import messages

# Create your views here.

def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            do = fm.cleaned_data['dob']
            em = fm.cleaned_data['email']
            mo = fm.cleaned_data['mobile']
            pw = fm.cleaned_data['password']
            reg = Student(name=nm, dob=do, email=em, mobile=mo, password=pw)
            fm.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = Student.objects.all()
    return render(request, 'addandshow.html', {'form':fm, 'stu':stud})

def registration(request):
    if request.method == "POST":
        name = request.POST.get('name')
        # dob = request.POST.get('dob')
        email = request.POST.get('email')
        # mobile = request.POST.get('mobile')
        pwd = request.POST.get('pwd')
        # cpwd = request.POST.get('cpwd')

        #registration = Registration(name=name, dob=dob, email=email, mobile=mobile, pwd=pwd, cpwd=cpwd)
        #registration.save()
        x = User.objects.create_user(username=email, first_name=name, last_name=name, email=email, password=pwd)
        x.save()
        messages.info(request, 'Student Registerd Sussesfully')
    return render(request, 'registration.html')

# This function will Delete
def delete_data(request, id):
    if request.method == 'POST':
        pi = Student.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

def update_data(request, id):
    if request.method == 'POST':
        pi = Student.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Student.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'updatestudent.html', {'form':fm})

# This is Login Function
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect("login")
    else:
        return render(request, 'login.html')
    #return render(request, 'login.html')

# This is Logout Function.
def logout(request):
    auth.logout(request)
    return redirect('/')