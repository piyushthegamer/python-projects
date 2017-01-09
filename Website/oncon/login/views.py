from django.http import HttpResponseRedirect,HttpResponse
from django.db import transaction
from registeration.models import registeration
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.cache import cache_control
from django.template.response import TemplateResponse
from datetime import datetime
import random
import requests
from django.core.mail import send_mail
html=''

@cache_control(no_cache=True, must_revalidate=True, no_store=True)

def login(request):
    global html
    uid=request.POST.get('user_id','')
    pwd=request.POST.get('psswrd','')
    try:
        data=registeration.objects.get(uid=uid,pwd=pwd)
    except ObjectDoesNotExist:
        data=None
        html='/'
    transaction.on_commit(foo)
    if data!=None:  
        if data.isactivate == 'yes':
            request.session['isLogged']=True
            if "speceventuse" in uid:
                request.session['isspecial']=True
            request.session['name']=data.f_name+" "+data.l_name
            request.session['pid']=data.pid
        else:
        	request.session['status'] = False
    else:
    	request.session['isLogged']=False
    return HttpResponseRedirect(html)
    

def logout(request):
    request.session['isLogged']=None
    request.session['logout']=True
    if request.session.get('isspecial','')!='':
        del request.session['isspecial']
    del request.session['pid']    
    return HttpResponseRedirect('/')

def foo():
    global html
    html = '/'   

def forgot(request):   
    return TemplateResponse(request,'forgot.html',{"data":''})
# Create your views here.

def verification(request):
    eid=request.POST.get('mailid','')
    flag=1
    resp='Please check your mail'
    str1=''
    try:
        data=registeration.objects.get(eid=eid)
        str1=data.pid
    except ObjectDoesNotExist:
        resp='E-mail ID not found'
        flag=0    
    str2=[str(ord(c)+100) for c in str1]
    rand=random.randrange(10,86)
    rand2=random.randrange(1,9)
    for i in range(len(str2)):
        str2[i]=str(int(str2[i])+rand*rand2)
    str2.append(rand)
    str2.append(rand2)
    cyphered=''.join(map(str, str2))
    activeurl="http://"+(requests.get('https://api.ipify.org')).text+":8000/login/changepassword?user="+datetime.now().strftime('%Y%m%d%H%M')+cyphered
    send_mail('Activation Link', activeurl, 'collegize.com',[eid], fail_silently=False)
    return TemplateResponse(request,'forgot.html',{"data":resp})

def changepassword(request):
    key=request.GET.get('user','')
    gotdate=key[:12]
    v_k1=key[-1:]
    v_k2=key[-3:-1]
    dwk=key[12:]
    main_key=dwk[:-3]
    index=0
    ind=0
    data=None
    user=""
    strli=[]
    if int(datetime.now().strftime('%Y%m%d%H%M')) - int(gotdate) < 49:
        while (ind < len(main_key)/3 ):
            strli.append(main_key[index:index+3])
            strli[ind]=chr((int(strli[ind])-int(v_k1)*int(v_k2))-100)
            uid=''.join(strli)
            index=index+3
            ind=ind+1
        try:
            data=registeration.objects.get(pid=uid)
        except ObjectDoesNotExist:
            data=None
    
        if data !=None:
            request.session['pid']=uid
            return TemplateResponse(request,'newpass.html',{})
        else:
            return TemplateResponse(request,'forgot.html',{"data":'Some Error occured...Try Again'})
    else:
        return TemplateResponse(request,'forgot.html',{"data":'Please try again Link time out'})

def password(request):
    password=request.POST.get('pwd','')
    uid=request.session.get('pid','')
    data=None
    try:
        data=registeration.objects.get(pid=uid)
    except ObjectDoesNotExist:
        data=None

    if data!=None:
        data.pwd=password
        data.save()
        return HttpResponseRedirect('/') 

    else:
        HttpResponse('Oops Something went wrong')



