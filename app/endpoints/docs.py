from django.shortcuts import render
from django.views import View

from sportswatch import urls


class DocsView(View):

    def get(self, request):
        return render(request, 'docs.html', context={
            'endpoints': urls.urlpatterns
        })
