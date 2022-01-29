from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from profiles_api import views


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
