import os

from django.http import HttpResponse
from django.views import View
from django.conf import settings

from sportswatch import settings


class SchemaView(View):

    def get(self, request):
        data = open(os.path.join(settings.BASE_DIR, settings.STATIC_URL, 'openapi-schema.yml')).read()
        return HttpResponse(content=data, content_type='text/x-yaml')
