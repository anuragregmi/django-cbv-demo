from django.conf.urls import url

from main.views import TestView

urlpatterns = [
    url(r'^$', TestView.as_view())
]
