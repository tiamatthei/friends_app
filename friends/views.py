from django.http import HttpResponse, JsonResponse
from .models import User, MetaUser
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def index(request):
    #todo_list = User.objects.order_by('-pub_date')[:5]
    return render(request, 'index.html')

@csrf_protect
def friends(request):
    name = request.GET.get("name", '')
    user_data = list(User.objects.filter(name=name).values())[0]
    meta_user = MetaUser.objects.filter(user=User.objects.filter(name=name).values()[0]['id'])[0]
    friends = list(meta_user.friends.all())
    not_friends = list(User.objects.exclude(id=user_data['id']))
    
    for friend in friends:
        if friend in not_friends:
            not_friends.remove(friend)


    print(friends)
    print(MetaUser.objects.filter(user=User.objects.filter(name=name).values()[0]['id']).values()[0])
    if len(user_data)>0:
        context = {'user_data': user_data, "not_friends":not_friends, "friends":friends}
        return render(request, 'friends.html', context)
            
    else :
        return render(request, 'index.html')


def user(request):
    id = request.GET.get("user_id", '')
    user_data = list(User.objects.filter(id=id).values())[0]
    if len(user_data)>0:
        context = {'user_data': user_data}
        return render(request, 'user.html', context)
            
    else :
        return render(request, 'index.html')

def add_friend(request):
    if request.method == 'POST':
        user_id = request.POST.get("user_id", '')
        new_friend = request.POST.get("new_friend", '')
        print("u_id: ", user_id, "  ", new_friend)
        
        meta_user = MetaUser.objects.filter(user=User.objects.filter(id=user_id).values()[0]['id'])[0]
        print(meta_user)
        friends = meta_user.friends.add(new_friend)
        print(friends)
        
        data = {'message':"Success", "status":200}
        return JsonResponse(data, status=data['status'])
    
    data = {'message':"ERROR ON SUBMIT", "status":400}
    return JsonResponse(data, status=data['status'])


def remove_friend(request):
    if request.method == 'POST':
        user_id = request.POST.get("user_id", '')
        to_delete = request.POST.get("to_delete", '')
        print("u_id: ", user_id, "  ", to_delete)
        
        meta_user = MetaUser.objects.filter(user=User.objects.filter(id=user_id).values()[0]['id'])[0]
        print(meta_user)
        friends = meta_user.friends.remove(to_delete)
        print(friends)
        
        data = {'message':"Success", "status":200}
        return JsonResponse(data, status=data['status'])
    
    data = {'message':"ERROR ON SUBMIT", "status":400}
    return JsonResponse(data, status=data['status'])



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
        data = {'message':"Success, voting started", "status":200}
        return JsonResponse(data, status=data['status'])
    
    data = {'message':"ERROR ON SUBMIT", "status":400}
    return JsonResponse(data, status=data['status'])


@csrf_protect
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = list(User.objects.filter(email=email, password=password).values())
        if len(user) == 0:
            data = {'message':"ERROR ON SUBMIT", "status":400}
            return JsonResponse(data, status=data['status'])
        else:
            user = user[0]
        
        data = {'message':"Success, voting started", "status":200, "user_data":user}
        return JsonResponse(data, status=data['status'])
    
    data = {'message':"ERROR ON SUBMIT", "status":400}
    return JsonResponse(data, status=data['status'])


