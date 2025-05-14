from django.urls import path
from cars.views import CarsListView,NewCarCreatView,CarDetailView,CarUpdateView,CarDeleteView,Redirecionar

urlpatterns = [
    path('cars/',CarsListView.as_view(),name='cars_list'),
    path('new_car/',NewCarCreatView.as_view(),name='new_car'),
    path('car/<int:pk>/',CarDetailView.as_view(),name='car_detail'),
    path('car/<int:pk>/update/',CarUpdateView.as_view(),name='car_update'),
    path('car/<int:pk>/delete/',CarDeleteView.as_view(),name='car_delete'),
    path('',Redirecionar.as_view(),name='Home'),
    ]
