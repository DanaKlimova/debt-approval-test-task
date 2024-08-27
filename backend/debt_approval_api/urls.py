from django.urls import path

from . import views

urlpatterns = [
    path("manufacturers/<int:contract_id>/", views.get_manufacturers, name="get_manufacturers"),
]
