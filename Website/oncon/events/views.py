from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.db import transaction
import time
from events.models import event_detail,joined_event
from wall_of_fame.models import skill_karma_details
from registeration.models import registeration
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.cache import cache_control
from django.template.response import TemplateResponse

def events_main(request):
    uid=request.session.get('pid','')
    if uid== '':
        return HttpResponseRedirect("/")
    elif request.session.get('isspecial','') == True:
        return TemplateResponse(request,"new_event.html",{"name":request.session.get('name','noob')})

def submit_event(request):
    uid=request.session.get('pid','')
    if uid== '':
        return HttpResponseRedirect("/")
    else:
        ans_query=None
        title=request.POST.get('title','')
        detailed=request.POST.get('detailed','')
        date=request.POST.get('date','')
        start_time=request.POST.get('start_time','')
        end_time=request.POST.get('end_time','')
        notice=request.POST.get('note','')
        venue=request.POST.get('venue','')
        getimage=request.FILES.get('image','')
        img=request.POST.get('img','')
        gettype=request.POST.get('type','')
        
        if gettype != 'update':
            if getimage == '':
                getimage='images/images.jpg'
            events_query=event_detail(pid=uid,title=title,image=getimage,detail=detailed,date=date,attending="0",start_time=start_time,end_time=end_time,venue=venue,notice=notice)
            events_query.save()
        else:
            eid=request.POST.get('id','')
            events_query=event_detail.objects.get(id=eid)
            events_query.title=title
            events_query.detail=detailed
            events_query.notice=notice
            events_query.venue=venue
            if getimage == '':
                events_query.image=img
            else:
                events_query.image=getimage
            events_query.save()
    return HttpResponseRedirect("/events/manage")

def display_events(request):
    uid=request.session.get('pid','')
    if uid== '':
        return HttpResponseRedirect("/")
    else:
        data=event_detail.objects.filter(pid=uid)
        data2=registeration.objects.get(pid=uid)
        return TemplateResponse(request,"event_manage.html",{"data":data,"name":data2.f_name+" "+data2.l_name})

def disp_events(request):
    uid=request.session.get('pid','')
    if uid== '':
        return HttpResponseRedirect("/")
    else:
        data=event_detail.objects.all()
        data2=registeration.objects.get(pid=uid)
        data3=skill_karma_details.objects.get(pid=uid)
        return TemplateResponse(request,"event_list.html",{"data":data,"name":data2.f_name+" "+data2.l_name,"data3":data3})

def sp_event(request):
    uid=request.session.get('pid','')
    if uid== '':
        return HttpResponseRedirect("/")
    else:
        evid=request.GET.get("id",'')
        data=event_detail.objects.get(pid=uid,id=evid)
        data2=registeration.objects.get(pid=uid)
        return TemplateResponse(request,"eventview.html",{"data":data,"name":data2.f_name+" "+data2.l_name})

def viewevent(request):
    uid=request.session.get('pid','')
    if uid== '':
        return HttpResponseRedirect("/")
    else:
        disable="yes"
        evid=request.GET.get("id",'')
        data=event_detail.objects.get(id=evid)
        data3=skill_karma_details.objects.get(pid=uid)
        data2=registeration.objects.get(pid=uid)
        try:
            data3=joined_event.objects.get(pid=uid,event_id=evid)
        except ObjectDoesNotExist:
            disable="no"
        return TemplateResponse(request,"event.html",{"data":data,"name":data2.f_name+" "+data2.l_name,"disable":disable,"data3":data3})

def joinevent(request):
    uid=request.session.get('pid','')
    if uid== '':
        return HttpResponseRedirect("/")
    else:
        strg=""
        evid=request.GET.get("id",'')
        try:
            data2=joined_event.objects.get(pid=uid,event_id=evid)
        except ObjectDoesNotExist:    
            data=event_detail.objects.get(id=evid)
            data.attending=str(int(data.attending)+1)
            strg=data.attending
            data.save()
            data2=joined_event(pid=uid,event_id=evid)
            data2.save()
        return HttpResponse(strg)
# Create your views here.
