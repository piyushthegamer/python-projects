from django.http import HttpResponseRedirect,HttpResponse
from django.db import transaction
from user_profile.models import user_profile
from registeration.models import registeration
from testapp.models import image,video
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.cache import cache_control
from django.template.response import TemplateResponse

@cache_control(no_cache=True, must_revalidate=True, no_store=True)

def test_main(request):
        return TemplateResponse(request,'testmain.html',{})

def upload(request):
    getimage=request.FILES.get('image','')
    data=video.objects.get(id=1)
    data.videostore=getimage
    data.save()
    return HttpResponse(getimage)

def images(request):
    data=image.objects.get(id=1)
    source=data.imagestore
    return TemplateResponse(request,'testimage.html',{"source":source})

def videos(request):
    data=video.objects.get(id=1)
    source=data.videostore
    return TemplateResponse(request,'testvideo.html',{"source":source})
