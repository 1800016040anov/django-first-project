from django.db import models
 
# Create your models here.
class Member(models.Model):
 
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    nilai = models.IntegerField(default="")
     
    created = models.DateTimeField(auto_now_add=True)
     
    def __str__(self):
        return self.firstname + " " + self.lastname
 
    class Meta:
        ordering = ['created',] 
        db_table = "blog_table"