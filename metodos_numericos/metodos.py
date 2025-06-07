import numpy as np
import sympy as sp
from sympy import sympify, Symbol
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def graficar_funcion(funcion_str, a=None, b=None, raiz=None):
    """Genera una gráfica de la función y la convierte a base64 para HTML."""
    x = Symbol('x')
    try:
        funcion = sympify(funcion_str)
    except:
        return None
    
    # Convertir la función sympy a una función numpy
    f = sp.lambdify(x, funcion, 'numpy')
    
    # Determinar el rango de visualización
    if a is not None and b is not None:
        x_vals = np.linspace(a-1, b+1, 400)
    else:
        x_vals = np.linspace(-10, 10, 400)
    
    y_vals = f(x_vals)
    
    plt.figure()
    plt.plot(x_vals, y_vals, label=f'f(x) = {funcion_str}')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True)
    
    if raiz is not None:
        plt.scatter([raiz], [0], color='red', label=f'Raíz aproximada: {raiz:.4f}')
    
    if a is not None and b is not None:
        plt.axvspan(a, b, color='yellow', alpha=0.3, label='Intervalo [a, b]')
    
    plt.legend()
    plt.title('Gráfica de la función')
    
    # Guardar la imagen en un buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)
    
    # Convertir a base64 para mostrar en HTML
    image_png = buffer.getvalue()
    buffer.close()
    return base64.b64encode(image_png).decode('utf-8')

def metodo_biseccion(funcion_str, a, b, tolerancia, max_iter):
    """Implementación del método de bisección."""
    x = Symbol('x')
    try:
        funcion = sympify(funcion_str)
    except:
        return {'error': 'Función no válida'}
    
    f = sp.lambdify(x, funcion, 'numpy')
    
    # Verificar condición de cambio de signo
    if f(a) * f(b) >= 0:
        return {'error': 'No hay cambio de signo en el intervalo [a, b]'}
    
    iteraciones = []
    for i in range(max_iter):
        c = (a + b) / 2
        error = abs(b - a) / 2
        iteraciones.append({
            'iteracion': i + 1,
            'a': a,
            'b': b,
            'c': c,
            'f(c)': f(c),
            'error': error
        })
        
        if error < tolerancia:
            break
            
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    
    return {
        'raiz': (a + b) / 2,
        'iteraciones': iteraciones,
        'imagen': graficar_funcion(funcion_str, a, b, (a + b) / 2)
    }

def metodo_newton(funcion_str, x0, tolerancia, max_iter, modificado=False):
    """Implementación del método de Newton-Raphson (estándar o modificado)."""
    x = Symbol('x')
    try:
        funcion = sympify(funcion_str)
    except:
        return {'error': 'Función no válida'}
    
    f = sp.lambdify(x, funcion, 'numpy')
    df = sp.lambdify(x, funcion.diff(x), 'numpy')
    
    if modificado:
        df_x0 = df(x0)
    
    iteraciones = []
    x_actual = x0
    
    for i in range(max_iter):
        try:
            f_val = f(x_actual)
            df_val = df(x_actual) if not modificado else df_x0
            x_siguiente = x_actual - f_val / df_val
        except:
            return {'error': 'División por cero o punto no válido'}
        
        error = abs(x_siguiente - x_actual)
        iteraciones.append({
            'iteracion': i + 1,
            'x_actual': x_actual,
            'f(x)': f_val,
            'f\'(x)': df_val,
            'x_siguiente': x_siguiente,
            'error': error
        })
        
        if error < tolerancia:
            break
            
        x_actual = x_siguiente
    
    return {
        'raiz': x_actual,
        'iteraciones': iteraciones,
        'imagen': graficar_funcion(funcion_str, raiz=x_actual)
    }