from django.db import models
from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify

class Restaurant(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(blank=True)
    description = models.TextField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    logo = models.ImageField(upload_to="restaurant_logos")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

def rest_pre(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.name)

pre_save.connect(rest_pre, sender=Restaurant)

class Item(models.Model):
    restaurant = models.ForeignKey(Restaurant)
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=3)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name',]


def item_pre(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.name)

pre_save.connect(item_pre, sender=Item)