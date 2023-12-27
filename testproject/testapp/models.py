
from django.db import models


# class Product(models.Model):
#     name = models.CharField(max_length=255)
#     product_access = models.ForeignKey('ProductAccess', on_delete=models.CASCADE)
class Product(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey("auth.User", on_delete=models.CASCADE)

class Lesson(models.Model):
    name = models.CharField(max_length=255)
    video_link = models.URLField()
    duration_seconds = models.PositiveIntegerField()
    products = models.ManyToManyField(Product, related_name='lessons')

class ProductAccess(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    last_accessed = models.DateTimeField(null=True, blank=True)
    viewed = models.BooleanField(default=False)
    view_time_seconds = models.PositiveIntegerField(default=0)


