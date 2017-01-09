
from django.http import HttpResponseRedirect,HttpResponse
from django.db import transaction
import random
from django.template.response import TemplateResponse
import requests
from django.core.exceptions import ObjectDoesNotExist
from registeration.models import registeration,activatekey
from user_profile.models import user_profile
from wall_of_fame.models import skill_karma_details
from django.core.mail import send_mail
html =""
activeurl=""
def register(request):
    global activeurl
    fname=request.POST.get('fname','')
    lname=request.POST.get('lname','')
    uid=request.POST.get('uid','')
    eid=request.POST.get('eid','')
    pwd=request.POST.get('pwd','')
    pnum=request.POST.get('pnum','')
    gender=request.POST.get('optradio','')
    dob=request.POST.get('dob','')
    str1=eid[0:3]+uid[1:3]+pnum[2:6]

    try:
        data=registeration.objects.get(eid=eid)
        request.session['checkemail']='Email already registered'
    except ObjectDoesNotExist:
        data=None

    if data == None:    
        try: 
            data=registeration.objects.get(uid=uid)
            request.session['checkuser']="Username already present"
        except ObjectDoesNotExist:
            data=None
            #isdata2=False

    if data == None:
        reg_obj=registeration(f_name=fname,l_name=lname,uid=uid,pwd=pwd,cnum=pnum,isactivate='no',spuser='no',gender=gender,dob=dob,pid=uid+pnum[-2:],eid=eid)
        reg_obj.save()
        key_obj=activatekey(pid=uid+pnum[-2:],active_key=str1)
        key_obj.save()
        user_obj=user_profile(f_name=fname,l_name=lname,pid=uid+pnum[-2:],image="images/images.jpg")
        user_obj.save()
        str2=[str(ord(c)+100) for c in str1]
        rand=random.randrange(10,86)
        rand2=random.randrange(1,9)
        for i in range(len(str2)):
            str2[i]=str(int(str2[i])+rand*rand2)
        str2.append(rand)
        str2.append(rand2)
        cyphered=''.join(map(str, str2))
        activeurl="http://"+(requests.get('https://api.ipify.org')).text+":8000/register/activated?user="+cyphered
        send_mail('Activation Link', activeurl, 'collegize.com',
            [eid], fail_silently=False)
    
    transaction.on_commit(foo)

    return HttpResponseRedirect(html)

  #  
def foo():
    global html
    html = '/'#"<html><body>"+activeurl+"</body></html>"   


def activated(request):
    key=request.GET.get('user','')  
    v_k1=key[-1:]
    v_k2=key[-3:-1]
    main_key=key[:-3]
    index=0
    ind=0
    data=None
    flag=1
    t=""
    user=""
    strli=[]
    while (ind < len(main_key)/3 ):
        strli.append(main_key[index:index+3])
        strli[ind]=chr((int(strli[ind])-int(v_k1)*int(v_k2))-100)
        uid=''.join(strli)
        index=index+3
        ind=ind+1
    try:
        data=activatekey.objects.get(active_key=uid)
        user=data.pid
    except ObjectDoesNotExist:
       	data=None
        request.session['status']="Your account is already activated"
   
    if data !=None:
        try:
            t="yo"
            data.delete()
            data=registeration.objects.get(pid=user)
            data.isactivate="yes"
            data2=skill_karma_details(pid=user,skill="0",karma="0",total="0",name=data.f_name+" "+data.l_name,spuser='no',image="images/images.jpg")
            data.save()
            data2.save()
        except ObjectDoesNotExist:
            flag=0

    if flag !=0:
    	request.session['status']="Your acount has been activated"
    return HttpResponseRedirect('/')


