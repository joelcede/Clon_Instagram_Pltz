from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from posts import views as posts_view
from users import  views as users_view

urlpatterns = [
	path('admin/', admin.site.urls),	
	path('',posts_view.list_pos, name='feed'),
	path('users/login/', users_view.login_view, name='login'),
	path('users/logout/', users_view.logout_view, name='logout'),
	path('users/signup',users_view.signup, name='signup'),
	path('users/me/profile/',users_view.update_profile, name="update_profile"),
	path('posts/new/',posts_view.create_post, name='create_post')

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)