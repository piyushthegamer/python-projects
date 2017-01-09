from django.conf.urls import url
urlpatterns = [
   url(r'^main_page/', 'question.views.question_main', name='question_main'),
  url(r'^submit', 'question.views.ask_question', name='ask_question'),
  url(r'^comments', 'question.views.comments', name='comments'),
  url(r'^detailquestion', 'question.views.answer', name='answer'),
  url(r'^addanswer', 'question.views.addanswer', name='addanswer'),
  url(r'^qvote', 'question.views.questionvoting', name='questionvoting'),
   url(r'^answerupvote/', 'question.views.answerupvoting', name='answerupvoting'),
    url(r'^answerupvote/', 'question.views.answerdownvoting', name='answerdownvoting'),
 #  url(r'^forgot/', 'login.views.forgot', name='forgot'),
 #  url(r'^verification/', 'login.views.verification', name='verification'),
  # url(r'^changepassword', 'login.views.changepassword', name='changepassword'),
 #  url(r'^passwordchanged/', 'login.views.password', name='password'),
]