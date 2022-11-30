from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import AppUser
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login, logout
from django.core import serializers

# Create your views here.
def index(_):
    print("Requested index!")
    return HttpResponse(open('static/index.html').read())

@api_view(['POST'])
def sign_up(request):
    try:
        args = {'username': request.data['email'], 'password': request.data['password'], 'email': request.data['email']}
        new_user = AppUser(**args)
        new_user.full_clean()
        AppUser.objects.create_user(**args)
    except Exception as e:
        print(str(e))
        return JsonResponse({'err': 'Sign up failed!'})

    return JsonResponse({'success': 'Successfully signed up!'})

@api_view(['POST'])
def log_in(request):
    user = authenticate(username=request.data['email'], password=request.data['password'])
    if user is not None:
        if user.is_active:
            try:
                login(request._request, user)
            except Exception as e:
                print(str(e))
                return JsonResponse({'err': 'Login failed!'})

            return JsonResponse({'success': f'Logged in as {request.data["email"]}'})
        else:
            return JsonResponse({'err': 'Login failed!'})
    else:
        return JsonResponse({'err': 'Login failed!'})

@api_view(['GET'])
def who_am_i(request):
    if request.user.is_authenticated:
        data = serializers.serialize("json", [request.user], fields=['email', 'username'])

        return HttpResponse(data)
    else:
        return JsonResponse({'user': None})

@api_view(['POST'])
def log_out(request):
    logout(request)
    return JsonResponse({'success': "Successfully logged out!"})
