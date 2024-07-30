from django.contrib import admin
from django.urls import path
from nejlepsiProjekt.views import partner_list, add_partner, register, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('partners/', partner_list, name=''),
    path('add-partner/', add_partner, name='rate_partner'),
    path('register/', register, name='register'),
]
