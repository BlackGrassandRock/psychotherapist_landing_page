from django.contrib import admin
from django.urls import path, include
from index_page.views import index, pageNotFound, customError, customPermissionDenied


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path("__debug__/", include("debug_toolbar.urls")),
]

handler404 = pageNotFound
handler403 = customPermissionDenied
handler500 = customError
