from django.shortcuts import render
from .models import Restaurant

class homepage(request):
    restaurant = Restaurant.objects.first()
    context = { 
        'restaurant_name' : restaurant.name if restaurant else 'my Restaurant'
        'phone_number' : restaurant.phone_number if restaurant else 'phone number'
        }
    return render(request, 'homepage.html', context)

def about_page(request):
    return render(request, 'about.html')
    
def menu_list(request):
    menu_lists = [
        {"name": "margherita pizza", "price":250, "description": "classic pizza with tomato and mozzarella"}
        {"name": "veg burger", "price":150, "description": "classic burger with tomato and mozzarella"}
        {"name": "pasta", "price":300, "description": "classic pasta"}
        {"name": "Paneer tikka", "price":250, "description": "classic paneer tikka with spices"}
    ] 
    return render(request, 'menuview.html', {"menu_items": menu_items})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request,'contact.html')