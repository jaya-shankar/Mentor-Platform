"""studentPlatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from studentPage.views import student_view,getChat_view,getDetails_view,sendDoubt_view
from mentorPage.views import mentor_view,createGroup_view,login_view,signUp_view,logout_view,courseDetails_view,addMessage_view,getDoubt_view,removeDoubt_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mentor_view ,name="mentor"),
    
    path('student', student_view,name="student"),
    path('create_group', createGroup_view,name="createGroup"),
    path('login', login_view,name="login"),
    path('register', signUp_view,name="register"),
    path('logout', logout_view,name="logout"),
    
    path('details/<str:title>', courseDetails_view,name="details"),
    path('add_message', addMessage_view,name="addMessage"),
    path('get_chats', getChat_view,name="getChat"),
    path('get_details', getDetails_view,name="getDetails"),
    path('send_doubt', sendDoubt_view,name="sendDoubt"),
    path('get_doubts', getDoubt_view,name="getDoubt"),
    path('remove_doubt', removeDoubt_view,name="removeDoubt"),

]
