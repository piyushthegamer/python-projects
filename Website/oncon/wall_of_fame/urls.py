from django.conf.urls import url
urlpatterns = [
   url(r'^main_page', 'wall_of_fame.views.main_page', name='main_page'),
   url(r'^show_detail', 'wall_of_fame.views.user_detail', name='user_detail'),
]