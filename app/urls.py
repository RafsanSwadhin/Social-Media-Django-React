from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import get_user_profile_data

urlpatterns = [
    path('user_data/<str:pk>/', get_user_profile_data, name='user-profile'),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
