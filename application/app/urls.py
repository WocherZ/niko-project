from django.urls import path
from .views import *

urlpatterns = [
    path('register', register, name='register'),
    path('authorization', authorization, name='authorization'),

]