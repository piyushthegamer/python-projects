from django.conf.urls import url
urlpatterns = [
   url(r'^main_page/', 'events.views.events_main', name='events_main'),
   url(r'^submit', 'events.views.submit_event', name='submit_event'),
   url(r'^manage', 'events.views.display_events', name='display_events'),
   url(r'^sp_view_event', 'events.views.sp_event', name='sp_event'),
   url(r'^showdetail', 'events.views.viewevent', name='viewevent'),
   url(r'^join', 'events.views.joinevent', name='joinevent'),
   url(r'^showall', 'events.views.disp_events', name='disp_events'),
 #  url(r'^forgot/', 'login.views.forgot', name='forgot'),
 #  url(r'^verification/', 'login.views.verification', name='verification'),
  # url(r'^changepassword', 'login.views.changepassword', name='changepassword'),
 #  url(r'^passwordchanged/', 'login.views.password', name='password'),
]