from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.db import transaction
import time
from wall_of_fame.models import skill_karma_details
from wall_of_fame.views import skillpoint,karmapoint
from workshop.models import workshop_detail,subscriber,workshop_videos,workshoplike
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.cache import cache_control
from django.template.response import TemplateResponse

def main_page(request):
    uid=request.session.get('pid','')
    if uid== '':
        return HttpResponseRedirect("/")
    else:
        data2=subscriber.objects.filter(pid=uid)[:4]
        data=workshop_detail.objects.filter(pid=uid)[:4]
        data3=skill_karma_details.objects.get(pid=request.session.get('pid',''))
        return TemplateResponse(request,"workshop_main_list.html",{"name":request.session.get('name','noob'),"data":data,"data2":data2,"data3":data3})

def started(request):
    uid=request.session.get('pid','')
    if uid== '':
        return HttpResponseRedirect("/")
    else:
        data=workshop_detail.objects.filter(pid=uid)
        data3=skill_karma_details.objects.get(pid=request.session.get('pid',''))
        return TemplateResponse(request,"workshop_started_list.html",{"name":request.session.get('name','noob'),"data":data,"data3":data3})

def joined(request):
    uid=request.session.get('pid','')
    if uid== '':
        return HttpResponseRedirect("/")
    else:
        data=subscriber.objects.filter(pid=uid)
        data3=skill_karma_details.objects.get(pid=request.session.get('pid',''))
        return TemplateResponse(request,"workshop_joined_list.html",{"name":request.session.get('name','noob'),"data":data,"data3":data3})

def online(request):
    uid=request.session.get('pid','')
    if uid== '':
        return HttpResponseRedirect("/")
    else:
        data=workshop_detail.objects.all().exclude(pid=uid).order_by('id')
        data3=skill_karma_details.objects.get(pid=request.session.get('pid',''))
        return TemplateResponse(request,"workshop_allreadystarted_list.html",{"name":request.session.get('name','noob'),"data":data,"data3":data3})

def show_detail(request):
    uid=request.session.get('pid','')
    disable=""
    disable2=""
    if uid== '':
        return HttpResponseRedirect("/")
    else:
        wid=request.GET.get('id','')
        data=workshop_detail.objects.get(id=wid)
        vid=workshop_videos.objects.filter(workshop_id=wid)
        data3=skill_karma_details.objects.get(pid=request.session.get('pid',''))
        try:
            data2=subscriber.objects.get(workshop_id=wid,pid=uid)
        except ObjectDoesNotExist:  
            disable="no"
        try:
            data4=workshoplike.objects.get(workshop_id=wid,pid=uid)
        except ObjectDoesNotExist:  
            disable2="no"
        return TemplateResponse(request,"workshop.html",{"name":request.session.get('name','noob'),"data":data,"data3":data3,"vid":vid,"disable":disable,"disable2":disable2})

def manage(request):
    uid=request.session.get('pid','')
    if uid== '':
        return HttpResponseRedirect("/")
    else:
        wid=request.GET.get('id','')
        data=workshop_detail.objects.get(id=wid)
        vid=workshop_videos.objects.filter(workshop_id=wid)
        data3=skill_karma_details.objects.get(pid=request.session.get('pid',''))
        return TemplateResponse(request,"editworkshop.html",{"name":request.session.get('name','noob'),"data":data,"data3":data3,"vid":vid})


def strtwork(request):
    uid=request.session.get('pid','')
    if uid== '':
        return HttpResponseRedirect("/")
    else:
        wid=request.POST.get('id','')
        title=request.POST.get('title','')
        workshoptitle=request.POST.get('workshoptitle','')
        workdetail=request.POST.get('workdetail','')
        worknotice=request.POST.get('worknotice','')
        getvideo=request.FILES.get('video','')
        getimage=request.FILES.get('image','')
        gettype=request.POST.get('type','')
        data3=skill_karma_details.objects.get(pid=request.session.get('pid',''))
        if gettype == "update":
            data=workshop_detail.objects.get(id=wid)
            if workshoptitle !='':
                data.workshop_title=workshoptitle
                subscriber.objects.filter(workshop_id=wid).update(workshop_title=workshoptitle)
            if workdetail != '':
                data.workshop_details=workdetail
            if worknotice !='':
                data.note=worknotice
            if getvideo != '':
                vid=workshop_videos(up_date=time.strftime('%d-%m-%Y'),workshop_id=wid,video=getvideo,vid_title=title)
                data.videos_num=str(int(data.videos_num)+1)
                subscriber.objects.filter(workshop_id=wid).update(videos_num=data.videos_num)
                vid.save()
                skillpoint(uid,1)
            if getimage != '':   
                subscriber.objects.filter(workshop_id=wid).update(images=getimage)
                data.images=getimage
            data.save()
            vid=workshop_videos.objects.filter(workshop_id=wid)
            return HttpResponseRedirect('/workshop/manage_workshop?id='+wid)#return HttpResponse("updated")
        else:
            if getimage == '':
                getimage="images/images.jpg"
            data2=workshop_detail(pid=uid,workshop_title=workshoptitle,workshop_details=workdetail,ratings="0",videos_num="0",subscriber_num="0",note=worknotice,date=time.strftime('%d-%m-%Y'),images=getimage)
            data2.save()
            getid=workshop_detail.objects.filter(pid=uid).order_by('-id')[0]
            if getvideo != '':
                vid2=workshop_videos(up_date=time.strftime('%d-%m-%Y'),workshop_id=getid.id,video=getvideo,vid_title=title)
                workshop_detail.objects.filter(id=getid.id).update(videos_num="1")
                vid2.save()
                skillpoint(uid,1)
            data=workshop_detail.objects.filter(pid=uid)
            return HttpResponseRedirect('/workshop/startedwork/')
            #return HttpResponse("started")

def newworkshop(request):
    uid=request.session.get('pid','')
    if uid== '':
        return HttpResponseRedirect("/")
    else:
        data3=skill_karma_details.objects.get(pid=request.session.get('pid',''))
        return TemplateResponse(request,"new_workshop.html",{"name":request.session.get('name','noob'),"data3":data3})

def joinwork(request):
    uid=request.session.get('pid','')
    if uid== '':
        return HttpResponseRedirect("/")
    else:
        strg=""
        wid=request.GET.get("id",'')
        try:
            data2=subscriber.objects.get(workshop_id=wid,pid=uid)
        except ObjectDoesNotExist:    
            data=workshop_detail.objects.get(id=wid)
            data.subscriber_num=str(int(data.subscriber_num)+1)
            strg=data.subscriber_num
            data.save()
            data2=subscriber(pid=uid,workshop_id=wid,date=data.date,workshop_title=data.workshop_title,videos_num=data.videos_num,subscriber_num=data.subscriber_num,ratings=data.ratings,images=data.images)
            data2.save()
            subscriber.objects.filter(workshop_id=wid).update(subscriber_num=data.subscriber_num)
            karmapoint(data.pid,3)
        return HttpResponse(strg)


def likework(request):
    uid=request.session.get('pid','')
    if uid== '':
        return HttpResponseRedirect("/")
    else:
        strg=""
        wid=request.GET.get("id",'')
        try:
            data2=workshoplike.objects.get(workshop_id=wid,pid=uid)
        except ObjectDoesNotExist:    
            data=workshop_detail.objects.get(id=wid)
            data.ratings=str(int(data.ratings)+1)
            strg=data.ratings
            data.save()
            data2=workshoplike(pid=uid,workshop_id=wid)
            data2.save()
            subscriber.objects.filter(workshop_id=wid).update(ratings=data.ratings)
            skillpoint(data.pid,2)
        return HttpResponse(strg)