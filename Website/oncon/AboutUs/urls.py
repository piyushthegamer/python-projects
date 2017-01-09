from django.conf.urls import url
urlpatterns = [
   url(r'^aboutus/', 'AboutUs.views.about', name='about'),
   url(r'^splist/', 'AboutUs.views.speciallist', name='speciallist'),
]