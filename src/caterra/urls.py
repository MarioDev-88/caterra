import debug_toolbar

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from apps.users.views import login_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", login_view),
    path("usuarios/", include("apps.users.urls")),
    path("administracion/", include("apps.backoffice.urls")),
    path('tinymce/', include('tinymce.urls')),
    path("", include("apps.ecommerce.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
