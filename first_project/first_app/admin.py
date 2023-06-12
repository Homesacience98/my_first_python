from django.contrib import admin
from .models import Profile
from.models import Post, Message


# from first_app.models import tags,Chat
admin.site.register(Message)

admin.site.register(Post)
# Register your models here.

admin.site.register(Profile)

# admin.site.register(Post)

# admin.site.register(tags)

# admin.site.register(Comment)

# admin.site.register(Chat)



