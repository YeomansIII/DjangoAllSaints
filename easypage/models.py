# coding=utf8
from django.db import models
from django.core.exceptions import ValidationError
from blanc_basic_assets.fields import AssetForeignKey

class QuickLink(models.Model):
    image_file = AssetForeignKey('assets.Image')
    name = models.CharField(max_length=50)
    heading = models.CharField(max_length=20)
    body = models.CharField(max_length=250)
    button_text = models.CharField(max_length=20, default=u'View details »')
    link = models.CharField(max_length=300)

    def __str__(self):              # __unicode__ on Python 2
        return self.name
    def __unicode__(self):              # __unicode__ on Python 2
        return unicode(self.name)

class Carousel(models.Model):
    image_file = AssetForeignKey('assets.Image')
    image_link = models.CharField(max_length=300, blank=True)
    name = models.CharField(max_length=50)
    heading = models.CharField(max_length=50, blank=True)
    body = models.CharField(max_length=150, blank=True)
    button_text = models.CharField(max_length=20, blank=True)
    link = models.CharField(max_length=300, blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.name
    def __unicode__(self):              # __unicode__ on Python 2
        return unicode(self.name)

class Featurette(models.Model):
    image_file = AssetForeignKey('assets.Image')
    name = models.CharField(max_length=50)
    heading1 = models.CharField(max_length=50)
    heading_link = models.CharField(max_length=300, blank=True)
    heading2 = models.CharField(max_length=50, blank=True)
    body = models.CharField(max_length=150)
    button_text = models.CharField(max_length=20, blank=True, default=u'View details »')
    link = models.CharField(max_length=300, blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.name
    def __unicode__(self):              # __unicode__ on Python 2
        return unicode(self.name)
