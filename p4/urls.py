from django.contrib import admin
from django.urls import path, include
from .views import handler404, handler505

urlpatterns = [
    path('', include('home.urls'), name='home-urls'),
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('bible/', include("bible.urls"), name='bible-urls'),
    path('devotional/', include('devotional.urls'), name='devotional-urls'),
    path('events/', include('events.urls'), name='events-urls'),
    path('message/', include('message.urls'), name='message-urls'),
    path('newuser/', include('newuser.urls'), name='newuser'),
    path('summernote/', include('django_summernote.urls')),
    path('profile/', include('membership.urls'), name='membership-urls'),
    
]

handler404 = 'p4.views.handler404'
handler500 = 'p4.views.handler500'