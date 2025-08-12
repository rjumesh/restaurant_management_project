from django.shortcuts import render
from .models import Restaurant

class homepage(request):
    restaurant = Restaurant.objects.first()
    return render(request, 'homepage.html', {'restaurant_name' : restaurant.name if restaurant else 'my Restaurant'})

def about_page(request):
    return render(request, 'about.html')
    