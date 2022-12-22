from django.urls import path

from tjheeringa_github_io.users.views import about_view, home_view

app_name = "users"
urlpatterns = [
    path("", home_view, name="home"),
    path("about", about_view, name="about"),
]
