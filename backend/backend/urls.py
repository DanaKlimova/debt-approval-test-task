from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("debt_approval_api/", include("debt_approval_api.urls")),
    path("admin/", admin.site.urls),
]
