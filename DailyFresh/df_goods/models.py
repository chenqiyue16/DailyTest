from django.db import models
from tinymce.models import HTMLField
# Create your models here.


class TypeInfo(models.Model):
    t_title = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.t_title

class GoodsInfo(models.Model):
    g_title = models.CharField(max_length=20)
    g_pic = models.ImageField(upload_to='goods')
    g_price = models.DecimalField(max_digits=5, decimal_places=2)
    g_unit = models.CharField(max_length=20,default='500g')
    g_click = models.IntegerField(default=0)
    g_jianjie = models.CharField(max_length=200)
    g_kucun = models.IntegerField(default=0)
    g_content = HTMLField()
    g_type = models.ForeignKey(TypeInfo)
    # a_adv = models.BooleanField(default=False)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.g_title



