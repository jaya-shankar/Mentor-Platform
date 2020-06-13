from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.decorators import login_required


from mentorPage.models import Course,Chats
from .models import Doubts

# Create your views here.
@login_required()
def student_view(request,*args,**kwargs):
    all_courses=Course.objects.all()
    user=request.user
    enrolled_courses=Course.objects.filter(members=user)
    enrolled_course_titles=[]
    for i in enrolled_courses:
        enrolled_course_titles.append(i.title)

    unenrolled_courses = all_courses.difference(enrolled_courses)
    unenrolled_course_titles=[]
    for i in unenrolled_courses:
        unenrolled_course_titles.append(i.title)
        
    context={"enrolled_courses" : enrolled_courses,
                "unenrolled_courses" : unenrolled_courses , 
                "username" :user.username ,
                }

    if(request.method=="GET"):
         return render(request,"studentHome.html",context)

    if(request.method=="POST"):
        if(request.POST.get("courseName")):
            joined_course=request.POST.get("courseName")
            course=Course.objects.get(title=joined_course)
            course.members.add(User.objects.get(id=request.user.id))
            return render(request,"studentHome.html",context)
        else:
            
            courseName=request.POST["course_name"]
            creatorID=Course.objects.get(title=courseName).creator
            creatorName=User.objects.get(id=creatorID).username
            
            chats=Chats.objects.filter(course=Course.objects.get(title=courseName))
            
            cleaned_chats=[]
            for i in range(len(chats)):
                cleaned_message={  
                                "id" : chats[i].id,
                                "message" : chats[i].message,
                                "image" : chats[i].image ,
                                "date" : chats[i].time.strftime("%x"),
                                "time" :chats[i].time.strftime("%H:%M")}
                cleaned_chats.append(cleaned_message)
            
            context={"chats":cleaned_chats,
                        "enrolled_courses" : enrolled_courses,
                        "unenrolled_courses" : unenrolled_courses , 
                        "username" :user.username ,
                        "creatorName" : creatorName,
                        "chats" : cleaned_chats,
                        "title" : courseName,
                        
                        }
            print(context)
            return render(request,"studentHome.html",context)

   
    
   
        
@login_required()
def getChat_view(request,*args,**kwargs):
    courseName=request.GET["course_name"]
    creatorID=Course.objects.get(title=courseName).creator
    creatorName=User.objects.get(id=creatorID).username
    
    chats=list(Chats.objects.filter(course=Course.objects.get(title=courseName)).values())
    cleaned_chats=[]
    for i in chats:
        cleaned_message={  "id" : i["id"],
                        "message" : i["message"],
                        "image" : i["image"] ,
                        "date" : i["time"].strftime("%x"),
                        "time" :i["time"].strftime("%H:%M")}
        cleaned_chats.append(cleaned_message)
    
    response={"chats":cleaned_chats,
                "creatorName" : creatorName}
    
    return JsonResponse(response ,safe=False)

@login_required()
def getDetails_view(request,*args,**kwargs):
    courseName=request.GET["course_name"]
    courseDetails = ((Course.objects.get(title=courseName)))
    creator=User.objects.get(id=courseDetails.creator).username
    response={"title":courseDetails.title,
                "description":courseDetails.description,
                "level": courseDetails.level,
                "takeaways": courseDetails.takeaways,
                "creator" : creator
                }
    return JsonResponse(response ,safe=False)

@login_required()
def sendDoubt_view(request,*args,**kwargs):
    message=request.GET["message"]
    try:
        student=request.GET["user"]
        course=request.GET["course"]
        mentor=request.GET["mentor"]

    except:
        doubtID=request.GET["doubt_id"]
        p_doubt=Doubts.objects.get(id=doubtID)
        student=p_doubt.receiver
        mentor=p_doubt.sender
        course=p_doubt.course
    
    doubt=Doubts(sender=student,receiver=mentor,message=message,course=course)
    doubt.save()

    
    return HttpResponse("SUCESS")