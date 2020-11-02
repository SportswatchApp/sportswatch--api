from rest_framework.views import APIView


class PublicMixin(APIView):

    model = None
    request_obj = None
