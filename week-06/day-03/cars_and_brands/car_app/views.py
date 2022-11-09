from django.shortcuts import render
from django.http import HttpResponse
from .models import Brand
from django.core.files.storage import FileSystemStorage

def list_brands(request):
    try:
        id = int(request.POST.get('id'))
        brand = Brand.objects.filter(id=id)
        brand_name = request.POST.get('name')
        if type(brand_name) == str and brand_name.strip() != '':
            brand.update(name=brand_name)
    except:
        brand_name = request.POST.get('name')
        if type(brand_name) == str and brand_name.strip() != '' and request.POST.get('id') == None:
            Brand.objects.create(name=brand_name)
    
    brands = Brand.objects.all()
    return render(request, 'car_app/list_brand.html', {'brands': brands})

def new_brand(request):
    return render(request, 'car_app/new_brand.html')

def specific_brand(_, brand_id):
    brand = Brand.objects.get(id=brand_id)
    return HttpResponse(
        f"""
        <h1>{brand.name}</h1>
        <ul><li><a href='/brands/{brand.id}/cars'>List of cars</a></li></ul>
        <a href='/brands/'>Home</a>
        """
    )

def edit_brand(request, brand_id):
    brand = Brand.objects.get(id=brand_id)
    return render(request, 'car_app/edit_brand.html', {'brand': brand})

def list_cars(request, brand_id):
    brand = Brand.objects.get(id=brand_id)
    try:
        model = request.POST['name']
        year = request.POST['year']
        color = request.POST['color']
        file = request.FILES["image"]
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        url = fs.url(filename)
        brand.cars.create(model=model, year=year, color=color, image=url)
    finally:
        return render(request, 'car_app/list_car.html', {'brand': brand})

def specific_car(request, brand_id, car_id):
    brand = Brand.objects.get(id=brand_id)
    car = brand.cars.get(id=car_id)
    return render(request, 'car_app/specific_car.html', {'car': car})

def new_car(request, brand_id):
    brand = Brand.objects.get(id=brand_id)
    return render(request, 'car_app/new_car.html', {'brand': brand})
