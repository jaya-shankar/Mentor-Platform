from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login, logout
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.decorators import login_required
from django.core import serializers


from rest_framework import generics,permissions
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework.renderers import JSONRenderer


from mentorPage.models import Course,Chats
from studentPage.models import Doubts

from .serializers import GroupNameSerializer,CourseSerializer,UsersSerializer,UserSerializer,ChatSerializer,RegistrationSerializer
from .serializers import DoubtsSerializer,NewCourseSerializer,MessageSerializer, AskDoubtSerializer,LoginSerializer
# Create your views here.


class get_all_groups_view(generics.ListAPIView):
    """
    GET all courses
    """
    queryset=Course.objects
    serializer_class = GroupNameSerializer

    def get(self,request,*args, **kwargs):
        return Response(GroupNameSerializer(self.queryset.all(),many=True).data)
    
    permission_classes = [permissions.IsAuthenticated]
    serializer_class=NewCourseSerializer
    def post(self, request, *args, **kwargs):
        course_details=dict(request.data)
        del course_details['csrfmiddlewaretoken']
        course_details['creator']=request.user
        course=Course.create(course_details)
        course.save()
        return Response(CourseSerializer(course).data, status=status.HTTP_201_CREATED)


class get_course_info_view(generics.ListAPIView):
    """
    GET course info
    """
    queryset=Course.objects.all()

    def get(self,request,*args, **kwargs):
        course=valdiate_course(kwargs)
        if(not course):
            return error_404(message="Course does not exist")
        else:
            return Response(CourseSerializer(course).data)

    permission_classes = [permissions.IsAuthenticated]
    serializer_class=NewCourseSerializer
    def put(self, request, *args, **kwargs):
        course=valdiate_course(kwargs)
        if(not course):
            return error_404(message="Course does not exist")
        if(request.user==course.creator):
            serialized=NewCourseSerializer(data=request.data,instance=course)
            if(serialized.is_valid()):
                serialized.save()
                return Response(CourseSerializer(course).data, status=status.HTTP_201_CREATED)
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

        return error_404(message="Only Creator can update course details ", status=status.HTTP_401_UNAUTHORIZED)

    def delete(self,request,*args, **kwargs):
        course=valdiate_course(kwargs)
        if(not course):
            return error_404(message="Course does not exist")
        if(request.user!=course.creator):
            return error_404(message="Only Creator can delete")
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class get_users_view(generics.ListAPIView):
    """
    GET all users
    """

    queryset=User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        return Response(UsersSerializer(self.queryset.all(),many=True).data)

    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serialized = RegistrationSerializer(data=request.data)
        if serialized.is_valid():
            User.objects.create_user(
                email=serialized.initial_data['email'],
                username=serialized.initial_data['username'],
                first_name=serialized.initial_data['first_name'],
                last_name=serialized.initial_data['last_name'],
                password=serialized.initial_data['password']
        )
            return Response(serialized.data, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)



class get_user_info_view(generics.ListAPIView):
    """
    GET user info
    """

    queryset=User.objects.all()
    courses=Course.objects.all()
    serializer_class = RegistrationSerializer
   
    def get(self,request,*args, **kwargs):
        user = valdiate_user(kwargs)
        if(not user):
            return error_404(message="User does not exist")
        return Response(UserSerializer(user).data)

    permission_classes = [permissions.IsAuthenticated]
    def put(self,request,*args, **kwargs):
        user = valdiate_user(kwargs)
        if(user==request.user):
            serialized = RegistrationSerializer(data=request.data,instance=request.user)
            if serialized.is_valid():
                serialized.save()
                return Response(serialized.data, status=status.HTTP_201_CREATED)
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

        return error_404(message="Only Authorised can update there own details ")

    def delete(self,request,*args, **kwargs):
        user = valdiate_user(kwargs)
        if(request.user==user):
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return error_404(message="One can delete there own account")

        
class get_messages_view(generics.ListAPIView):

    queryset=Chats.objects.all()
    serializer_class=ChatSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self,request,*args,**kwargs):
        course=valdiate_course(kwargs)
        if(not course):
            return error_404(message="Course does not exist")
        chat=self.queryset.filter(course=course)
        if(request.user.Courses.exists() or request.user==course.creator):
            return Response(ChatSerializer(chat,many=True).data)
        return error_404(message="Only group members can view messages" ,status=status.HTTP_401_UNAUTHORIZED)

    serializer_class=MessageSerializer
    def post(self,request,*args,**kwargs):

        course=valdiate_course(kwargs)
        if(not course):
            return error_404(message="Course does not exist")
        if(course.creator!=request.user):
            return error_404(message="Only creator of the groups can send message",status=status.HTTP_403_FORBIDDEN)
        message=request.data.get("message")
        image=request.data.get("image")
        chat = Chats(course=course,message=message,image=image)
        chat.save()
        chats=self.queryset.filter(course=course)
        
        return Response(ChatSerializer(chats,many=True).data, status=status.HTTP_201_CREATED)


class login_view(generics.CreateAPIView):

    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer

    def post(self,request,*args,**kwargs):
        logout(request)
        username = request.data.get("username")
        password = request.data.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return Response(
                data={
                    "message": "Login Sucessful"
                }
            )

        return error_404(message="Login Failure" , status=status.HTTP_401_UNAUTHORIZED)
        

class get_doubts_user_view(generics.CreateAPIView):
    queryset = Doubts.objects.all()
    serializer_class = DoubtsSerializer

    def get(self,request,*args,**kwargs):
        user = valdiate_user(kwargs)
        if(not user):
            return error_404(message="User does not exist")
        doubts=self.queryset.filter(sender=user)
        return Response(DoubtsSerializer(doubts,many=True).data)


class get_doubts_course_view(generics.CreateAPIView):
    queryset = Doubts.objects.all()
    serializer_class = DoubtsSerializer

    def get(self,request,*args,**kwargs):
        course = valdiate_course(kwargs)
        if(not course):
            return error_404(message="Course does not exist")
        #should add only creator can view the doubts
        doubts=self.queryset.all().filter(course=course)
        return Response(DoubtsSerializer(doubts,many=True).data,)

    serializer_class = AskDoubtSerializer

    def post(self,request,*args,**kwargs):
        course=valdiate_course(kwargs)
        if(not course):
            return error_404(message="Course does not exist")
        new_doubt = Doubts.create(request.user,course,request.data["message"])
        new_doubt.save()
        doubts=self.queryset.all().filter(course=course)
        return Response(DoubtsSerializer(doubts,many=True).data,)

    
def valdiate_course(kwargs):
    try:
        a_course = Course.objects.get(pk=(kwargs["id"]))
        return a_course
    except KeyError:
        a_course = Course.objects.get(title=kwargs["name"])
        return a_course
        
    except Course.DoesNotExist:
        return None

def valdiate_user(kwargs):
    try:
         user = User.objects.get(pk=int(kwargs["id"]))
    except KeyError:
        user = User.objects.get(username=kwargs["name"])
    except User.DoesNotExist:
        return None
    return user

def error_404(message,status=status.HTTP_404_NOT_FOUND):
    return Response(
                data={
                    "message": message
                },
                status=status
            )