from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import User, MetaUser
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def index(request):
    #todo_list = User.objects.order_by('-pub_date')[:5]
    return render(request, 'index.html')

def friends(request):
    print(request)
    #todo_list = User.objects.order_by('-pub_date')[:5]
    return render(request, 'friends.html')

def user(request):
    #todo_list = User.objects.order_by('-pub_date')[:5]
    return render(request, 'index.html')

@csrf_protect
def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        alias = request.POST['alias']
        email = request.POST['email']
        password = request.POST['password']
        dob = request.POST['birthday']

        user = User.objects.create(name=name, email=email, password=password, alias=alias, birthday=dob)
        user.save()
        
        meta_user = MetaUser(user=user)
        meta_user.save()

        # You can also save additional data like the date of birth (dob)
        # by creating a separate model for user profile information and
        # using a OneToOneField to link it to the User model.

        # profile = UserProfile(user=user, dob=dob)
        # profile.save()
        return HttpResponseRedirect('/friends')
    
    return JsonResponse({'error': 'Registration failed'})

