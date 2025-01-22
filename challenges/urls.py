from django.urls import path

from . import views

urlpatterns = [
    # path("january", views.index),
    # path("february", views.feb)
    path("", views.index),
    path("<int:month>", views.month_challenge_by_number),
    path("<str:month>", views.month_challenge, name="month_challenge"),
]