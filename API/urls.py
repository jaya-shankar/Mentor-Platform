from django.urls import path
from django.conf import settings

from . import views 


urlpatterns = [
    
    path('courses', views.get_all_groups_view.as_view() , name="courses") , 
    path('courses/<int:id>', views.get_course_info_view.as_view() , name="courseInfo-id") , 
    path('courses/title/<str:name>', views.get_course_info_view.as_view() , name="courseInfo-name") , 
    path('courses/<int:id>/doubts', views.get_doubts_course_view.as_view() , name="courseInfo-id") , 
    path('courses/title/<str:name>/doubts', views.get_doubts_course_view.as_view() , name="courseInfo-name") , 
    path('courses/<int:id>/messages', views.get_messages_view.as_view() , name="courseMsgs-id") , 
    path('courses/title/<str:name>/messages', views.get_messages_view.as_view() , name="courseMsgs-name") , 
    path('users', views.get_users_view.as_view() , name="users") , 
    path('users/<int:id>', views.get_user_info_view.as_view() , name="user") , 
    path('users/username/<str:name>', views.get_user_info_view.as_view() , name="user") , 
    path('users/<int:id>/doubts', views.get_doubts_user_view.as_view() , name="doubts") , 
    path('users/username/<str:name>/doubts', views.get_doubts_user_view.as_view() , name="doubts") , 
    path('auth', views.login_view.as_view() , name="register") ,
    
]
