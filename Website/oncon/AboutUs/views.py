from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.views.decorators.cache import cache_control
from wall_of_fame.models import skill_karma_details
from registeration.models import registeration

def about(request):
    data=registeration.objects.filter(spuser='no')
    if request.session.get('isLogged', False):
        data2=skill_karma_details.objects.get(pid=request.session.get('pid',''))
        return TemplateResponse(request,'loggedaboutus.html',{"name":request.session.get('name','noob'),"num":data.count(),"data2":data2})
    else:
        return TemplateResponse(request,'aboutus.html',{"num":data.count()})

def speciallist(request):
    data=registeration.objects.filter(spuser='yes')
    if request.session.get('isLogged', False):
        namelist=[]
        collegelist=[]
        data2=skill_karma_details.objects.get(pid=request.session.get('pid',''))
        for obj in data:
            namelist.append(obj.f_name+" "+obj.l_name)
            collegelist.append(obj.spcollege)
        tup=map(lambda a,b:(a,b),namelist,collegelist)
        return TemplateResponse(request,'specuserlist.html',{"name":request.session.get('name','noob'),"data":tup,"data2":data2})
    else:
        return HttpResponseRedirect('/')  

# Create your views here.
