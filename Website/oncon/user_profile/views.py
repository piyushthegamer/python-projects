from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.db import transaction
from user_profile.models import user_profile
from registeration.models import registeration
from wall_of_fame.models import skill_karma_details
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.cache import cache_control
from django.template.response import TemplateResponse

@cache_control(no_cache=True, must_revalidate=True, no_store=True)

def profile_main(request):
    uid=request.session.get('pid','')
    if uid== '':
        return HttpResponseRedirect("/")
    else:
        data=registeration.objects.get(pid=uid)
        data2=user_profile.objects.get(pid=uid)
        data2.f_name=data.f_name
        data2.l_name=data.l_name
        data2.save()
        data3=skill_karma_details.objects.get(pid=uid)
        return TemplateResponse(request,'profile.html',{"name":request.session.get('name','noob'),"fname":data2.f_name,"lname":data2.l_name,"address":data2.address,"city":data2.city,"state":data2.state,"pin":data2.pin,"country":data2.country,"college":data2.college,"biography":data2.biography,"skills":data2.skills,"tenth":data2.tenthth_marks,"twelth":data2.twelth_marks,"course":data2.course,"data3":data3})

def account(request):
    uid=request.session.get('pid','')
    try:
        data=user_profile.objects.get(pid=uid)
    except user_profile.DoesNotExist:
        if uid =='':
            return HttpResponse("yo")
        else:
            return HttpResponse(uid)

    if request.GET.get('address','empty')!='empty':
        address=request.GET.get('address','')
        data.address=address
        data.save()
        return HttpResponse(address)
    elif request.GET.get('city','empty')!='empty':
        city=request.GET.get('city','')
        data.city=city
        data.save()
        return HttpResponse(city)
    elif request.GET.get('state','empty')!='empty':
        state=request.GET.get('state','')
        data.state=state
        data.save()
        return HttpResponse(state)
    elif request.GET.get('pin','empty')!='empty':
        pin=request.GET.get('pin','')
        data.pin=pin
        data.save()
        return HttpResponse(pin)
    elif request.GET.get('country','empty')!='empty':
        country=request.GET.get('country','')
        data.country=country
        data.save()
        return HttpResponse(country)

def profile(request):
    uid=request.session.get('pid','')
    try:
        data=user_profile.objects.get(pid=uid)
    except user_profile.DoesNotExist:
        if uid =='':
            return HttpResponse("yo")
        else:
            return HttpResponse(uid)

    if request.GET.get('college','empty')!='empty':
        college=request.GET.get('college','')
        data.college=college
        data.save()
        return HttpResponse(college)
    elif request.GET.get('biography','empty')!='empty':
        biography=request.GET.get('biography','')
        data.biography=biography
        data.save()
        return HttpResponse(biography)
    elif request.GET.get('skills','empty')!='empty':
        skills=request.GET.get('skills','')
        data.skills=skills
        data.save()
        return HttpResponse(skills)
    elif request.GET.get('tenth','empty')!='empty':
        tenth=request.GET.get('tenth','')
        data.tenthth_marks=tenth
        data.save()
        return HttpResponse(tenth)
    elif request.GET.get('twelth','empty')!='empty':
        twelth=request.GET.get('twelth','')
        data.twelth_marks=twelth
        data.save()
        return HttpResponse(twelth)
    elif request.GET.get('course','empty')!='empty':
        course=request.GET.get('course','')
        data.course=course
        data.save()
        return HttpResponse(course)

def upload(request):
    uid=request.session.get('pid','')
    if uid== '':
        return HttpResponseRedirect("/")
    else:
        getimage=request.FILES.get('image','')
        data2=user_profile.objects.get(pid=uid)
        data3=skill_karma_details.objects.get(pid=uid)
        data2.image=getimage
        data3.image="images/"+getimage.name
        data2.save()
        data3.save()
        return HttpResponseRedirect("/user_profile/main_page")
