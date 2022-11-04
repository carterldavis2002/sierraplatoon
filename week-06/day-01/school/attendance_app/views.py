from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from . import models

def index(request):

    students = models.Student.objects.all() # get list of all students

    # the home page should show a roster of all the students, so we pass the whole list into the template
    return render(request, 'attendance_app/index.html', {'students': students} )

@csrf_exempt
# this function creates a cartItem / updates a cartItem quantity
def add_student(request):
    body = json.loads(request.body) 

    new_student = models.Student(name = body['name'], email = body['email'])
    new_student.save()

    return JsonResponse({'success':True})
