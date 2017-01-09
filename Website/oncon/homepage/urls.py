from django.conf.urls import url
urlpatterns = [
   url(r'^$', 'homepage.views.home', name='home'),
]