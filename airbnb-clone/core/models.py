from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):

    """Time Stamped Model """

    created = models.DateTimeField(auto_now_add=True)  # 생성될 때 시간을 기록
    updated = models.DateTimeField(auto_now=True)  # models이 업데이트 될때 시간을 기록

    # abstract is not going to database
    # if you don't need model what you created to go to database , Use abstract!
    class Meta:
        abstract = True
