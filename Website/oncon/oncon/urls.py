"""oncon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', include('homepage.urls')),
    url(r'^register/',include('registeration.urls')),
    url(r'^login/',include('login.urls')),
    url(r'^user_profile/',include('user_profile.urls')),
    url(r'^question/',include('question.urls')),
    url(r'^events/',include('events.urls')),
    url(r'^wall_of_fame/',include('wall_of_fame.urls')),
    url(r'^workshop/',include('workshop.urls')),
    url(r'^testapp/',include('testapp.urls')),
    url(r'^project/',include('project.urls')),
    url(r'^AboutUs/',include('AboutUs.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)