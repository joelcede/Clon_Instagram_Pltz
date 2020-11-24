from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from posts import views as posts_view
from django.conf.urls.static import static

urlpatterns = [
	path('admin/', admin.site.urls),	
	path('posts/',posts_view.list_pos),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)