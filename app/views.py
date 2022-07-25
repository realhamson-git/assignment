from django.shortcuts import render, redirect
from .models import extendUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def signin(request):
    if(request.user.is_authenticated):
        return redirect('/dashboard')
    else:
        if(request.method == 'POST'):
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username= username, password= password)
            if(user):
                login(request, user)
                return redirect('/dashboard')
            messages.warning(request, 'wrong credential...')
            return redirect('/')
    return render(request, 'signin.html')

def signup(request):
    if(request.method == 'POST'):
        postReq = request.POST
        username = postReq.get('username')
        firstname =  postReq.get('firstname')
        lastname = postReq.get('lastname')
        password = postReq.get('password')
        confirmpassword = postReq.get('confirmPassword')
        email = postReq.get('email')
        address1 = postReq.get('address1')
        address2 = postReq.get('address2') 
        profile = request.FILES.get('profile')
        types = postReq.get('type')
        combineAddress = address1 + '' + address2
        print(username, profile, types, combineAddress)
        if(password == confirmpassword):
            userobj = User.objects.create_user(username = username,first_name=firstname,last_name=lastname,email = email, password = password)
            extend = extendUser(user = userobj, address = combineAddress, profile = profile, types = types ).save()
            messages.success(request, 'Account successfully created')
        messages.error(request, 'Password does not same...')
        return redirect('/signup')
    return render(request, 'signup.html')

def Logout(request):
    logout(request)
    return redirect('/')
    
@login_required
def dashboard(request):
    user = request.user
    userObj = User.objects.get(username = user)
    extendObj = extendUser.objects.get(user = user)
    if(extendObj.types == 'doctor'):
        return render(request, 'dashboard.html', {'extend': extendObj,'user':userObj,'type':'doctor'})
    if(extendObj.types == 'patient' ):
        return render(request, 'dashboard.html', {'extend':extendObj,'user':userObj,'type':'patient'})
    return redirect('/')

