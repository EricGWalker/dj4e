from django.urls import path

from . import views

app_name = "hello"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("sessions/", views.SessionCounterView.as_view(), name="sessions"),
    path("cookies/", views.CookieCounterView.as_view(), name="cookies"),
]
