from django.urls import reverse_lazy
from cars.models import Car
from cars.forms import CarModelForm
from django.contrib.auth.decorators import login_required
from django. utils.decorators import method_decorator
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView,RedirectView


class Redirecionar(RedirectView):
    pattern_name = 'cars_list'

class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars' 
    
    def get_queryset(self):
        queryset = super().get_queryset().order_by('-model')
        search = self.request.GET.get('search')
        orderby = self.request.GET.get('orderby')
        if search and orderby:
            queryset = queryset.filter(brand__name__icontains=search).order_by(orderby)

        if search:
            queryset = queryset.filter(brand__name__icontains=search) 
        if orderby:
            queryset = queryset.order_by(orderby) 
        
        return queryset

@method_decorator(login_required(login_url='login'),name='dispatch')
class NewCarCreatView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = reverse_lazy('cars_list')

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'

@method_decorator(login_required(login_url='login'),name='dispatch')
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'
 
    def get_success_url(self):
        return reverse_lazy('car_detail',kwargs={'pk':self.object.pk})

@method_decorator(login_required(login_url='login'),name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = reverse_lazy('cars_list')