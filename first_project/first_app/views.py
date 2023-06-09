from django.shortcuts import render,redirect
from django.http import HttpResponse
from first_app.forms import  LoginForm,RegForm, EditUserForm,CreateBlogForm
from django.contrib.auth import  views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView,UpdateView
from django.views.generic import UpdateView
from first_app.models import  Profile
from django.urls import reverse_lazy
from .forms import  ProfileForm
from django.views.generic import ListView,DetailView,UpdateView,DeleteView,CreateView,TemplateView, ListView
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm 
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.http import HttpResponse
from .models import Post

# from .forms import Profile, Meep
# Create your views here.



def post_like(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, id=pk)
        # if likes.filter(id=request.user.id)
    else:
        messages.success(request,("you must be logged in to view this post"))
        return redirect("home")

def create_post1(request):
    if not request.user.is_authenticated:
        return redirect('login')

    post = Post.objects.all()
    # ordering = ["-id"]

    form = CreateBlogForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = user.objects.filter(username=user.username).first()
        obj.author = author
        obj.save()
        form= CreateBlogForm()
    
    context = {'form': form, 'object_list': post}
    return render(request, 'testapp/home.html', context)


def must_authenticate_view(request):
    return render(request, 'testapp/must_authenticate.html', {})

def create_blog_view(request):

    context ={}

    user= request.user
    if not user.is_authenticated:
        return redirect('login')

    form = CreateBlogForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = user.objects.filter(username=user.username).first()
        obj.author = author
        obj.save()
        form= CreateBlogForm()

    context['form']= form 

    return render(request, 'testapp/create_blog.html', context)





def create_post(request):

    context ={}

    user= request.user
    if not user.is_authenticated:
        return redirect('login')

    form = CreateBlogForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = user.objects.filter(username=user.username).first()
        obj.author = author
        obj.save()
        form= CreateBlogForm()

    context['form']= form 

    return render(request, 'testapp/home.html', context)

class AddPostView(CreateView):
    model = Post
    template_name = 'testapp/add_post.html'
    fields= '__all__'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'testapp/article_detail.html'

    form = CommentForm



# class HomeVieww(ListView):
#     model = Post
#     template_name = 'testapp/home.html'








def accountSettings(request):
    profile= request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
            messages.success(request, 'Profile edited successfully.')
            # return render(request,'testapp/index.html')


    context = {'form':form}
    return render(request, 'testapp/account_settings.html', context)

class EditProfiePageView(UpdateView):
    model = Profile
    tamplate_name= 'testapp/edit_profie_page.html'
    fields = ['bio' , 'location',]
    success_url = reverse_lazy('home')



# def update_profile(request):
#     # context['page_title'] = "Update Profile"
#     user = User.objects.get(id= request.user.id)
#     profile = Profile.objects.get(user= user)
#     # context['userData'] = user
#     # context['userProfile'] = profile
#     if request.method == 'POST':
#         data = request.POST
#         # if data['password1'] == '':
#         # data['password1'] = '123'
#         form = UpdateProfile(data, instance=user)
#         if form.is_valid():
#             form.save()
#             form2 = UpdateProfileMeta(data, instance=profile)
#             if form2.is_valid():
#                 form2.save()
#                 messages.success(request,"Your Profile has been updated successfully")
#                 return redirect("profile")
#             else:
#                 # form = UpdateProfile(instance=user)
#                 context['form2'] = form2
#         else:
#             context['form1'] = form
#             form = UpdateProfile(instance=request.user)
#     return render(request,'testapp/update_profile.html')





def edit_form(request):
    if request.method == 'POST': 
        edit_form = EditUserForm(request.POST, instance=request.user or None)
        if edit_form.is_valid(): 
                 edit_form.save() 
        messages.success(request, 'User edited successfully.')
    else: 
        edit_form = EditUserForm(instance=request.user) 
    return render(request, 'testapp/edit_form.html', {'edit_key':edit_form})


def profile_form(request ,pk):
        if request.method == 'POST': 
            profile_form = ProfileForm(request.POST, instance=request.user.profile(pk=pk) or None  )
            if profile_form.is_valid(): 
                     profile_form.save() 
            messages.success(request, 'User edited successfully.')

        else:
            # return render(request,
        # else: 
            profile_form = ProfileForm(request.user ) 
            # profile_form = Profile.objects.get()

            return render(request, 'testapp/profile_form.html', {'profile_key':profile_form})


def view_profile(request , user_id):
    profile = Profile.objects.get(id=user_id)
    return render(request, 'testapp/view_profile.html',{'profile':profile})

def edit_profile(request, user_id):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('view_profile', user_id)


# def edit_profile(request  ,user_id):
#     if request.method == 'POST':
#         # form = EditProfileForm(request.POST, instance=request.user)
#         profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.userprofile (id=user_id))  # request.FILES is show the selected image or file

#         if form.is_valid() and profile_form.is_valid():
#             user_form = form.save()
#             custom_form = profile_form.save(False)
#             custom_form.user = user_form
#             custom_form.save()
#             return redirect('view_profile1')
#     else:
#         # form = EditProfileForm(instance=request.user)
#         profile_form = ProfileForm(instance=request.user.userprofile (id=user_id))
#         args = {}
#         # args.update(csrf(request))
#         args['form'] = form
#         args['profile_form'] = profile_form
#         return render(request, 'testapp/edit_profile1.html', args)






def pass_form(request): 
    if request.method == 'POST':
            pass_form = PasswordChangeForm(data=request.POST, user=request.user)
            if pass_form.is_valid():
                pass_form.save()
                update_session_auth_hash(request, pass_form.user)
                return redirect('/')
                # messages.success(request, 'Your password was successfully updated!')
                # return HttpResponseRedirect(reverse_lazy('view_profile'))
                #  return HttpResponseRedirect(reverse_lazy('adopcion:solicitud_listar'))
                # return render(request,'testapp/index.html')
            else:
                
              pass_form = PasswordChangeForm(user=request.user)
            return render(request, 'testapp/pass_form.html', {'pass_key': pass_form})

class EditProfilePageView( UpdateView):
    model = Profile
    template_name = 'testapp/edit_profile_page.html'
    fields = ['first_name','last_name','contact','location','bio' ,'profile_pic',]
    success_url = reverse_lazy('view_profile')

def Update_profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProfileForm( request.POST ,request.FILES ,instance=profile )
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = ProfileForm(profile)
    return render(request, 'testapp/edit_profile_page.html', {'form': form})

# class ProfileUpdateView(TemplateView):
#     # edit_form = EditUserForm
#     profile_form = ProfileForm
#     template_name = 'first_app/profile-update.html'

# def register(request):
#       form = UserCreationForm(request.POST or None)
#     #   if request.method == 'POST':
#     #         register_form = RegForm(request.POST)
#       if form.is_valid():
#                   User_obj=form.save()
#                   return render(request, 'testapp/login.html')

#                 #   return redirect('testapp/login.html')
#              # register_form = RegForm
#       return render(request, 'testapp/register.html',{"form": form})


# def profile_form(request ,pk):
#     if request.method == 'POST': 
#         form = ProfileForm(request.POST, request.user or None)
#         #   form = ProfileForm(request.POST)
#         if form.is_valid(): 
#             cd = form.cleaned_data
#             # profile = form.save(commit=False)
#             pc = ProfileForm(
#                 # first_name=cd['first_name'],
#                 # last_name=cd['last_name'],
#                 # contact=cd['contact'],
#                 # location=cd['location'],
#                 # bio=cd['bio'],
#                 # profile_pic=cd['profile_pic']
#                 # user=request.user
#             )
#             pc.save()
#             return redirect('view_profile')
#         #         profile_form.save() 
#         # messages.success(request, 'profile edited successfully.')
#     else: 
#         profile_form = ProfileForm(request.user) 
#         # return render(request, 'testapp/profile_form.html', {'profile_key': profile_form})


def edit_form(request):
    if request.method == 'POST': 
        edit_form = EditUserForm(request.POST, instance=request.user or None)
        if edit_form.is_valid(): 
                 edit_form.save() 
        messages.success(request, 'User edited successfully.')
    else: 
        edit_form = EditUserForm(instance=request.user) 
    return render(request, 'testapp/edit_form.html', {'edit_key':edit_form})

# def view_profile(request ,pk):


#     if pk:
#         user.object.get(pk=pk)
#     else:
#         user= request.user

#     return render(request, 'testapp/view_profile.html',{'user'.user})
def view_profile(request , user_id):
    profile = Profile.objects.get(id=user_id)
    return render(request, 'testapp/view_profile.html',{'profile':profile})
    
# def 
def userprofile(request, user_id):
    user = User.objects.get(id=user_id)
    profile = Profile.objects.get(user=user)
    return render(request, 'testapp/profile.html',{'profile':profile})

class HomeView(TemplateView):
    template_name = 'testapp/index.html'

class Log_outView(TemplateView):
    template_name = 'testapp/logout.html'

def index(request):
    return render(request, 'testapp/index.html')    

def Explore(request):
    return render(request, 'testapp/explore.html')

def Chat(request):
    return render(request, 'testapp/chat.html')     


def Log_out(request):
    messages.success(request, 'You have logged out')

    return render(request, 'testapp/logout.html')

class Login_view(auth_views.LoginView):
      template_name = 'testapp/login.html'  
      context_object_name = 'form'    


def register(request):
        form = UserCreationForm(request.POST or None)
        #   if request.method == 'POST':
        #         register_form = RegForm(request.POST)
        if form.is_valid():
                    User_obj=form.save()

                    return render(request, 'testapp/login.html')
        messages.success(request, 'Registration successful')

                    #   return redirect('testapp/login.html')
                # register_form = RegForm
        return render(request, 'testapp/register.html',{"form": form})



    
      