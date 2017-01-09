from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views.decorators.cache import cache_control
from wall_of_fame.models import skill_karma_details
from workshop.models import subscriber
from question.models import question,answers
from project.models import projectsubs
from registeration.models import registeration
from events.models import event_detail
import time

@cache_control(no_cache=True, must_revalidate=True, no_store=True)

def home(request):
    data=registeration.objects.filter(spuser='no')
    if request.session.get('isLogged', False):
        if request.session.get('isspecial','') !='':
            return TemplateResponse(request,'new_event.html',{"name":request.session.get('name','noob')})
        else:
            data22=[]
            data33=[]
            data44=[]
            data55=[]
            data66=[]
            blah=""
            dataobj=None
            tup=()
            dataobj=question.objects.filter(pid=request.session.get('pid','')).order_by('-id').values_list('id')[:10]
            data11=list(sum(dataobj, ()))
            if dataobj != None:
                for q_id in data11:
                    try:
                        query_obj=answers.objects.filter(question_id=q_id).order_by('-answer_num')[0]
                    except  IndexError:
                        query_obj=None
                    if query_obj != None:
                        data22.append(query_obj.answer_num)
                        data33.append(query_obj.date)
                        query_obj=question.objects.get(id=q_id)
                        data44.append(query_obj.vote)
                        data55.append(query_obj.date)
                        data66.append(query_obj.question_head)
                    else:
                        data22.append("No Reply Yet")
                        data33.append("---")
                        query_obj=question.objects.get(id=q_id)
                        data44.append(query_obj.vote)
                        data55.append(query_obj.date)
                        data66.append(query_obj.question_head)
                tup=map(lambda a,b,c,d,e,f:(a,b,c,d,e,f),data11,data22,data33,data44,data55,data66)
            event_detail.objects.filter(date=time.strftime('%Y-%m-%d')).delete()
            data=event_detail.objects.values_list('id','date','start_time','venue','image')[:4]
            data2=skill_karma_details.objects.get(pid=request.session.get('pid',''))
            data3=subscriber.objects.filter(pid=request.session.get('pid',''))[:4]
            data4=projectsubs.objects.filter(pid=request.session.get('pid',''))[:4]
            return TemplateResponse(request,'home.html',{"name":request.session.get('name','noob'),"data":data,"data2":data2,"workshopdata":data3,"projectdata":data4,"tup":tup})
    elif request.session.get('status',True) == False:
        del request.session['status']
        data2=skill_karma_details.objects.filter(spuser='no').order_by('-total')[:5]
        return TemplateResponse(request,'index.html',{"data":'account not activated',"num":data.count(),"data2":data2})

    elif request.session.get('isLogged', True) == False:
        del request.session['isLogged']
        data2=skill_karma_details.objects.filter(spuser='no').order_by('-total')[:5] 
        return TemplateResponse(request,'index.html',{"data":'Wrong password or username',"num":data.count(),"data2":data2})

    elif request.session.get('logout', False) ==True:
        del request.session['logout'] 
        data2=skill_karma_details.objects.filter(spuser='no').order_by('-total')[:5] 
        return TemplateResponse(request,'index.html',{"num":data.count(),"data2":data2})

    elif request.session.get('pid','') != '':
        del request.session['pid']
        data2=skill_karma_details.objects.filter(spuser='no').order_by('-total')[:5] 
        return TemplateResponse(request,'index.html',{"data":'Password Changed',"num":data.count(),"data2":data2})

    else:
        checkuser=request.session.get('checkuser','')
        checkemail=request.session.get('checkemail','')
        status=request.session.get('status','')
        request.session['checkemail'] = ''
        request.session['checkuser'] = ''
        request.session['status'] = ''
        data2=skill_karma_details.objects.filter(spuser='no').order_by('-total')[:5]
        return TemplateResponse(request,'index.html',{"checkuser":checkuser,"checkemail":checkemail,"status":status,"num":data.count(),"data2":data2})	



# Create your views here.
