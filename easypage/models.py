# coding=utf8
from django.db import models
from django.core.exceptions import ValidationError
from blanc_basic_assets.models import Image

class QuickLink(models.Model):
    image_file = models.ForeignKey(Image)
    heading = models.CharField(max_length=20)
    body = models.CharField(max_length=250)
    button_text = models.CharField(max_length=20, default=u'View details »')
    link = models.CharField(max_length=300)

    def __str__(self):              # __unicode__ on Python 2
        return self.title
    def __unicode__(self):              # __unicode__ on Python 2
        return unicode(self.heading)

class Carousel(models.Model):
    image_file = models.ForeignKey(Image)
    heading = models.CharField(max_length=50)
    body = models.CharField(max_length=150)
    button_text = models.CharField(max_length=20)
    link = models.CharField(max_length=300)

    def __str__(self):              # __unicode__ on Python 2
        return self.heading
    def __unicode__(self):              # __unicode__ on Python 2
        return unicode(self.heading)
