from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.db import transaction
import time
from wall_of_fame.models import skill_karma_details
from wall_of_fame.views import skillpoint,karmapoint
from project.models import project_info,projectsubs,projectlike
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.cache import cache_control
from django.template.response import TemplateResponse

def main_page(request):
    uid=request.session.get('pid','')
    if uid== '':
        return HttpResponseRedirect("/")
    else:
        data2=projectsubs.objects.filter(pid=uid)[:4]
        data=project_info.objects.filter(pid=uid)[:4]
        data3=skill_karma_details.objects.get(pid=request.session.get('pid',''))
        return TemplateResponse(request,"project_main_list.html",{"name":request.session.get('name','noob'),"data":data,"data2":data2,"data3":data3})

def started(request):
    uid=request.session.get('pid','')
    if uid== '':
        return HttpResponseRedirect("/")
    else:
        data=project_info.objects.filter(pid=uid)
        data3=skill_karma_details.objects.get(pid=request.session.get('pid',''))
        return TemplateResponse(request,"project_started_list.html",{"name":request.session.get('name','noob'),"data":data,"data3":data3})

def joined(request):
    uid=request.session.get('pid','')
    if uid== '':
        return HttpResponseRedirect("/")
    else:
        data=projectsubs.objects.filter(pid=uid)
        data3=skill_karma_details.objects.get(pid=request.session.get('pid',''))
        return TemplateResponse(request,"project_joined_list.html",{"name":request.session.get('name','noob'),"data":data,"data3":data3})

def online(request):
    uid=request.session.get('pid','')
    if uid== '':
        return HttpResponseRedirect("/")
    else:
        data=project_info.objects.all().exclude(pid=uid).exclude(status="completed").order_by('id')
        data3=skill_karma_details.objects.get(pid=request.session.get('pid',''))
        return TemplateResponse(request,"project_allreadystarted_list.html",{"name":request.session.get('name','noob'),"data":data,"data3":data3})

def show_detail(request):
    uid=request.session.get('pid','')
    disable=""
    disable2=""
    if uid== '':
        return HttpResponseRedirect("/")
    else:
        wid=request.GET.get('id','')
        data=project_info.objects.get(id=wid)
        data3=skill_karma_details.objects.get(pid=request.session.get('pid',''))
        try:
            data2=projectsubs.objects.get(proid=wid,pid=uid)
        except ObjectDoesNotExist:
            if data.members != "0":  
                disable="no"
        try:
            data4=projectlike.objects.get(proid=wid,pid=uid)
        except ObjectDoesNotExist:  
            disable2="no"
        memberslist=projectsubs.objects.filter(proid=wid)
        #return HttpResponse(memberslist.name)
        return TemplateResponse(request,"project.html",{"name":request.session.get('name','noob'),"data":data,"data3":data3,"disable":disable,"disable2":disable2,"memberslist":memberslist})

def manage(request):
    uid=request.session.get('pid','')
    if uid== '':
        return HttpResponseRedirect("/")
    else:
        wid=request.GET.get('id','')
        data=project_info.objects.get(id=wid)
        data3=skill_karma_details.objects.get(pid=request.session.get('pid',''))
        return TemplateResponse(request,"editproject.html",{"name":request.session.get('name','noob'),"data":data,"data3":data3})

def newproject(request):
    uid=request.session.get('pid','')
    if uid== '':
        return HttpResponseRedirect("/")
    else:
        data3=skill_karma_details.objects.get(pid=request.session.get('pid',''))
        return TemplateResponse(request,"new_project.html",{"name":request.session.get('name','noob'),"data3":data3})

def strtproject(request):
    uid=request.session.get('pid','')
    if uid== '':
        return HttpResponseRedirect("/")
    else:
        wid=request.POST.get('id','')
        projecttitle=request.POST.get('ptitle','')
        projecturl=request.POST.get('url','')
        projectdetail=request.POST.get('detail','')
        technology=request.POST.get('technology','')
        promembers=request.POST.get('members','')
        projectnote=request.POST.get('note','')
        synfile=request.FILES.get('synfile','')
        getvideo=request.FILES.get('video','')
        getimage=request.FILES.get('image','')
        gettype=request.POST.get('type','')
        data3=skill_karma_details.objects.get(pid=request.session.get('pid',''))
        if gettype == "update":
            data=project_info.objects.get(id=wid)
            if projecttitle !='':
                data.ptitle=projecttitle
                projectsubs.objects.filter(proid=wid).update(ptitle=projecttitle)
            if projectdetail != '':
                data.detail=projectdetail
            if technology != '':
                data.technology=technology
                projectsubs.objects.filter(proid=wid).update(technology=technology)
            if projectnote !='':
                data.note=projectnote
            if getvideo != '':
                data.video=getvideo
                data.videodate=time.strftime('%d-%m-%Y')
                projectsubs.objects.filter(proid=wid).update(status="completed")
                if data.status != "completed":
                    skillpoint(uid,10)
                data.status="completed"
            if synfile != '':
                data.synopsis=synfile
                data.synopfile=synfile.name
            if projecturl != '':
                data.url=projecturl
                projectsubs.objects.filter(proid=wid).update(status="completed")
                if data.status != "completed":
                    skillpoint(uid,10)
                data.status="completed"
            if getimage != '':   
                projectsubs.objects.filter(proid=wid).update(images=getimage)
                data.images=getimage
            data.save()
            return HttpResponseRedirect('/project/manage_project?id='+wid)
            #return HttpResponse(synfile)
        else:
            if getimage == '':
                getimage="images/images.jpg"
            if synfile == '':
                synfile = 'nosyn'
                filename= 'na'
            else:
                filename= synfile.name
            data2=project_info(pid=uid,ptitle=projecttitle,detail=projectdetail,synopfile=filename,synopsis=synfile,rating="0",technology=technology,status="ongoing",url="nourl",video="novid",videodate="na",members=promembers,note=projectnote,date=time.strftime('%d-%m-%Y'),images=getimage)
            data2.save()
            data=project_info.objects.filter(pid=uid)
            return HttpResponseRedirect('/project/startedproject/')
            #return HttpResponse("started")

def joinproject(request):
    uid=request.session.get('pid','')
    if uid== '':
        return HttpResponseRedirect("/")
    else:
        strg=""
        wid=request.GET.get("id",'')
        try:
            data2=projectsubs.objects.get(proid=wid,pid=uid)
        except ObjectDoesNotExist:    
            data=project_info.objects.get(id=wid)
            if data.members != "0":
                data.members=str(int(data.members)-1)
                strg=data.members
                data.save()
                data3=skill_karma_details.objects.get(pid=request.session.get('pid',''))
                data2=projectsubs(pid=uid,name=data3.name,skid=data3.id,proid=wid,date=data.date,ptitle=data.ptitle,technology=data.technology,status=data.status,members=data.members,rating=data.rating,images=data.images)
                data2.save()
                projectsubs.objects.filter(proid=wid).update(members=data.members)
                karmapoint(data.pid,5)
            else:
                strg="already filled :(" 
        return HttpResponse(strg)


def likeproject(request):
    uid=request.session.get('pid','')
    if uid== '':
        return HttpResponseRedirect("/")
    else:
        strg=""
        wid=request.GET.get("id",'')
        try:
            data2=projectlike.objects.get(proid=wid,pid=uid)
        except ObjectDoesNotExist:    
            data=project_info.objects.get(id=wid)
            #data3=projectsubs.objects.get(proid=wid)
            data.rating=str(int(data.rating)+1)
            strg=data.rating
            data.save()
            data2=projectlike(pid=uid,proid=wid)
            data2.save()
            projectsubs.objects.filter(proid=wid).update(rating=data.rating)
            skillpoint(data.pid,2)
        return HttpResponse(strg)

