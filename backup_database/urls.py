from django.urls import path
from .views import BackupDatabase, HomeView
 
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('backup', BackupDatabase.as_view(), name='backup'),
] 

