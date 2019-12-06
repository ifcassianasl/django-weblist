from django.contrib import admin
from django.urls import path, include
from web_list import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web_list.urls'))
]
