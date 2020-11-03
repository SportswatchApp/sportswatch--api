from rest_framework.response import Response as RestResponse


class Response(RestResponse):

    def __init__(self, request, listener):
        status, data = self._extract_data(listener.get_response(), request)
        if status > 227:
            data = {
                'detail': data,
                'status': status,
            }
        super().__init__(
            data=data,
            status=status,
            template_name=None,
            headers=None,
            exception=False,
            content_type='application/json'
        )

    def _extract_data(self, message, request):
        if isinstance(message, tuple):
            return message
        elif isinstance(message, dict):
            language = self._extract_language(request)
            return message['status'], message[language]
        else:
            raise TypeError('Cannot recognize type' + str(message))

    def _extract_language(self, request):
        return request.headers.get('Content-Language', 'en')
