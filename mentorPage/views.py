from django.shortcuts import render,redirect
from django.contrib.auth import authenticate , login, logout
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import CreateCourseForm,SignUpForm
from .models import Course,Chats
from studentPage.models import Doubts

# Create your views here.

@login_required()
def mentor_view(request,title="",*args,**kwargs):


    courses=Course.objects.filter(creator=request.user.id)
    courses_title=[]
    users=User.objects.all()
    for i in courses:
        courses_title.append(i.title)
    chats=[]
    if(title!=""):
        chats=Chats.objects.filter(course=Course.objects.get(title=title))
    
    context={"courses" : courses_title,
                "username" : request.user.username,
                "chats" : chats,
                "title" : title
                }

    if(request.method=="GET"):
        return render(request,"mentorHome.html",context)
    if(request.method=="POST"):

        return render(request,"mentorHome.html",context)



@login_required()
def createGroup_view(request,*args,**kwargs):
    if(request.method=="GET"):
        print("hello")
        form = CreateCourseForm({"creator":request.user.id})
        context={
            "form":form 
        }
        return render(request,"createGroup.html",context)

    elif(request.method=="POST"):
        form = CreateCourseForm(request.POST)
        if(form.is_valid()):
            details=form.cleaned_data
            details["creator"]=request.user.id
            form = CreateCourseForm(details)
            form.save()
            
        else:
            return render(request,"createGroup.html",context)

        return HttpResponseRedirect(reverse(mentor_view))

def login_view(request,*args,**kwargs):
    if(request.method=="GET"):
        context={}
        return render(request,"login.html",context)
    if(request.method=="POST"):
        print("login")
        print(request.POST)
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        context={}
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse(mentor_view))

        context={"message":"Invalid Login Credentials"}
        
        return render(request,"login.html",context)


def signUp_view(request,*args,**kwargs):
    if(request.method=="GET"):
        form = SignUpForm()
        context={"form" : form}
        return render(request,"signUp.html",context)
    if(request.method=="POST"):
        
        form=SignUpForm(request.POST)
       
        context={"form" : form}
        if(form.is_valid()):
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(request,username=username,password=password)
        else:
            erros=form.errors.get_json_data()
            points=[]
            for i in erros["password2"]:
                points.append(i["message"])
            context["messages"]=points
            
            return render(request,"signUp.html",context)
        if user is not None:
            login(request,user)
            print("user_id in signup")
            
            return HttpResponseRedirect(reverse(mentor_view))
        
        return render(request,"login.html",context)
   

def logout_view(request,*args,**kwargs):
    logout(request)
    return redirect(reverse(login_view))


@login_required()
def courseDetails_view(request,title,*args,**kwargs):
    courseDetails=Course.objects.get(title=title)
    context={
                "title" : courseDetails.title , 
                "level" : courseDetails.level , 
                "description" : courseDetails.description ,
                "takeaways" : courseDetails.takeaways , 
                "members" : courseDetails.members.all()
            }
    if(courseDetails.creator==request.user.id):
        return render(request, "details.html",context)
    else:
        return redirect(mentor_view)

@login_required()
def addMessage_view(request,*args,**kwargs):
    message=request.GET['message']
    courseName=request.GET['course_name']
    course=Course.objects.get(title=courseName)
    chat=Chats(course=course,message=message)
    chat.save()
    return HttpResponse("Success!")

@login_required()
def getDoubt_view(request,*args,**kwargs):
    username=request.GET["user_name"]
    doubts=list(Doubts.objects.filter(receiver=username,done=False).values())
    response={"doubts" : doubts}

    return JsonResponse(response)

def removeDoubt_view(request,*args,**kwargs):
    doubtID=request.GET["doubt_id"]

    doubt=Doubts.objects.get(id=doubtID)
    doubt.done=True
    doubt.save()
    
    return HttpResponse("sucess")

def addPhotos_view(request,*args,**kwargs):
    print(request.POST)
    
    return HttpResponse("sucess")