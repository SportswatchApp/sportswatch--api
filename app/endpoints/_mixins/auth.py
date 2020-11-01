from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class AuthMixin(APIView):
    model = None
    request_obj = None
    permission_classes = (IsAuthenticated,)
