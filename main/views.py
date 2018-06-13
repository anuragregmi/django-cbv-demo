from django.http import HttpResponse

class BaseView:
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']

    def as_view(*args, **kwargs):
        return lambda x: HttpResponse("HelloWorld")

class TestView(BaseView):
    pass
