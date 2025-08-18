from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length = 255)
    phone_number = models.CharField(max_length = 20)

    def __str__(self):
        return self.name


class RestaurantLocation(models.Model):
    address = models.CharField(max_length = 255)
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)
    zip_code = models.CharField(max_length = 100)

    def __str__(self):
        return f"{self.adress}, {self.city}, {self.state} - {self.zip_code}"


class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menu_items')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name