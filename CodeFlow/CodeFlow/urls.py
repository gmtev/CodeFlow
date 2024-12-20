# from django.conf import settings
# from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('CodeFlow.common.urls')),

    path('accounts/', include('CodeFlow.accounts.urls')),
    path('content/', include('CodeFlow.content.urls')),
]

# if settings.DEBUG: not needed since cloudinary is implemented
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
