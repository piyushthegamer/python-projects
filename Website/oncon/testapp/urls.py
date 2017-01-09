from django.conf.urls import url
urlpatterns = [
   url(r'^main_page', 'testapp.views.test_main', name='test_main'),
   url(r'^imageview/','testapp.views.images',name='images'),
   url(r'^videoview/','testapp.views.videos',name='videos'),
   url(r'^upload/','testapp.views.upload',name='upload'),
 #  url(r'^logout/', 'login.views.logout', name='logout'),
 #  url(r'^forgot/', 'login.views.forgot', name='forgot'),
 #  url(r'^verification/', 'login.views.verification', name='verification'),
  # url(r'^changepassword', 'login.views.changepassword', name='changepassword'),
 #  url(r'^passwordchanged/', 'login.views.password', name='password'),
]