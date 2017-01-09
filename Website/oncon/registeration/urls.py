from django.conf.urls import url
urlpatterns = [
   url(r'^notactivated/', 'registeration.views.register', name='register'),
   url(r'^activated', 'registeration.views.activated', name='activated'),
]