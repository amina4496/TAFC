from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from models import *
#from lsss1 import *
from abeencrypt import *
import json
from django.core import serializers
from django.core.files.storage import FileSystemStorage
from ecc import *
from datetime import datetime
import random
import time
import matplotlib.pyplot as plt
from django.core.mail import EmailMessage
from bloomfilter import*
# Create your views here.
def __datetime(date_str):
    return datetime.strptime(date_str, '%d/%m/%Y %I:%M:%S')
al=[]
policy=[]
andl=[]
orl=[]
abcd=0
file_content=""
from abeencrypt import *
def home(request):
    return render(request,'signing.html',{})
def log(request):
    global abcd
    global andl
    global orl,file_content
    abcd=0
    andl=[]
    orl=[]
    file_content=""
    return render(request,'signing.html',{})
def signup(request):
    return render(request,'signup.html',{})
def ind(request):
    return render(request,'index.html',{})
def dq1(request):
    pk, msk = setup()
    ob1=keyvals(pkv=pk,msk=msk)
    ob1.save()
    return render(request,'dq.html',{})
def dq2(request):
    return render(request,'kgf.html',{})

def newadmin(request):
    return render(request,'newadminhome.html',{})

def vb(request):
    global abcd
    global andl
    global orl,file_content
    abcd=0
    andl=[]
    orl=[]
    file_content=""
    return render(request,'dataown.html',{})

def logval(request):
    try:
        name=request.POST.get("name")
        email=request.POST.get("email")
        cat=request.POST.get("category")
        dob=request.POST.get("dob")
        dep=request.POST.get("dep")
        rol=request.POST.get("rol")
        username=request.POST.get("username")
        password=request.POST.get("password")
        sid=request.POST.get("sid")
        tid=request.POST.get("tid")
        sem=request.POST.get("sem")
        if sem==None:
            sem=""
        if sid==None:
            sid=""
        if tid==None:
            tid=""
        if cat=="DATA OWNER":
            ob=stafc(name=name,email=email,cat=cat,dob=dob,dep=dep,role=rol,username=username,password=password,status=1,sid=sid,tid=tid,sem=sem)
            ob.save()
        else:
            ob=stafc(name=name,email=email,cat=cat,dob=dob,dep=dep,role=rol,username=username,password=password,status=2,sid=sid,tid=tid,sem=sem)
            ob.save()
        return HttpResponse("<script>alert('Registration Successfull');window.location.href='/log/'</script>")
    except:
        return HttpResponse("<script>alert('Registration Failed');window.location.href='/log/'</script>")

def data(request):
    noti=filedates.objects.raw("select * from App_filedates order by id desc limit 5;")
    fil=stafc.objects.get(username=request.session["user"])
    notification=[]
    for ty in noti:
        print(ty.access,fil.role)
        if fil.role in ty.access:
            notification.append(str(ty.username)+" uploaded under Role "+str(fil.role))

    return render(request,'data.html',{"noti":notification})

def sig(request):
    
    return render(request,'approvalhome.html',{})

def newnoti(request):
    return render(request,'princi.html',{})
def valu(request):
    return render(request,'signval.html',{})

def sendnotif(request):
    return render(request,"nextnot.html",{})
def princi(request):
    return render(request,'princi.html',{})

def notifyprinci(request):
    return render(request,'princinoti.html',{})
def sen(request):
##    ob = filedates.objects.raw("select * from App_filedates where approve=1;")
    ob=filedates.objects.raw("select * from App_filedates where approve=0;")
    
    return render(request,'send.html',{})

def newnotification(request):
    n=request.POST.get("noti")
    ob=nots(notif=n).save()
    return HttpResponse("<script>alert('Notification Send ');window.location.href='/newnoti/'</script>")
def newsen(request):
##    ob = filedates.objects.raw("select * from App_filedates where approve=1;")
    ob=filedates.objects.raw("select * from App_filedates where approve=0 order by id desc limit 3;")
    
    return render(request,'send.html',{})

def cloudpage(request):
    print request.session["user"]
    ab=""
    if request.session["user"]=="Admin":
        ab="Admin"
    else:
        ab=request.session["user"]
    return render(request,'cloudpage.html',{"zx":ab})

def inbpage(request):
    print request.session["user"]
    return render(request,'inboxpage.html',{"zx":request.session["user"]})

def loginval(request):
    usernamelog=request.POST.get("usernamelog")
    passwordlog=request.POST.get("passwordlog")
    xy="True"
    al.append(usernamelog)
    if usernamelog=="admin" and passwordlog=="admin":
        request.session["user"]="Admin"
        return HttpResponse("<script>alert('Welcome Admin');window.location.href='/newadmin/'</script>")
##        return render(request,'newadminhome.html',{})
    elif usernamelog=="principal" and passwordlog=="principal":
        request.session["user"]="principal"
        return HttpResponse("<script>alert('Welcome Pricipal');window.location.href='/newnoti/'</script>")
##        return render(request,'dataown.html',{})
    else:
        obj=stafc.objects.all()
        for i in obj:
            if i.username==usernamelog and i.password==passwordlog and i.status==1 and i.approve==1:
                request.session["user"]=usernamelog
                noti=filedates.objects.raw("select * from App_filedates order by id desc limit 5;")
                try:
                    fil=stafc.objects.get(username=request.session["user"])
                    notification=[]
                    for ty in noti:
                        print(ty.access,fil.role)
                        if fil.role in ty.access:
                            notification.append(str(ty.username)+" uploaded under Role "+str(fil.role))
                except:
                    notification=[]
                    for ty in noti:
                        print(ty.access,fil.role)
                        notification.append("Principal uploaded a file")
                nn=nots.objects.all()
                for i in nn:
                    notification.append(str("Principal notified "+str(i.notif)))
                return render(request,'dataown.html',{"noti":notification})
            elif i.username==usernamelog and i.password==passwordlog and i.status==2 and i.approve==1:
                request.session["user"]=usernamelog
                noti=filedates.objects.raw("select * from App_filedates order by id desc limit 5;")
                try:
                    fil=stafc.objects.get(username=request.session["user"])
                    notification=[]
                    for ty in noti:
                        print(ty.access,fil.role)
                        if fil.role in ty.access:
                            notification.append(str(ty.username)+" uploaded under Role "+str(fil.role))
                except:
                    notification=[]
                    for ty in noti:
                        print(ty.access,fil.role)
                        notification.append("Principal uploaded a file")
                nn=nots.objects.all()
                for i in nn:
                    notification.append(str("Principal notified "+str(i.notif)))
                return render(request,'others.html',{"noti":notification})
            else:
                xy="False"
    if xy=="False":
        return render(request,'signing.html',{})

def keys(request):
    pk, msk = setup()
    ob1=keyvals(pkv=pk,msk=msk)
    ob1.save()
    ob=keyvals.objects.all()
    data={}
    ob=serializers.serialize("json",ob)
    data["dt1"]=json.loads(ob)
    print data
    return JsonResponse(data,safe=False)
def selected(request):
    x=request.GET.get("d1")
    ob=role.objects.raw("select * from App_role where department='"+x+"'")
    data={}
    ob=serializers.serialize("json",ob)
    data["dt1"]=json.loads(ob)
    print data
    return JsonResponse(data,safe=False)

def empire(request):
    from datetime import datetime
    from datetime import timedelta
    d=datetime.today()+timedelta(days=2)
    dd=d.strftime("%d/%m/%Y")
    dt=d.strftime("%H:%M:%S")
    v=request.GET.get("d1");
    o1=keyvals.objects.all()
    ob=stafc.objects.raw("select * from App_stafc where role='"+v+"'")
    data={}
    o1=serializers.serialize("json",o1)
    ob=serializers.serialize("json",ob)
    data["dt1"]=json.loads(ob)
    data["dt2"]=json.loads(o1)
    data["dt3"]=dd
    data["dt4"]=dt
    print data
    return JsonResponse(data,safe=False)

def verify(request):
    ob=stafc.objects.raw("select * from App_stafc where approve=0;")
    data={}
    ob=serializers.serialize("json",ob)
    data["dt1"]=json.loads(ob)
    print data
    return JsonResponse(data,safe=False)

def sending1(request):
    ob = filedates.objects.raw("select * from App_filedates where approve=0;")
    data={}
    ob=serializers.serialize("json",ob)
    data["dt1"]=json.loads(ob)
    print data
    return JsonResponse(data,safe=False)

def newsending(request):
    ob=filedates.objects.raw("select * from App_filedates where approve=0 order by id desc limit 3;")
    data={}
    ob=serializers.serialize("json",ob)
    data["dt1"]=json.loads(ob)
    print data
    return JsonResponse(data,safe=False)


def sending(request):
    ob = filedates.objects.raw("select * from App_filedates where approve=1 order by id desc;")
    data={}
    ob=serializers.serialize("json",ob)
    data["dt1"]=json.loads(ob)
    print data
    return JsonResponse(data,safe=False)

##def times(request):
##    ob=time_date.objects.raw("select * from App_time_date")
##    data={}
##    ob=serializers.serialize("json",ob)
##    data["dt1"]=json.loads(ob)
##    print data
##    return JsonResponse(data,safe=False)

def encr(request):
    timeor=[]
    timeand=[]
    ostr=""
    astr=""
    for i in orl:
        a=request.POST.get(i)
        ostr+=str(i)+"$"
        timeor.append(str(a))
        ostr+=str(a)+"&"
    for i in andl:
        a=request.POST.get(i)
        astr+=str(i)+"$"
        timeand.append(str(a))
        astr+=str(a)+"&"
        
    print timeor
    print timeand
    obj = filedates.objects.last()
    obj.approve=1
    obj.save()
    fo=open("App/static/files/"+str(obj.filename),"rb")
    file_content=fo.read()
    fo.close()
    p,m=setup()
    
    s=enc(p,file_content,policy)
    priv,pub=gen_pubKey()
    C1,C2 = encryption(pub, Hash.encode(file_content))
    ob=timeuser(oruser=ostr,anduser=astr,fid=int(obj.id)).save()
    fo=open("App\\enc\\"+obj.filename,"wb")
    fo.write(str(C1)+"&&"+str(C2))
    fo.close()
    ob=forfile(fid=int(obj.id),filename=str(obj.filename),priv=str(priv)).save()
    
    return render(request,'d1con.html',{"zx":str(C1)+str(C2)})


def encrypting(request):
    x=request.GET.get("d1")
    #y=request.GET.get("d2")
    #z=request.GET.get("d3")
    obj=filedates.objects.get(id=int(x))
    fo=open("App/static/files/"+obj.filename,"rb")
    file_content=fo.read()
    fo.close()
    p,m=setup()
    pub,priv=gen_pubKey()
    C1,C2 = encryption(pub, Hash.encode(file_content))
    C3,C4 = encryption(pub, Hash.encode(obj.time))
    C5,C6 = encryption(pub, Hash.encode(obj.date))
    fo=open("App\\enc\\"+obj.filename,"wb")
    fo.write(str(C1)+"&&"+str(C2))
    fo.close()
    s1=enc(p,file_content,policy)
    s2=enc(p,obj.time,policy)
    s3=enc(p,obj.date,policy)
    s=str(C1)+"$"+str(C2)+"$"+str(C3)+"$"+str(C4)+"$"+str(C5)+"$"+str(C6)
    
    return JsonResponse(s,safe=False)

def askkey(request):
    x=request.GET.get("d1")
    y=request.GET.get("d2")
    print x,y
##    z=request.GET.get("d3")
    try:
        ob=stafc.objects.get(username=request.session["user"])
        ob=askey(uid=int(ob.id),username=request.session["user"],role=ob.role,fileid=int(x),filename=str(y))
        ob.save()
        body="Username "+request.session["user"]+" has requested for the file "+str(y)
        email = EmailMessage('Key Approval Notification', body, to=['aamina4496@gmail.com'])
        email.send()
        print("Mail Send Successfully")
        return HttpResponse('Request Send')
    except:
        return HttpResponse('Request not Send')
def approved(request):
    x=request.GET.get("d1")
    obj=stafc.objects.get(id=x)
    obj.approve=1
    obj.save()
    ob=stafc.objects.raw("select * from App_stafc where approve=0;")
    data={}
    ob=serializers.serialize("json",ob)
    data["dt1"]=json.loads(ob)
    print data
    return JsonResponse(data,safe=False)
def reqfile(request):
    ob=askey.objects.raw("select * from App_askey order by id desc limit 5")
    return render(request,'keyreq.html',{"data":ob})
################################33

def acceptusers(request):
    ob=accepted.objects.all()
    return render(request,'accepted.html',{"data":ob})

def rejectusers(request):
    ob=rejected.objects.all()
    return render(request,'rejected.html',{"data":ob})

def download(request):
    a=request.POST.get('id')
    c=request.POST.get('priv')
    obj=forfile.objects.get(fid=int(a))
    print a,c
    fo=open("App/enc/"+str(obj.filename),"rb")
    q=fo.read()
    fo.close()
    print q
    ob=okay.objects.get(fid=int(a),filename=str(obj.filename),username=request.session['user'])
    obj=forfile.objects.get(fid=int(a),filename=str(obj.filename))
    z=""
    print obj.priv
    for i in obj.priv:
        if i.isdigit():
            z+=i
    print z
    pr=long(z)##priv
    q=q.split('&&')
    d=q[0].split(',')
    d0=d[0]
    w=''
    for i in d0:
        if i.isdigit():
            w+=i
    d1=d[1]
    print w,z
    x=''
    for i in d1:
        if i.isdigit():
            x+=i
    w=long(w)
    x=long(x)
    C1=(w,x)
    print C1
    g=''
    for i in q[1]:
        if i.isdigit():
            g+=i      
    C2=long(g)
    print C2
    print type(C1),type(C2),type(pr)
    print pr
    decrypted_string = decryption(C1, C2, pr)
    s=Hash.decode(str(decrypted_string))
    print s
    filename = "my_file.txt"
    content = q
    response = HttpResponse(s, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
    return response


import os
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def newdownload(request):
    b=request.POST.get('id')
    c=request.POST.get('priv')
    print b,c
    obj=forfile.objects.get(fid=int(b))
    fo=open("App/enc/"+str(obj.filename),"rb")
    q=fo.read()
    fo.close()
    print q
    ob=okay.objects.get(fid=int(b),filename=str(obj.filename),username=request.session['user'])
    obj=forfile.objects.get(fid=int(b),filename=str(obj.filename))
    z=""
    print obj.priv
    for i in obj.priv:
        if i.isdigit():
            z+=i
    print z
    pr=long(z)##priv
    q=q.split('&&')
    d=q[0].split(',')
    d0=d[0]
    w=''
    for i in d0:
        if i.isdigit():
            w+=i
    d1=d[1]
    print w,z
    x=''
    for i in d1:
        if i.isdigit():
            x+=i
    w=long(w)
    x=long(x)
    C1=(w,x)
    print C1
    g=''
    for i in q[1]:
        if i.isdigit():
            g+=i      
    C2=long(g)
    print C2
    print type(C1),type(C2),type(pr)
    print pr
    decrypted_string = decryption(C1, C2, pr)
    s=Hash.decode(str(decrypted_string))
    print s
    fd=open("my_file.txt","w")
    fd.write(s)
    fd.close()
    print "File co,pletely readed"
    filename = "my_file.txt"
    content = q
    response = HttpResponse(s, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
    return response


def check(request):
    try:
        uid=request.POST.get('uid')
        uname=request.POST.get('uname')
        role=request.POST.get('role')
        f=request.POST.get('file')
        fid=request.POST.get('fid')
        print uid,uname,role,f,fid
        ob=timeuser.objects.get(fid=int(fid))
        us=stafc.objects.get(username=uname)
        ok=filedates.objects.get(id=int(fid))
        print ob.oruser
        print ob.anduser
        sp1=ob.oruser.split("&")
        print sp1
        pred=[]
        for i in sp1:
            fg=i.split("$")
            pred.append(fg)
        print pred
        pqr=0
        plott=[]
        qo=0
        qp=0
        qpl=[]
        man=[]
        for i in pred:
            print"pred",i
            t1=time.time()
            print "i[0]",i[0]
            print "role",role,"dep",us.dep
            man.append(i[0])
            if role in i[0] and str(us.dep) in str(ok.access):
                dbt=str(ok.date)+" "+i[1]+":00"
                dbt=datetime.strptime(dbt,"%d/%m/%Y %I:%M:%S")
                now=datetime.now().strftime("%d/%m/%Y %I:%M:%S")
                now=datetime.strptime(now,"%d/%m/%Y %I:%M:%S")
                print "dbt",dbt
                print "now",now
                delta = now - dbt
                
                print "delta",delta  # prints: 1 day, 7:50:05
                #tot= delta.total_seconds()
                print "delta","-" in str(delta) 
                if "-" in str(delta):
                    print"---"
                    obi=askey.objects.get(uid=uid,username=uname,fileid=fid).delete()
                    ob=okay(uid=uid,username=uname,fid=fid,filename=f,priv=str(random.getrandbits(256))).save()
                    objj=accepted(uid=uid,uname=uname,role=role).save()
                    pqr=1
                    t2=time.time()
                    plott.append(t2-t1)
                    qpl.append(qp+1)
                else:
                    t2=time.time()
                    plott.append(t2-t1)
                    qpl.append(qp+1)
            else:
                t2=time.time()
                plott.append(t2-t1)
                qpl.append(qp+1)
        plt.plot(plott,qpl)
        plt.xlabel('Roles')
        plt.ylabel('Time Complexity')
        plt.title('Change in your graph')
        #plt.show()
        dec(man)
        if pqr==1:
            obj=askey.objects.raw("select * from App_askey order by id desc limit 5")
            return render(request,'keyreq.html',{"data":obj,"q":"q"})
        sp1=ob.anduser.split("&")
        print sp1
        pred1=[]
        for i in sp1:
            fg=i.split("$")
            pred1.append(fg)
        print pred1
        op=len(pred1)
        uo=[]
        qpl=[]
        plott=[]
        pqr=0
        for i in range(op):
            uo.append(i)
        qp=0
        for i in pred1:
            print"pred1",i
            t1=time.time()
            print "i[0]",i[0]
            print "role",role
            if role in i[0] and str(us.dep) in str(ok.access):
                dbt=str(ok.date)+" "+i[1]+":00"
                dbt=datetime.strptime(dbt,"%d/%m/%Y %I:%M:%S")
                now=datetime.now().strftime("%d/%m/%Y %I:%M:%S")
                now=datetime.strptime(now,"%d/%m/%Y %I:%M:%S")
                print "dbt",dbt
                print "now",now
                delta = now - dbt
                
                print "delta",delta  # prints: 1 day, 7:50:05
                #tot= delta.total_seconds()
                print "delta","-" in str(delta) 
                if "-" in str(delta):
                    print "inside"
                    obi=askey.objects.get(uid=uid,username=uname,fileid=fid).delete()
                    ob=okay(uid=uid,username=uname,fid=fid,filename=f,priv=str(random.getrandbits(256))).save()
                    pqr=1
##                    t2=time.time()
##                    plott.append(t2-t1)
##                    qpl.append(qp+1)
                else:
                    pass
##                    t2=time.time()
##                    plott.append(t2-t1)
##                    qpl.append(qp+1)
            else:
                t2=time.time()
                plott.append(t2-t1)
                qpl.append(qp+1)
    ##    plt.plot(plott,qpl)
    ##    plt.xlabel('Roles')
    ##    plt.ylabel('Time Complexity')
    ##    plt.title('Change in your graph')
    ##    plt.show()
                    
        if pqr==1:
            obj=askey.objects.raw("select * from App_askey order by id desc limit 5")
            objj=accepted(uid=uid,uname=uname,role=role).save()
            return render(request,'keyreq.html',{"data":obj,"q":"q"})
        objj=rejected(uid=uid,uname=uname,role=role).save()
        obj=askey.objects.raw("select * from App_askey order by id desc limit 5")
        return render(request,'keyreq.html',{"data":obj,"r":"r"})
    except Exception,ex:
        print "Exception: "+str(ex)
        print request.session['user']
        obj=askey.objects.raw("select * from App_askey order by id desc limit 5")
        return render(request,'keyreq.html',{"data":obj,"r":"r"})
def showfiles(requesst):
    a=request.POST.get("id")
    b=request.POST.get("name")
    c=request.POST.get("priv")
    decrypted_string = decryption(C1, C2, privKey)
    s=Hash.decode(str(decrypted_string))
    return render(request,'aprmess.html',{"data":ob})
##def apmess(request):
##    ob=okay.objects.all()
##    print ob
##    for i in ob:
##        print i.fid,i.filename
##    return render(request,'aprmess.html',{"data":ob})

def apmess(request):
    ob=okay.objects.raw("select * from App_okay where username='"+request.session['user']+"' order by id desc limit 10;")
    print ob
    for i in ob:
        print i.fid,i.filename
    return render(request,'aprmess.html',{"data":ob,"z":request.session['user']})
def approvemsg(request):
    x=request.GET.get("d1")
    obj=filedates.objects.get(id=x)
    obj.approve=1
    obj.save()
    ob=filedates.objects.raw("select * from App_filedates where approve=0 order by id desc limit 3;")
    data={}
    ob=serializers.serialize("json",ob)
    data["dt1"]=json.loads(ob)
    print data
    return JsonResponse(data,safe=False)

def deprole(request):
    x=request.GET.get("d1")
    ob=role.objects.raw("select * from App_role where department='"+x+"'")
    data={}
    ob=serializers.serialize("json",ob)
    data["dt1"]=json.loads(ob)
    print data
    return JsonResponse(data,safe=False)

def newrole(request):
    x=request.GET.get("d1")
    ob=role.objects.raw("select * from App_role where department='"+x+"'")
    data={}
    ob=serializers.serialize("json",ob)
    data["dt1"]=json.loads(ob)
    print data
    return JsonResponse(data,safe=False)

def read_file(request):
    global abcd
    if abcd==0:
        abcd=12
        s = request.FILES["files2"]
        print s
        if request.FILES["files2"]:
            fs = FileSystemStorage("App/static/files/")
            fs.save(s.name, s)
            filename ="App/static/files/"+s.name
            obj = filedates.objects.last()
            obj.filename=s.name
            obj.save()
        obj = filedates.objects.last()
        print type(obj.filename)
        fo=open("App/static/files/"+str(obj.filename),"rb")
        global file_content
        file_content=fo.read()
        fo.close()
        print obj.access
        print type(obj.access)
        t=obj.access.split(")")
        print t
        ui=[]
        global andl
        global orl
        for i in t:
            sas=""
            for j in i:
                if j.isdigit() or j.isalpha() or j=="," or j=="." or j=="-":
                    sas+=j
            if sas[0]=="u":
                sas=sas[1:]
            mn=sas.split(",")
            kl=[]
            for k in mn:
                kl.append(str(k))
            ui.append(kl)
        print ui
        
        for i in range(len(ui)):
            if ui[i][-1]=="1":
                for j in range(len(ui[i])):
                    if ui[i][j]!='' or ui[i][j]!='u':
                        andl.append(ui[i][j])
            if ui[i][-1]=="-1":
                for j in range(len(ui[i])):
                    if ui[i][j]!='' or ui[i][j]!='u':
                        orl.append(ui[i][j])
        
        
        while 'u' in andl:
            andl.remove('u')
        
        while 'u' in orl:
            orl.remove('u')
        while '' in orl:
            orl.remove('')
        while '' in andl:
            andl.remove('')
        orl=orl[:-1]
        andl=andl[:-1]
        print "and gate"
        print andl
        print "or gate"
        print orl
        print
        role=['MCA','MBA','MATHS','LITERATURE']
        while 'MCA' in andl:
            andl.remove('MCA')
        while 'MBA' in andl:
            andl.remove('MBA')
        while 'CS' in andl:
            andl.remove('CS')
        while 'CIVIL' in andl:
            andl.remove('CIVIL')
        while 'MECH' in andl:
            andl.remove('MECH')
        while 'EC' in andl:
            andl.remove('EC')
        
        while 'MCA' in orl:
            orl.remove('MCA')
        while 'MBA' in orl:
            orl.remove('MBA')
        while 'CS' in orl:
            orl.remove('CS')
        while 'CIVIL' in orl:
            orl.remove('CIVIL')
        while 'MECH' in orl:
            orl.remove('MECH')
        while 'EC' in orl:
            orl.remove('EC')
##        i8=len(orl)
##        for i in range(i8):
##            print orl[i]
##            if orl[i] in role:
##                
##                orl.remove(orl[i])
##        i8=len(andl)
##        for i in range(i8):
##            print andl[i]
##            if andl[i] in role:
##                andl.remove(andl[i])
        return render(request,'datacontent.html',{"zx":file_content,"data":andl,"d":orl})
    else:
        global andl
        global orl,file_content
        return render(request,'datacontent.html',{"zx":file_content,"data":andl,"d":orl})
def boolean(request):
    x=request.GET.get("d1")
##    y=request.GET.get("d2")
##    z=request.GET.get("d3")
    import datetime
    now=datetime.datetime.now()
    y=now.strftime("%d/%m/%Y")
    z=now.strftime("%H:%M:%S")
    q=request.GET.getlist("d4[]")
    for i in q:
        policy.append(str(i))
    try:
        bloom(policy)
    except:
        pass
    booly=x.split(";")
    obc=filedates(access=booly,time=z,date=y,filename="")
    obc.save()
    #lsss1(booly)
    return HttpResponse("Success")


def discard(request):
    x=request.GET.get("d1")
    obj=stafc.objects.get(id=x).delete()
    ob=stafc.objects.raw("select * from App_stafc where approve=0;")
    data={}
    ob=serializers.serialize("json",ob)
    data["dt1"]=json.loads(ob)
    print data
    return JsonResponse(data,safe=False)

def discardmsg(request):
    x=request.GET.get("d1")
    obj=filedates.objects.get(id=x).delete()
    ob=filedates.objects.raw("select * from App_filedates where approve=0 order by id desc limit 3;")
    data={}
    ob=serializers.serialize("json",ob)
    data["dt1"]=json.loads(ob)
    print data
    return JsonResponse(data,safe=False)


