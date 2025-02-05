
from django.contrib import admin
from django.urls import path

from core.views import home, explore, login, about

urlpatterns = [
    path('', home, name='home'),
    path('explore/', explore, name='explore'),
    path('login/', login, name='login'),
    path('about/', about, name='about'),
    path('admin/', admin.site.urls),
]
