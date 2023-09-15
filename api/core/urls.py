from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from ninja import NinjaAPI
from ninja.security import django_auth

from knightauth.api import register_router, session_auth_router

api = NinjaAPI(
    title='KnightAuth',
    auth=[django_auth],
    csrf=True,
)

api.add_router('auth', session_auth_router)
api.add_router('auth/', register_router)


@api.get('test', url_name='test', auth=None)
def test_get(request):
    return {'message': 'Hello, world!'}


@api.post('test', url_name='test', auth=None)
def token_post(request):
    return {'message': 'Hello, world!'}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]
