from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

def add_variable_to_context(request):
    print('here')
    isAjax=False
    if request.is_ajax():
        isAjax=True

    return {'isAjax': isAjax}

class MyMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if request.is_ajax():
            response['Location'] = request.get_full_path()
            response['Cache-Control'] = 'no-cache'

        return response
