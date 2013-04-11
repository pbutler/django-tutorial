from django.db import models

# Create your models here.


class Entry(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    entry = models.ForeignKey(Entry)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __unicode__(self):
        return self.subject
