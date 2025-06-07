from django.shortcuts import render, redirect
from .forms import MetodoForm
from .metodos import (
    metodo_biseccion,
    metodo_newton
)

def inicio(request):
    if request.method == 'POST':
        form = MetodoForm(request.POST)
        if form.is_valid():
            metodo = form.cleaned_data['metodo']
            funcion = form.cleaned_data['funcion']
            tolerancia = form.cleaned_data['tolerancia']
            max_iter = form.cleaned_data['max_iter']
            
            if metodo == 'biseccion':
                a = form.cleaned_data['a']
                b = form.cleaned_data['b']
                resultado = metodo_biseccion(funcion, a, b, tolerancia, max_iter)
            elif metodo == 'newton':
                x0 = form.cleaned_data['x0']
                resultado = metodo_newton(funcion, x0, tolerancia, max_iter)
            else:  # newton_modificado
                x0 = form.cleaned_data['x0']
                resultado = metodo_newton(funcion, x0, tolerancia, max_iter, modificado=True)
            
            resultado['metodo'] = metodo
            resultado['funcion'] = funcion
            request.session['resultado'] = resultado
            return redirect('metodos_numericos:calcular')
    else:
        form = MetodoForm()
    
    return render(request, 'metodos_numericos/inicio.html', {'form': form})

def calcular_raiz(request):
    resultado = request.session.get('resultado', {})
    return render(request, 'metodos_numericos/resultados.html', resultado)