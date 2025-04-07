from django import forms
from cars.models import Car

class CarModelForm(forms.ModelForm):
    
    class Meta:
        model = Car
        fields = '__all__'

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value', 'Valor mínimo do veículo deve ser de R$20.000,00')
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1975:
            self.add_error('factory_year', 'Ano de fabricação mínimo do veículo deve ser 1975')
        return factory_year
    
    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
        if photo is None:
            self.add_error('photo', 'É necessário anexar uma foto do veículo!')
        return photo
    