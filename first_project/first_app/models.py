from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.urls import reverse
from django.db.models import Max
# Create your models here.


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user')
    sender = models.ForeignKey(User, on_delete=models.CASCADE,related_name='form_user')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE,related_name='to_user')
    body = models.TextField(blank=True, null=True,max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def send_message(from_user, to_user,body):
        sender_message = Message(
            user=from_user,
            sender= from_user,
            recipient=to_user,
            body=body,
            is_read=True)
        sender_message.save()

        recipient_message = Message(
            user=to_user,
            sender=from_user,
            body=body,
            recipient=from_user)
        recipient_message.save()

        return sender_message

    def get_messages(user):
        messages = Message.objects.filter(user=user).values('recipient').annotate(last=Max('date')).order_by('-last')
        users = []

        for message in messages:
            users.append({
                'user': User.objects.get(pk=message['recipient']),
                'last': message['last'],
                'unread': Message.objects.filter(user=user, recipient__pk=message['recipient'], is_read=False).count()

            })

        return users









class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE  ,blank=True,null=True) 
    first_name = models.CharField(max_length=100 ,null=True)
    last_name = models.CharField(max_length=100,null=True)
    profile_pic = models.ImageField(max_length=255,null=True  ,blank=True,default='alaye.jpg')
    #     profile_pic = models.ImageField(default='default.jpg')
    bio = models.CharField(max_length=255,null=True)
    contact = models.CharField(max_length=255 ,null=True)
    location = models.CharField(max_length=255,null=True)
    created_at = models.DateTimeField(default=timezone.now,null=True)
    updated_at = models.DateTimeField(default=timezone.now,null=True)

    def __str__(self):
        return str(self.user.username)

class Post(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE  ,blank=True,null=True) 
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Profile ,on_delete=models.CASCADE)
    body = models.CharField(max_length=500)
    image = models.ImageField(blank=True, null=True,upload_to='static/img',default='alaye.jpg' )
    # created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User , related_name="post_likes", blank=True)

    def number_of_likes(self):
        return self.likes.count()




    def __str__(self):  
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        return reverse('add_post', args=(str(self.id)))


def create_profile(sender,instance,created,**kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

post_save.connect(create_profile, sender=User)




def createProfile(sender, **kwargs):
    if kwargs['created']:user_profile = UserProfile.objects.created(user=kwargs['instance'])
    post_save.connect(createProfile, sender=User)

# class User(models.Model):
#     firstname = models.CharField(max_length=100)
#     username=models.CharField(max_length=100)
#     password=models.CharField(max_length=10)
#     email=models.EmailField()




# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE ,null=True) 
#     bio = models.CharField(max_length=255)
#     profile_pic = models.ImageField(default='default.jpg')
#     # date_created = models.DateTimeField(default=timezone.now)
    
#     def __str__(self):
#         return self.user

# class tags(models.Model):
#     name = models.CharField(max_length=255)
    
#     def __str__(self):
#         return self.name

# class Post(models.Model):
#     # user= models.ForeignKey(User,default=None, on_delete=models.CASCADE)
#     Profile = models.ForeignKey (Profile, default=1, on_delete=models.CASCADE)
#     post_title = models.CharField( verbose_name="post title", max_length=150)
#     tags = models.ManyToManyField(tags, verbose_name="post tags")
#     post_img = models.ImageField(blank=True, null=True,  upload_to='uploads/post_img', verbose_name='Post Image')

#     def __str__(self):
#         return self.post_title
        
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    user= models.ForeignKey(User,default=1, on_delete=models.CASCADE)

    comment = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username
# class Chat(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     message = models.CharField(max_length=255)
    
#     def __str__(self):
#         return self.message


