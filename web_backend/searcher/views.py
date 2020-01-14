import json

from django.core import signing
from django.http import JsonResponse, HttpResponse

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import login, authenticate, get_user
from django.contrib.auth import logout

from django.contrib.admin.views.decorators import staff_member_required

from searcher.models import MyUser
from django.contrib.sessions.models import Session


@login_required
@csrf_exempt
def hello(request):
    print("Hello")
    return HttpResponse(content='hello')


@csrf_exempt
def search(request):
    print("Hello")
    return HttpResponse(content='hello')




@csrf_exempt
def authentication(request):
    user_info = json.loads(request.body)

    user = authenticate(request, username=user_info['username'], password=user_info['password'])
    if user is not None:
        login(request, user)
        print("Successes!")
    else:
        print(":(")

    return HttpResponse(content='ok')


@csrf_exempt
def registration(request):
    user_info = json.loads(request.body)

    if not MyUser.objects.filter(username=user_info['username']).count():
        MyUser.objects.create(
            username=user_info['username'],
            password=user_info['password']

        )
    else:
        print("User exist")

    return JsonResponse(

        {
            'Successes': 'authentication'

        }
    )
