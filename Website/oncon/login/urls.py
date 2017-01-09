from django.conf.urls import url
urlpatterns = [
   url(r'^login/', 'login.views.login', name='login'),
   url(r'^logout/', 'login.views.logout', name='logout'),
   url(r'^forgot/', 'login.views.forgot', name='forgot'),
   url(r'^verification/', 'login.views.verification', name='verification'),
   url(r'^changepassword', 'login.views.changepassword', name='changepassword'),
   url(r'^passwordchanged/', 'login.views.password', name='password'),
]