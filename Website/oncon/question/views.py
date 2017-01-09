from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.db import transaction
import time
from question.models import question,answers,answer_comments,question_comments,questionlike,answerlike
from wall_of_fame.models import skill_karma_details
from user_profile.models import user_profile
from wall_of_fame.views import skillpoint,karmapoint
from registeration.models import registeration
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.cache import cache_control
from django.template.response import TemplateResponse

@cache_control(no_cache=True, must_revalidate=True, no_store=True)

def question_main(request):
    uid=request.session.get('pid','')
    if uid== '':
        return HttpResponseRedirect("/")
    else:
        data2=[]
        data3=[]
        data4=[]
        data5=[]
        data6=[]
        blah=""
        data=question.objects.filter(pid=uid).values_list('id')
        data1=list(sum(data, ()))
        for q_id in data1:
            try:
                query_obj=answers.objects.filter(question_id=q_id).order_by('-answer_num')[0]
            except  IndexError:
                query_obj=None
            if query_obj != None:
                data2.append(query_obj.answer_num)
                data3.append(query_obj.date)
                query_obj=question.objects.get(id=q_id)
                data4.append(query_obj.vote)
                data5.append(query_obj.date)
                data6.append(query_obj.question_head)
            else:
                data2.append("No Reply Yet")
                data3.append("---")
                query_obj=question.objects.get(id=q_id)
                data4.append(query_obj.vote)
                data5.append(query_obj.date)
                data6.append(query_obj.question_head)

        data7=question.objects.exclude(pid=uid).values_list('question_head', 'id')[:20]
        data8=skill_karma_details.objects.get(pid=uid)
        tup=map(lambda a,b,c,d,e,f:(a,b,c,d,e,f),data1,data2,data3,data4,data5,data6)
    #return HttpResponse(tup)
    return TemplateResponse(request,"post_a_que.html",{"name":request.session.get('name','noob'),"tup":tup,"data":data7,"data2":data8})

def ask_question(request):
    uid=request.session.get('pid','')
    if uid== '':
        return HttpResponseRedirect("/")
    else:
        question_head=request.GET.get('question_head','')
        question_detail=request.GET.get('detail','')
        tag=request.POST.get('tag','')
        data=question.objects.all().last()
        try:
            qid=str(int(data.id)+1)
        except AttributeError:
            qid="0"
        data=question(id=qid,pid=uid,question_head=question_head,question_detail=question_detail,vote="0",date=time.strftime('%d-%m-%Y'))
        data.save()

    return HttpResponseRedirect("/question/main_page/")

def comments(request):
    uid=request.session.get('pid','')
    if uid== '':
        return HttpResponseRedirect("/")
    else:
        question_comment=request.GET.get('que_comment','')
        answer_comment=request.GET.get('ans_comment','')
        if question_comment != '':
            question_id=request.GET.get('question_id','')
            commentid=question_comments.objects.all().last()
            try:
                qid=str(int(commentid.id)+1)
            except AttributeError:
                qid="0"
            data=question.objects.get(id=question_id)
            #return HttpResponse(data.pid+question_comments+question_id+time.strftime('%d-%m-%Y')+uid)
            data2=question_comments(id=qid,pid=data.pid,comment=question_comment,question_id=question_id,date=time.strftime('%d-%m-%Y'),cpid=uid)
            data2.save()
        else:
            answer_id=request.GET.get('answer_id','')
            question_id=request.GET.get('question_id','')
            commentid=answer_comments.objects.all().last()
            try:
                qid=str(int(commentid.id)+1)
            except AttributeError:
                qid="0"
            data=answers.objects.get(question_id=question_id,answer_num=answer_id)
            sk_obj=skill_karma_details.objects.get(pid=uid)
            data2=answer_comments(id=qid,pid=data.pid,answer_id=answer_id,image=sk_obj.image,skid=str(sk_obj.id),comment=answer_comment,question_id=question_id,date=time.strftime('%d-%m-%Y'),cpid=uid)
            data2.save()
    return HttpResponseRedirect("/question/detailquestion?id="+question_id)

def answer(request):
    uid=request.session.get('pid','')
    if uid== '':
        return HttpResponseRedirect("/")
    else:
        sameuser="yes"
        sameuser2=[]
        useridis=[]
        userimage=[]
        commentlist=[]
        datelist=[]
        skidlist=[]
        imagelist=[]
        votelist=[]
        answerlist=[]
        answernumlist=[]
        data3 = None
        commentdata=None
        like_query=None
        question_id=request.GET.get('id','')
        data=question.objects.get(id=question_id)
        data2=answers.objects.filter(question_id=question_id).order_by('id')
        data3=question_comments.objects.filter(question_id=question_id)
        data4=answer_comments.objects.filter(question_id=question_id)
        data5=question.objects.exclude(pid=uid).values_list('question_head', 'id')[:20]
        data6=skill_karma_details.objects.get(pid=uid)
        data7=user_profile.objects.get(pid=data.pid)
        image=data7.image
        data8=skill_karma_details.objects.get(pid=data.pid)
        userid=data8.id
        username=data8.name
        if data3 != None:
            for userdata in data3:
                commentlist.append(userdata.comment)
                datelist.append(userdata.date)
                comdata=skill_karma_details.objects.get(pid=userdata.cpid)
                useridis.append(comdata.id)
                userimage.append(comdata.image)
            commentdata=map(lambda a,b,c,d:(a,b,c,d),commentlist,useridis,userimage,datelist)
        datelist=[]
        if data.pid != uid:
            try:
                like_query=questionlike.objects.get(question_id=question_id,pid=uid)
                if like_query.id != None:
                    sameuser="yes"
            except ObjectDoesNotExist:
                sameuser="no"
        for answer in data2:
            skidlist.append(answer.skid)
            imagelist.append(answer.image)
            votelist.append(answer.vote)
            answerlist.append(answer.answer)
            datelist.append(answer.date)
            answernumlist.append(answer.answer_num)
            if answer.cpid != uid:
                try:
                    alike_query=answerlike.objects.get(question_id=data.id,answer_num=answer.answer_num,pid=uid)
                except ObjectDoesNotExist:
                    alike_query=None       
                if alike_query == None:
                    sameuser2.append("no")
                else:
                    sameuser2.append("yes")
            else:
                sameuser2.append("yes")    
        tup2=map(lambda a,b,c,d,e,f,g:(a,b,c,d,e,f,g),skidlist,imagelist,votelist,answerlist,datelist,answernumlist,sameuser2)
    #return HttpResponse(tup2)
    return TemplateResponse(request,"questions.html",{"name":request.session.get('name','noob'),"data":data,"data2":tup2,"data3":commentdata,"data4":data4,"data5":data5,"data6":data6,"sameuser":sameuser,"userid":userid,"image":image,"username":username})

def addanswer(request):
    uid=request.session.get('pid','')
    if uid== '':
        return HttpResponseRedirect("/")
    else:
        ans_query=None
        answer=request.GET.get('answer','')
        que_id=request.GET.get('question_id','')
        data=answers.objects.all().last()
        try:
            qid=str(int(data.id)+1)
        except AttributeError:
            qid="0"
        data=question.objects.get(id=que_id)
        sk_obj=skill_karma_details.objects.get(pid=uid)
        try:
            ans_query=answers.objects.filter(question_id=que_id).order_by('-answer_num')[0]
        except IndexError:
            ans_query= None
        if ans_query != None:
            count=str(int(ans_query.answer_num)+1)
        else:
            count='1'
        data2=answers(id=qid,pid=data.pid,answer=answer,image=sk_obj.image,skid=str(sk_obj.id),answer_num=count,question_id=que_id,vote="0",date=time.strftime('%d-%m-%Y'),cpid=uid)
        data2.save()
        karmapoint(uid,2)
    return HttpResponseRedirect("/question/detailquestion?id="+que_id)

def questionvoting(request):
    uid=request.session.get('pid','')
    if uid== '':
        return HttpResponseRedirect("/")
    else:
        que_id=request.GET.get('id','')
        vtype=request.GET.get('votetype','')
        data=question.objects.get(id=que_id)
        if vtype == 'up':
            data.vote=str(int(data.vote)+1)
            skillpoint(data.pid,1)
        else:
            data.vote=str(int(data.vote)-1)
        data.save()
        data2=questionlike(pid=uid,question_id=que_id)
        data2.save()
    return HttpResponse(data.vote)

def answerupvoting(request):
    uid=request.session.get('pid','')
    if uid== '':
        return HttpResponseRedirect("/")
    else:
        qid=request.POST.get('question_id','')
        anum=request.POST.get('answernum','')
        try:
            alike_query=answerlike.objects.get(question_id=qid,answer_num=anum,pid=uid)
        except ObjectDoesNotExist:
            alike_query=answerlike(pid=uid,question_id=qid,answer_num=anum)
            ans_obj=answers.objects.get(question_id=qid,answer_num=anum)
            ans_obj.vote=str(int(ans_obj.vote)+1)
            ans_obj.save()
            alike_query.save()
            karmapoint(uid,1)
            alike_query=answerlike.objects.get(question_id=qid,answer_num=anum,pid=uid)
    return HttpResponseRedirect("/question/detailquestion?id="+qid)

def answerdownvoting(request):
    uid=request.session.get('pid','')
    if uid== '':
        return HttpResponseRedirect("/")
    else:
        qid=request.POST.get('question_id','')
        anum=request.POST.get('answernum','')
        try:
            alike_query=answerlike.objects.get(question_id=qid,answer_num=anum,pid=uid)
        except ObjectDoesNotExist:
            alike_query=answerlike(pid=uid,question_id=qid,answer_num=anum)
            ans_obj=answers.objects.get(question_id=qid,answer_num=anum)
            ans_obj.vote=str(int(ans_obj.vote)-1)
            ans_obj.save()
            alike_query.save()
            alike_query=answerlike.objects.get(question_id=qid,answer_num=anum,pid=uid)
    return HttpResponseRedirect("/question/detailquestion?id="+qid)