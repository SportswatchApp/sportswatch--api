from django.urls import path

from app.endpoints.docs import DocsView
from app.endpoints.user.create import CreateUserEndpoint
from app.endpoints.user.login import LoginEndpoint

urlpatterns = [
    path('', DocsView.as_view(), name='docs'),
    path('login/', LoginEndpoint.as_view(), name='login endpoint'),
    path('users/', CreateUserEndpoint.as_view(), name='create user endpoint')
]
