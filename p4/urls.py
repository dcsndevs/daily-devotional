from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('account/', include('account.urls')),
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('bible/', include("bible.urls"), name='bible-urls'),
    path('events/', include('events.urls'), name='events-urls'),
    path('summernote/', include('django_summernote.urls')),
    path('profile/', include('membership.urls'), name='membership-urls'),
    path('', include('devotional.urls'), name='devotional-urls'),
    
]
