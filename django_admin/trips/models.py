from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    # 標題不可以超過 100 個字元
    content = models.TextField(blank=True)
    # blank = True表示非必填
    photo = models.URLField(blank=True)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now_add=True -- 物件新增的時間。若想設成物件修改時間，則用 auto_now=True
    
    # 使得Post名稱可以是我打的title !
    
    def __str__(self):
        return self.title