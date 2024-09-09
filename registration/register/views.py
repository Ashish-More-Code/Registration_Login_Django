from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


# Create your views here.
def reg(request):
    if request.method=='POST':
        uname=request.POST['input1']
        upass=request.POST['input2']
        ucpass=request.POST['input3']
        if uname=="" or upass=="" or ucpass=="":
             errmsg="Username and password cannot be empty"
             context={}
             context['emptymsg']=errmsg
             return render(request,'register.html',context)
        elif upass==ucpass:
          sucmsg="Registartion succefull"
          context={}
          context['successmsg']=sucmsg
          a=User.objects.create_user(username=uname,password=upass)
          a.save()
          return render(request,'register.html',context)
          
        else:
          errmsg="Password does not Match"
          context={}
          context['msg']=errmsg
          print("error")
          return render(request,'register.html',context)
    else:
        return  render(request,'register.html')
    

def ulogin(request):
    if request.method == 'POST':
        uname = request.POST['username']
        upass = request.POST['password']
        userauth= authenticate(request,username=uname,password=upass)
        print(userauth)
        if userauth is not None:
            context = {'loginmsg': "Login successful"}
            return render(request, 'login.html', context)
        else:
            context = {'loginmsg': "Login unsuccessful"}
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html')
    
    