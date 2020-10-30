from django.urls import path

from app.endpoints.user.create import CreateUserEndpoint

urlpatterns = [
    path('users/', CreateUserEndpoint.as_view(), name='create user endpoint')
]
