from django.urls import path, include
from sportswatch.schema import SchemaView

urlpatterns = [
    path('api/v1/', include('app.urls')),
    path('openapi/', SchemaView.as_view(), name='schema view'),
]
