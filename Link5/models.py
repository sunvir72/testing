from django.db import models

# Create your models here.
class testmodel(models.Model):
    iflogged=models.BooleanField(default=False)
    curr_name=models.CharField(max_length=200,default='hh')
    curr_email=models.CharField(max_length=200,default='hh@hhh.com')
    ifTeacher=models.BooleanField(default=False)

    def __str__(self):
        return self.curr_name
