from django.shortcuts import render
from math import factorial

def factorials_view(request):
    numbers = range(3, 9)
    factorials = {num: factorial(num) for num in numbers}
    return render(request, 'app53/factorials.html', {'factorials': factorials})
