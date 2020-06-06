from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Course



class CreateCourseForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder" : "Your Title"}))
    LEVELS = (('Beginner', 'Beginner'),('Intermediate', 'Intermediate'),('Advanced', 'Advanced'),)
    level = forms.ChoiceField(choices=LEVELS)
    description = forms.CharField(widget=forms.Textarea(attrs={"placeholder":"Description" , 
                                                                "class":"form-control" , 
                                                                "id":"description" ,
                                                                "rows": "3"}))

    takeaways = forms.CharField(widget=forms.Textarea(attrs={"placeholder":"Takeaways" , 
                                                             "class":"form-control" ,  
                                                             "id":"takeaways" ,
                                                             "rows": "3"}))
    creator = forms.IntegerField()
    class Meta:
        model = Course
        fields = [
            'title' ,
            'level' ,
            'description' ,
            'takeaways' ,
            'creator' ,
           
        ]



class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder" : "Username",
                                                                "class" : "form-control",
                                                                "id" : "user-name",
                                                                "required" : True ,
                                                                "autofocus": True}))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder" : "Password",
                                                                    "class" : "form-control",
                                                                    "required" : True,
                                                                    }))                    

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder" : "Repeat Password",
                                                                    "class" : "form-control",
                                                                    "required" : True,
                                                                    }))                                        
    class Meta:
        model=User
        fields = [
            'username',
            'password1' ,
            'password2' 
            
        ]





