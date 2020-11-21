from django.http import HttpResponse
from django.views import View


class SchemaView(View):

    def get(self, request):
        data = open('openapi-schema.yml').read()
        return HttpResponse(content=data, content_type='text/x-yaml')
