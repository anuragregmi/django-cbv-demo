from django.conf.urls import url

from main.views.demo import TestView

urlpatterns = [
    url(r'^$', TestView.as_view())
]
