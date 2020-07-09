from django.urls import path
from django.conf import settings

from . import views 


urlpatterns = [
    path('student', views.student_view,name="student"),
    path('get_chats', views.getChat_view,name="getChat"),
    path('get_details', views.getDetails_view,name="getDetails"),
    path('send_doubt', views.sendDoubt_view,name="sendDoubt"),
    path('change_password', views.changePassword_view,name="changePassword"),


]

