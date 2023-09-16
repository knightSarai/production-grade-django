from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI, Router
from ninja.security import django_auth

from knightauth.api import register_router, session_auth_router

api = NinjaAPI(
    title='KnightAuth',
    auth=[django_auth],
    csrf=True,
)

test_router = Router()


@test_router.get("", auth=None)
def test(request):
    return {"hello": "world"}


@test_router.post("", auth=None)
def token_post(request):
    return {'message': 'Hello, world!'}


api.add_router('auth', session_auth_router)
api.add_router('auth/', register_router)
api.add_router('test/', test_router)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]
