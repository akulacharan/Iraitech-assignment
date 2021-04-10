from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User,auth
from .models import User
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password=request.POST['password']
        confirm_password = request.POST['confirm-password']

        if User.objects.filter(username=username).exists():
            return HttpResponse("<script>alert('username taken')</script>")
            #messages.info(request,'username-taken')
        elif User.objects.filter(email=email).exists():
            return HttpResponse("<script>alert('email taken')</script>")
            #messages.info(request, 'email-taken')
        elif User.objects.filter(mobile=mobile).exists():
            return HttpResponse("<script>alert('mobile taken')</script>")
        # messages.info(request, mobile-taken')

        elif confirm_password != password:
            return HttpResponse("<script>alert('password doesnot matched')</script>")

        else:
            user=User.objects.create_user(username=username,password=password,email=email,mobile=mobile)
            user.save();
            messages.info(request, 'user-created')
        return redirect('/login')
    return render(request,'register.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            return HttpResponse('wrong username / password')
            messages.info(request, 'invalid credentials')
    else:
        return render(request,'login.html')

def home(request):
    return render(request,'base.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def calculate(request,username):
    global g
    g = username
    content = User.objects.get(username=g)
    if request.method == 'POST':
        n_value = request.POST['nvalue']
        x_value = request.POST['xvalue']
        #convert into integer
        n_value = int(n_value)
        x_value = int(x_value)

        def summation(x, n):
            result = 0
            for i in range(1, n + 1):
                expresult = 1 / (x ** i)
                result += expresult
            return result

        print(summation(x_value, n_value))
        re = summation(x_value, n_value)
        return render(request, 'calculate.html', {'re': re,'content':content})

    return render(request,'calculate.html')