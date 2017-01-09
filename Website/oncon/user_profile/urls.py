from django.conf.urls import url
urlpatterns = [
   url(r'^main_page', 'user_profile.views.profile_main', name='profile_main'),
   url(r'^account/update','user_profile.views.account',name='account'),
   url(r'^profile/update/','user_profile.views.profile',name='profile'),
   url(r'^profile/upload_image/','user_profile.views.upload',name='upload'),
 #  url(r'^logout/', 'login.views.logout', name='logout'),
 #  url(r'^forgot/', 'login.views.forgot', name='forgot'),
 #  url(r'^verification/', 'login.views.verification', name='verification'),
  # url(r'^changepassword', 'login.views.changepassword', name='changepassword'),
 #  url(r'^passwordchanged/', 'login.views.password', name='password'),
]