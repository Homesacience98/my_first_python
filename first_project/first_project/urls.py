"""
URL configuration for first_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from first_app.views import Chat,Explore,Log_out,Login_view, register,Log_outView , view_profile ,profile_form,EditProfilePageView,pass_form,Update_profile , edit_profile,EditProfiePageView,profile_form,AddPostView,create_blog_view
from django.conf import settings
from django.conf.urls.static import static
from first_app import views
from django.contrib.auth import views as auth_views
from first_app.views import pass_form, must_authenticate_view , UserSearch, NewConversation
from first_app.views import HomeView , ArticleDetailView ,create_post1 , inbox , Directs ,SendDirect


urlpatterns = [


    path('uploadpost/',views.upload_post,name="upload_post"),

    path('new/<username>', NewConversation, name='newconversation'),
    path('new/', UserSearch, name='usersearch'),
    path('direct/', inbox, name='inbox'),
    path('directs/<username>', Directs, name='directs'),
    path('send/', SendDirect, name='send_direct'),

    path('home/' , create_post1,name= 'home1'),
    path('tolu1/',AddPostView.as_view(),name= 'add_post'),
    path('article/<int:pk>',ArticleDetailView.as_view(),name= 'article-detail'),
    path('must_authentiate/' ,must_authenticate_view, name= 'must_authentiate'),
    path('create_post/' ,create_blog_view, name= 'create_post'),

    
    path('admin/', admin.site.urls),
    path('',HomeView.as_view(), name='home'),
    path('chat/',Chat, name='chat'),
    path('explore/',Explore, name='explore'),
    path('log_out/',Log_out, name='logout'),
    path("login/",Login_view.as_view(),name="login"),
    path('logout/',auth_views.LogoutView.as_view(template_name='testapp/logout.html'),name='logout'),
    path("register/",register,name="register"),
    #
    path('edit_form_page/',views.edit_form,name="edit_form"),
    #
    path('view_profile_page/<int:user_id>', view_profile, name='view_profile'),

     path('edit_profile1/<int:pk>',views.profile_form,name="edit_profile1"),




    path('account/',views.accountSettings, name="account"),



     path('edit_profie_page/<int:pk>', EditProfiePageView.as_view(), name='edit_profie_page'),





# view profile working 
     path('profile/<int:pk>', profile_form, name='profile_form'),

#

# working for user form
    path('profile/<int:pk>', EditProfilePageView.as_view(), name='edit_profile_page'),

#
    path('view_profile_page/<int:pk>/update', Update_profile, name='view_profile_update'),

    path('pass_form_page/', pass_form, name='pass_form'),


    # path('update-profile',views.update_profile,name='update-profile'),

# user profile  going to profile_form.html
    path('profile/<int:user_id>', views.userprofile, name='userprofile'),



    path('view_profile/<int:user_id>',views.view_profile, name ='view_profile'),
     path('view_profile/edit_profile/<int:user_id>', views.edit_profile, name ='edit_profile'),
]

if settings.DEBUG: 
 urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL) 
 urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
