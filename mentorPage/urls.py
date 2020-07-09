from django.urls import path
from django.conf import settings

from . import views 


urlpatterns = [
    path('',views.mentor_view ,name="mentor"),
    path('create_group', views.createGroup_view,name="createGroup"),
    path('login', views.login_view,name="login"),
    path('register', views.signUp_view,name="register"),
    path('logout', views.logout_view,name="logout"),
    path('details/<str:title>', views.courseDetails_view,name="details"),
    path('add_message', views.addMessage_view,name="addMessage"),
    path('get_doubts', views.getDoubt_view,name="getDoubt"),
    path('remove_doubt', views.removeDoubt_view,name="removeDoubt"),
    path('add_photos', views.addPhotos_view,name="addPhoto"),


]


