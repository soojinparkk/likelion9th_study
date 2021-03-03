from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)        # 제한이 있는 문자열
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()               # 날짜와 시간 저장
    body = models.TextField()                       # 제한이 없는 문자열
    image = models.ImageField(upload_to="blog/", blank=True, null=True)    # upload_to: 업로드할 폴더 지정

    def __str__(self):
        return self.title

    def summery(self):
        return self.body[:100]