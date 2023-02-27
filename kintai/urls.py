from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('backup_database/', include('backup_database.urls')),
    path('', include('attendance.urls')),
    path('fix_request/', include('fix_request.urls')),
]
