from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_brands),
    path('new/', views.new_brand),
    path('<int:brand_id>', views.specific_brand),
    path('<int:brand_id>/edit', views.edit_brand),

    path('<int:brand_id>/cars', views.list_cars),
    path('<int:brand_id>/cars/new', views.new_car),
    path('<int:brand_id>/cars/<int:car_id>', views.specific_car),
    #path('<int:brand_id>/cars/<int:car_id>/edit', views.edit_car)
]
