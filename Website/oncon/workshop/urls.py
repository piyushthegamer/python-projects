from django.conf.urls import url
urlpatterns = [
   url(r'^main_page', 'workshop.views.main_page', name='main_page'),
   #url(r'^uploadvideo/','workshop.views.upload_vid',name='upload_vid'),
   url(r'^start_workshop/','workshop.views.strtwork',name='strtwork'),
   #url(r'^updateimage/','workshop.views.img',name='img'),
   url(r'^joinedwork/','workshop.views.joined',name='joined'),
   url(r'^startedwork/','workshop.views.started',name='started'),
   url(r'^onlinework/','workshop.views.online',name='online'),
   url(r'^showdetail','workshop.views.show_detail',name='show_detail'),
   url(r'^manage_workshop','workshop.views.manage',name='manage'),
   url(r'^startnew/','workshop.views.newworkshop',name='newworkshop'),
   url(r'^join','workshop.views.joinwork',name='joinwork'),
   url(r'^like','workshop.views.likework',name='likework'),
]