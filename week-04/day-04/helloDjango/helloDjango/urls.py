"""helloDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
import math

def rectAreaHandler(request):
    try:
        height = int(request.GET.get("height"))
        width = int(request.GET.get("width"))
        return HttpResponse(f"<h1>ANSWER IS: {height * width}</h1>")
    except:
        response = HttpResponse("<h1>Query params were invalid!</h1>")
        response.status_code = 418
        return response

def rectPerimeterHandler(request):
    try:
        height = int(request.GET.get("height"))
        width = int(request.GET.get("width"))
        return HttpResponse(f"<h1>ANSWER IS: {(height * 2) + (width * 2)}</h1>")
    except:
        response = HttpResponse("<h1>Query params were invalid!</h1>")
        response.status_code = 418
        return response

def circleAreaHandler(request):
    try:
        radius = int(request.GET.get("radius"))
        return HttpResponse(f"<h1>ANSWER IS: {math.pi * radius * radius}</h1>")
    except:
        response = HttpResponse("<h1>Query params were invalid!</h1>")
        response.status_code = 418
        return response

def circlePerimeterHandler(request):
    try:
        radius = int(request.GET.get("radius"))
        return HttpResponse(f"<h1>ANSWER IS: {math.pi * 2 * radius}</h1>")
    except:
        response = HttpResponse("<h1>Query params were invalid!</h1>")
        response.status_code = 418
        return response

def rectAreaHandlerOrdered(_, height, width):
        return HttpResponse(f"<h1>ANSWER IS: {height * width}</h1>")

def rectPerimeterHandlerOrdered(_, height, width):
        return HttpResponse(f"<h1>ANSWER IS: {(height * 2) + (width * 2)}</h1>")

def circleAreaHandlerOrdered(_, radius):
    return HttpResponse(f"<h1>ANSWER IS: {math.pi * radius * radius}</h1>")

def circlePerimeterHandlerOrdered(_, radius):
    return HttpResponse(f"<h1>ANSWER IS: {math.pi * 2 * radius}</h1>")

def rootHandler(_):
    return HttpResponse("<h1>Welcome to the geometry site!</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', rootHandler),
    path('rectangle/area', rectAreaHandler),
    path('rectangle/perimeter', rectPerimeterHandler),
    path('circle/area', circleAreaHandler),
    path('circle/perimeter', circlePerimeterHandler),

    path('rectangle/area/<int:height>/<int:width>', rectAreaHandlerOrdered),
    path('rectangle/perimeter/<int:height>/<int:width>', rectPerimeterHandlerOrdered),
    path('circle/area/<int:radius>', circleAreaHandlerOrdered),
    path('circle/perimeter/<int:radius>', circlePerimeterHandlerOrdered)
]
