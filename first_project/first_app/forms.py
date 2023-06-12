from django.forms import forms
from first_app.models import  User,Profile
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.forms import ModelForm ,widgets
from .models import  Profile
from django.contrib.auth.models import User
from django.forms import widgets
from unicodedata import category
from .models import Post ,Comment
# from django.forms import ClearableFileInput

# class CommentForm(ModelForm):
#     Comment = forms.CharField(widget=forms.Textarea(attrs={
#             'rows': '4',
#     }))

class CreateBlogForm(ModelForm):

    class Meta:
             model = Post
             fields = ['title','image', 'body']



#profile extra
# class ProfilePicForm(ModelForm):
#      profile_pic = forms.ImageField(label ='Profile.Picture' )
   
#      class meta:
#         model = Profile
#         fields =('profile_pic', )




# class ProfilePicForm(forms.ModelForm):
#     profile_pic = forms.ImageField(label ='Profile.Picture' )
    
    # class Meta:
    #     model = Profile
    #     fields = ('profile_pic', )


class EditUserForm(UserChangeForm): 
    class Meta():
        model = User 
        fields = ('username', 'first_name','last_name' , 'email')

class LoginForm(forms.Form):
    class Meta():
        model = User
        fields = '__all__'

class UserForm(forms.Form):
    class Meta():
        model = User
        fields = '__all__'




# 345677djc 

# class EditProfileForm(ModelForm):
#          class Meta:
#              model = User
#              fields = ('email','first_name','last_name')


class ProfileForm(ModelForm):
    # bio = forms.CharField(max_length=100)
    # contact = forms.CharField(max_length=100)
    # profile_pic = forms.ImageField()
    # location = forms.CharField(max_length=100)
    
    class Meta():
        model = Profile
        # fields = ( 'bio',  'location')
        fields = '__all__'
        exclude = ['user']

        widgets={

            # 'bio': TextInput(attrs={'class':'form-control'}),
            # 'contact': TextInput(attrs={'class':'form-control'}),
            # 'profile_pic': FileInput(attrs={'class':'form-control'}),
            # 'location': Textarea(attrs={'class':'form-control'}),

        }

#djw cjk389hd






class RegForm(UserCreationForm):
    class Meta():
        model = User
        fields = ('username','email', 'password1', 'password2')