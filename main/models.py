from django.db import models
from phone_field import PhoneField


class AnniversaryPosts(models.Model):
    title = models.CharField(max_length=100, verbose_name='기념일 제목')
    content = models.CharField(max_length=500, verbose_name='메시지 내용')
    Anniversary_date = models.DateField('기념일')
    Anniversary_email = models.EmailField(blank=True)
    Anniversary_phone = PhoneField(blank=True)

    class Meta:
        ordering = ['Anniversary_date']

    def __str__(self):
        return self.title