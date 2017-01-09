from django.conf.urls import url
urlpatterns = [
   url(r'^main_page', 'project.views.main_page', name='main_page'),
   #url(r'^uploadvideo/','workshop.views.upload_vid',name='upload_vid'),
   url(r'^start_project/','project.views.strtproject',name='strtproject'),
   #url(r'^updateimage/','workshop.views.img',name='img'),
   url(r'^joinedproject/','project.views.joined',name='joined'),
   url(r'^startedproject/','project.views.started',name='started'),
   url(r'^onlineproject/','project.views.online',name='online'),
   url(r'^showdetail','project.views.show_detail',name='show_detail'),
   url(r'^manage_project','project.views.manage',name='manage'),
   url(r'^startnew/','project.views.newproject',name='newproject'),
   url(r'^join','project.views.joinproject',name='joinproject'),
   url(r'^like','project.views.likeproject',name='likeproject'),
]