from django.shortcuts import render
from .models import Restaurant

def homepage(request):
    restaurant = Restaurant.objrcts.first()
    return render(request, 'homepage.html', {'restaurant_name': restaurant.name if restaurant else 'My Restaurant'})