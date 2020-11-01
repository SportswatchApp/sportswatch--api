from django.urls import path

from app.endpoints.docs import DocsView
from app.endpoints.user.create import CreateUserEndpoint

urlpatterns = [
    path('', DocsView.as_view(), name='docs'),
    path('users/', CreateUserEndpoint.as_view(), name='create user endpoint')
]
