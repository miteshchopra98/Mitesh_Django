from django.shortcuts import *
from users.forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
from users.models import Profile

# Create your views here.


def Register(request):

    form = RegisterForm(request.POST or None)

    if request.method == 'POST':
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            print(username)
            print(password1)
            print(password2)
            id = form.instance.id
            return redirect('users:profformcreate', userid = id)

        
        
        else:

            
            username = form.data.get('username')
            user_exists = User.objects.filter(username=username).exists()
            password1 = form.data.get('password1')
            password2 = form.data.get('password2')
            
            if user_exists:
                messages.success(
                    request,
                    'Username already exists'
                   )

            elif password1 != password2:
               messages.success(
                    request,
                    'Password does not match'
                   )

            elif len(password1)<8:
               messages.success(
                    request,
                    'password length cannot be less than 8'
                   )

            
        
            print('username = ',username)
            print('password1 = ',password1)
            print('password2 = ',password2)
                  
            return redirect('register')
    
    context={
        'form':form
        }

    return render(request, 'users/register.html', context)



def Login_view(request):

    if request.method == 'POST':
        username  = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        print(user)

        if user is None:
            messages.success(
                request,
                'Username or Password is not valid'
            )
            return redirect('login')

        elif user.is_superuser:
            login(request, user)
            messages.success(
                request,
                'Admin {}, you have been successfully logged in'.format(username)
            )
            return redirect('food:Index')

        elif user is not None:
            login(request, user)
            messages.success(
                request,
                '{}, you have been successfully logged in'.format(username)
            )
            return redirect('food:Index')

            
        
        
    context = {

        }
    return render(request, 'users/login.html', context)



def logout_view(request):
    

    if request.method == 'POST':
        logout(request)
        messages.success(
            request,
            'You have been logged out'
        )
        return redirect('food:Index')

    return render(request, 'users/logout.html')



def ProfileView(request):

    if not request.user.is_authenticated:
        return redirect('login')
    
    context ={
        }


    return render(request,'users/profile.html', context)



def ProfileFormEdit(request, userid):


    prof = Profile.objects.get(user=userid)
    form = ProfileForm(request.POST or None, request.FILES or None ,instance=prof)
    
    if request.method == 'POST':
        form.save()
        return redirect('profile')

    
    context = {
        'userid':userid,
        'form': form
        }

    return render(request, 'users/profform.html', context)

def ProfFormCreate(request, userid):
    prof = Profile.objects.get(user=userid)
    form = ProfileForm(request.POST or None, request.FILES or None, instance=prof)

    if request.method == 'POST':
        print('userid: {}'.format(userid))

        
        if form.is_valid():
            form.save()
            return redirect('login')
                

    context ={

        'userid':userid,
        'form':form
        }
    return render(request, 'users/profform.html', context)