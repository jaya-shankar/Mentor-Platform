from rest_framework import serializers
from django.contrib.auth.models import User

from mentorPage.models import Course,Chats
from studentPage.models import Doubts


class GroupNameSerializer(serializers.ModelSerializer):

    class Meta:
        model=Course
        fields=('id','title')

class CourseSerializer(serializers.ModelSerializer):
    creator=serializers.SerializerMethodField()
    messages = serializers.SerializerMethodField()
    members=serializers.SerializerMethodField()
    class Meta:
        model=Course
        fields=('id' ,
            'title' ,
            'level' ,
            'description' ,
            'takeaways' ,
            'creator' ,
            'messages',
            'members'
            )

    def get_messages(self,course):
        count=Chats.objects.filter(course=course).count()
        return count
    def get_creator(self,course):
        return UsersSerializer(course.creator).data

    def get_members(self,course):
        return UsersSerializer(course.members,many=True).data
    
class NewCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('title',
                    'level' ,
                    'description' ,
                    'takeaways' ,
                )

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chats
        fields = ('message',
                    'image'
                )

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('username','id')


class UserSerializer(serializers.ModelSerializer):
    groupsJoined=serializers.SerializerMethodField()
    groupsCreated=serializers.SerializerMethodField()
    class Meta:
        model=User
        fields=('username','id','groupsJoined','groupsCreated')
    
   
    def get_groupsJoined(self,user):

        groupsJoined=GroupNameSerializer(user.Courses.all(),many=True)
        return groupsJoined.data
    
    def get_groupsCreated(self,user):

        groupsCreated=GroupNameSerializer(Course.objects.filter(creator=user.id),many=True)
        return groupsCreated.data


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model=Chats
        fields=('message','time','image')
class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('username','password','email','first_name','last_name')

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('username','password')

class DoubtsSerializer(serializers.ModelSerializer):
    sender=serializers.SerializerMethodField()
    receiver=serializers.SerializerMethodField()
    course=serializers.SerializerMethodField()
    class Meta:
        model=Doubts
        fields=('message','course','sender','receiver')
    def get_sender(self,doubt):
        return UsersSerializer(doubt.sender).data
    def get_receiver(self,doubt):
        return UsersSerializer(doubt.receiver).data
    def get_course(self,doubt):
        return GroupNameSerializer(doubt.course).data
    


class AskDoubtSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doubts
        fields = ('message',)

