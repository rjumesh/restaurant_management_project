from django.urls import path
from .views import *

urlpatterns = [
    path('about/'',views.about_page, name='about'),    
    path('menu/'',views.menu_list, name='menu'),    
    path('contact/'',views.contact, name='contact'),
]