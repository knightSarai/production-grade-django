from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def test(request):
    return HttpResponse("Hello, world.")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test),
]
