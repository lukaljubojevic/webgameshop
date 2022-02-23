from django.contrib import admin
from django.urls import path
from .views.home import Index , trgovina
from .views.registracija import Signup
from .views.login import Login , logout
from .views.kosarica import Kosarica
from .middlewares.auth import  auth_middleware

  
  
urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('trgovina', trgovina, name='trgovina'),
    path('registracija', Signup.as_view(), name='registracija'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('kosarica', auth_middleware(Kosarica.as_view()), name='kosarica'),
]