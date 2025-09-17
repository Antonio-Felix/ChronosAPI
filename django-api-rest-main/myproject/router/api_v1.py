from django.conf.urls import include
from django.urls import path

from myapp.api.v1.router import router

api_v1_urls = [
    path("", include((router.urls, "myapp"), namespace="myapp")),
] + router.urls
