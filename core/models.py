from django.db import models




types = [('1','1'),('2','2'),('3','3')]
types1 = [('1','1'),('2','2'),('3','3'),('4','4')]
class Profile(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    date = models.DateField()
    phone = models.BigIntegerField()
    email = models.EmailField()
    ranking = models.CharField(choices=types1,max_length=20,null=True,blank=False,default='year')
    profession = models.CharField(max_length=200)
    status = models.CharField(choices=types,max_length=20,null=True,blank=False,default='section')
    present = models.BooleanField(default=False)
    image = models.ImageField()
    updated = models.DateTimeField(auto_now=True)
    shift = models.CharField(max_length=200)
    def __str__(self):
        return self.first_name +' '+self.last_name


class LastFace(models.Model):
    last_face = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.last_face

