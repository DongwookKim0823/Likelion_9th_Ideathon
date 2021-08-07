from django.db import models

# Create your models here.

class Match(models.Model):
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="match/", blank = True, null = True) #media_url에 등록된 media폴더 안에 match라는 폴더를 만들어서 관리하겠다는 설정



    def __str__(self):
        return self.title #작성한 글이 글 리스트에서 객체명말고 작성한 title로 보여지게됨.

    def summary_body(self):
        return self.body[:15] #본문의 길이를 15자로 제한

    def summary_title(self):
        return self.title[:8]

