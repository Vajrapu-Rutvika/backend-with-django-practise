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

class AdvancedMiddleware:
    def __init__(self,get_responce):
        self.get_responce = get_responce

    def __call__(self,request):
        return self.get_responce(request)
    def process_view(self,request,view_func,view_args,view_kwargs):
        print(f"process_view called for {view_func.__name__}")

    def process_exception(self,request,exception):
        print(f"process_exception called with exception: {exception}")
    def process_template_response(self,request,response):
        print("process_template_response called")
        return response            

class FirstMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        

    def __call__(self,request):
        print("First Middleware before view")
        response = self.get_response(request)
        print("First Middleware after view")
        return response

class SecondMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        print("Second Middleware before view")
        response = self.get_response(request)
        print("Second Middleware after view")
        return response
             