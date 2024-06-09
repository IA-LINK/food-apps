from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Items(models.Model):


    def  __str__ (self):
        return self.item_name
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=11)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,default="http://3.bp.blogspot.com/-6C8L0SXuSHY/T-wlfd9dFJI/AAAAAAAAACg/ILqUp67tJTE/s1600/Fruits.jpg")


    def get_absolute_url(self):
        return reverse("foodz:detail", kwargs={"pk": self.pk})

