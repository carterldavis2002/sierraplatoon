from django.shortcuts import render
from django.http import HttpResponse
import uuid
from datetime import datetime

users = {}

# Simple session implementation
# def home(request):
#     user_id = request.COOKIES.get('user_id')
#     user = users.get(user_id)

#     if not user:
#         user_id = str(uuid.uuid4())
#         users[user_id] = {'views': 0}
#         user = users.get(user_id)
#     else:
#         users[user_id]['views'] += 1

#     response = render(request, 'challenge/index.html', user)
#     response.set_cookie('user_id', user_id)
#     return response

# Implementation using Django session middleware
def home(request):
    # No custom middleware session updating
    # if request.session.get('views') is None:
    #     request.session['views'] = 0
    #     request.session['start'] = datetime.now().__str__()
    # else:
    #     request.session['views'] += 1
    #     request.session['current'] = datetime.now().__str__()
    
    return render(request, 'challenge/index.html', {'views': request.session.get('views'), 'start': request.session.get('start'), 'current': request.session.get('current')})

# Second view to show session persists accross routes
def second_view(request):
    # No custom middleware session updating
    # if request.session.get('views') is None:
    #     request.session['views'] = 0
    #     request.session['start'] = datetime.now().__str__()
    # else:
    #     request.session['views'] += 1
    #     request.session['current'] = datetime.now().__str__()

    return HttpResponse(f"<h1>Still views: {request.session.get('views')}</h1>")

# Custom middleware to automatically update session variables
# for every route request (registerd in settings.py under MIDDLEWARE)
def counter_middleware(get_response):

    def middleware(request):
        if request.session.get('views') is None:
            request.session['views'] = 0
            request.session['start'] = datetime.now().__str__()
        else:
            request.session['views'] += 1
            request.session['current'] = datetime.now().__str__() 

        response = get_response(request)
        return response

    return middleware