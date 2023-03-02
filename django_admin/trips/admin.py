from django.contrib import admin

# Register your models here.

#我們需要在讓 Django 知道，有哪些 Model 需要管理後台。修改 trips app 裡的 admin.py，並註冊 Post 這個 Model：


from .models import Post, CAL1


admin.site.register(Post)
admin.site.register(CAL1)