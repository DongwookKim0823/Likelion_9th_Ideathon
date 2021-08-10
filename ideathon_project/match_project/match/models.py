from django.db import models

# Create your models here.

class Match(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100) # CharField가 제한적인 문자열이기 때문에 max_length를 이용하여 범위를 지정
    # pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = "match/", blank = True, null = True)

    def __str__(self):
        return self.title

    def summary(self): 
        return self.body[:100] # 슬라이싱을 통해 내용을 100자까지만 보이도록 해주는 기능
