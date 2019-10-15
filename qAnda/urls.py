from django.conf.urls import url
from . import view

app_name = 'xxqg'

urlpatterns = [
    url(r'^$', view.index),
    url(r'index', view.search, name="search"),
]