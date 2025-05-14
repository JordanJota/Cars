from django import forms
from cars.models import Car

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
    
    def clean_value(self):     
         value  = self.cleaned_data.get('value')
         if value < 20000:
             self.add_error('value','Valor minimo do carro deve de ser $20.000')
         return value
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

