import datetime

class RequestloggingMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("Request Logging Middleware initialized")

    def __call__(self,request):
        print(f"incoming request:{request.path} at {datetime.datetime.now()}")
        response = self.get_response(request)
        print(f"outgoing response:{request.path} at {datetime.datetime.now()}")
        return response    