from django.shortcuts import render

class APIErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        if isinstance(exception, requests.exceptions.RequestException):
            return render(request, 'error.html', {
                'error': 'Unable to connect to the API service. Please try again later.'
            })
        return None