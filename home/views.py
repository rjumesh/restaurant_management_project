from django.shortcuts import render
from .models import Restaurant
from .models import MenuItem

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



def menu_list(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'menu.html', {'menu_items': menu_items})

    from django.db import models
    from restaurant.models import Restaurant   # adjust import if needed

    class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menu_items')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)  # ✅ Added field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
    return self.name
    