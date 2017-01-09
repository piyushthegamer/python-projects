from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.db import transaction
import time
from wall_of_fame.models import skill_karma_details
from registeration.models import registeration
from user_profile.models import user_profile
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.cache import cache_control
from django.template.response import TemplateResponse

def main_page(request):
    uid=request.session.get('pid','')
    if uid== '':
        return HttpResponseRedirect("/")
    else:
        data=skill_karma_details.objects.get(pid=uid)
        data.total=int(data.skill)+int(data.karma)
        data.save()
        data2=skill_karma_details.objects.filter(spuser='no').order_by('-total')
        return TemplateResponse(request,"wall.html",{"name":request.session.get('name','noob'),"data":data2,"data2":data})

def skillpoint(uid,skill):
    data=skill_karma_details.objects.get(pid=uid)
    data.total=int(data.skill)+int(data.karma)
    data.skill=str(int(data.skill)+skill)
    data.total=str(int(data.total)+skill)
    data.save()
    return None

def karmapoint(uid,karma):
    data=skill_karma_details.objects.get(pid=uid)
    data.total=int(data.skill)+int(data.karma)
    data.karma=str(int(data.karma)+karma)
    data.total=str(int(data.total)+karma)
    data.save()
    return None

def user_detail(request):
    uid=request.session.get('pid','')
    if uid== '':
        return HttpResponseRedirect("/")
    else:
        userid=request.GET.get('id','')
        data=skill_karma_details.objects.get(id=userid)
        data3=user_profile.objects.get(pid=data.pid)
        data4=user_profile.objects.get(pid=uid)
        #data2=registeration.objects.get(pid=data.pid)
        return TemplateResponse(request,"profile_others.html",{"name":request.session.get('name','noob'),"image":data4.image,"data":data,"data2":data3})


