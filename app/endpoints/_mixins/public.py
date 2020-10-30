from rest_framework.views import APIView


class PublicMixin(APIView):

    def get_model(self):
        raise NotImplementedError()
