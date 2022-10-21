from django.db import models

# Create your models here.
class DataOrigin(models.Model):
    # def __str__(self):
    #     return self.name
    temperature = models.FloatField(default=0, null=False)
    count = models.FloatField(default=0)

class DataSex(models.Model):
    # def __str__(self):
    #     return self.name
    temperature = models.FloatField(default=0, null=False)
    count = models.FloatField(default=0)
    sex = models.CharField(default='',max_length=3)

class DataAge(models.Model):
    # def __str__(self):
    #     return self.name
    temperature = models.FloatField(default=0, null=False)
    count = models.FloatField(default=0)
    age = models.CharField(default='',max_length=4)