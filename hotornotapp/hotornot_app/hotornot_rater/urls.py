from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('signup/', views.signup, name='signup'),
	path('login/', views.login, name='login'),
	path('leaderboard/', views.leaderboard, name='leaderboard'),
	path('upload/', views.image_upload, name='upload'),
    path('success/', views.success, name = 'success'),
	path('photos/', views.photos, name = 'photos'),
]
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)