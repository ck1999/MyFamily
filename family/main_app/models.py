from django.db import models

# Create your models here.
class UserUI(models.Model):
    fio = models.CharField(max_length=40)
    needUser = models.BooleanField(default=False)

class UserUIPosition(models.Model):
    pos_x = models.FloatField()
    pos_y = models.FloatField()
    UserUIConnect = models.ForeignKey(UserUI, on_delete=models.CASCADE)