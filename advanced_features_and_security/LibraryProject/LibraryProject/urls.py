# advanced_features_and_security/advanced_features_and_security/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView # For logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bookshelf.urls')), # Include bookshelf app urls
    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'), # Add a logout URL
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Ensure your MEDIA_URL and MEDIA_ROOT are configured in settings.py
