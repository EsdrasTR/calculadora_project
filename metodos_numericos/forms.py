from django import forms

METODOS = (
    ('biseccion', 'Bisección'),
    ('newton', 'Newton-Raphson'),
    ('newton_modificado', 'Newton-Raphson Modificado'),
)

class MetodoForm(forms.Form):
    funcion = forms.CharField(
        label='Función polinómica (ej: x**3 - 2*x - 5)',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    metodo = forms.ChoiceField(
        label='Método numérico',
        choices=METODOS,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    # Campos para Bisección
    a = forms.FloatField(
        label='Extremo inferior (a)',
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    b = forms.FloatField(
        label='Extremo superior (b)',
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    
    # Campos para Newton
    x0 = forms.FloatField(
        label='Valor inicial (x0)',
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    
    # Campos comunes
    tolerancia = forms.FloatField(
        label='Tolerancia (error permitido)',
        initial=0.0001,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    max_iter = forms.IntegerField(
        label='Máximo número de iteraciones',
        initial=100,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    
    def clean(self):
        cleaned_data = super().clean()
        metodo = cleaned_data.get('metodo')
        
        if metodo == 'biseccion':
            a = cleaned_data.get('a')
            b = cleaned_data.get('b')
            if a is None or b is None:
                raise forms.ValidationError("Para el método de bisección, se requieren ambos extremos del intervalo.")
            if a >= b:
                raise forms.ValidationError("El extremo inferior (a) debe ser menor que el extremo superior (b).")
        else:
            x0 = cleaned_data.get('x0')
            if x0 is None:
                raise forms.ValidationError("Para los métodos de Newton, se requiere un valor inicial (x0).")
        
        return cleaned_data