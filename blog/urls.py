from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


api_urlpatterns = [
    path('', include('apps.cars.api.urls')),
    path('', include('apps.posts.api.urls')),
    path('', include('apps.teams.api.urls')),
    path('', include('apps.users.api.urls')),
    
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.users.urls')),
    path("team/", include("apps.teams.urls")),
    path("cars/", include("apps.cars.urls")),
    path('api/', include(api_urlpatterns)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)