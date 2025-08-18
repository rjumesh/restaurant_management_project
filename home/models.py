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