from django.http import HttpResponse

from main.views.base.base_view import BaseView


class TestView(BaseView):
    def get(self, request):
        return HttpResponse("Hello World")
