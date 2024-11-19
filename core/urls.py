from django.contrib import admin
from django.urls import path, include

API_VERSION = "api/v1/"
urlpatterns = [
    path('admin/', admin.site.urls),
    path(f"{API_VERSION}", include('authentication.urls')),
    path(f"{API_VERSION}", include('product.urls'))
]
